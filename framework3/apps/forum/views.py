from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView

from .models import *


def global_view(request):

    categories = {}

    for category in Category.objects.all():
        categories[category] = []

    for childcategory in ChildCategory.objects.all():
        categories[childcategory.father].append(childcategory)

    return render(request, 'global.html', {'categories': categories})


def category_view(request, category_slug):

    category_id = Category.objects.get(slug=category_slug)
    childcategories = ChildCategory.objects.filter(father=category_id)
    posts = Thread.objects.filter(category=category_id)

    return render(request, 'category.html',
                  {'category': category_id,
                   'childcategories': childcategories,
                   'posts': posts})


def childcategory_view(request, category_slug, childcategory_slug):

    category_id = Category.objects.get(slug=category_slug)
    childcategory_id = ChildCategory.objects.get(slug=childcategory_slug)

    posts = Thread.objects.filter(category=childcategory_id) if ChildCategory.objects.get(pk=childcategory_id).father == category_id else []
    return render(request, 'childcategory.html',
                  {'category': category_id,
                   'childcategory': childcategory_id,
                   'posts': posts})


class CreateThread(CreateView):
    template_name = 'createthread.html'
    model = Thread
    fields = ['title', 'message']

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.kwargs['childcategory_slug'] != "category":
            form.instance.category = ChildCategory.objects.get(slug=self.kwargs['childcategory_slug'])
        else:
            form.instance.category = Category.objects.get(slug=self.kwargs['category_slug'])
        form.save()
        return super(CreateThread, self).form_valid(form)

    def get_success_url(self):
        if self.kwargs['childcategory_slug'] != "category":
            return "/forum/{category}/{childcategory}/{thread_id}/".format(category=self.kwargs['category_slug'],
                                                                           childcategory=self.kwargs['childcategory_slug'],
                                                                           thread_id=str(self.object.id))
        else:
            return "/forum/{category}/{thread_id}/".format(category=self.kwargs['category_slug'],
                                                           thread_id=str(self.object.id))

    def get_context_data(self, **kwargs):
        context = super(CreateThread, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category_slug'])
        if self.kwargs['childcategory_slug'] != "category":
            context['childcategory'] = ChildCategory.objects.get(slug=self.kwargs['childcategory_slug'])
        return context


def thread_view(request, category_slug, childcategory_slug, thread_id):

    if request.user.is_authenticated() and request.method == 'POST':
        if request.POST['type'] == 'answer':
            answer = Answer(author=User.objects.get(username=request.POST['author']),
                            message=request.POST['message'],
                            originalthread=Thread.objects.get(pk=thread_id))
            answer.save()
        elif request.POST['type'] == 'comment':
            if 'threadid' in request.POST:
                model_to_use = Thread
                key = 'threadid'
            else:
                model_to_use = Answer
                key = 'answerid'
            comment = Comment(author=User.objects.get(username=request.POST['author']),
                              message=request.POST['message'],
                              thread=model_to_use.objects.get(pk=request.POST[key]))
            comment.save()

    category_id = Category.objects.get(slug=category_slug)
    childcategory_id = ChildCategory.objects.get(slug=childcategory_slug) if childcategory_slug != 'category' else None

    if not Thread.objects.filter(category_id=childcategory_id if childcategory_id else category_id):
        return HttpResponse(status=404)

    thread_obj = Thread.objects.get(pk=thread_id)
    thread = {'title': thread_obj.title,
              'id': thread_obj.id,
              'message': thread_obj.message,
              'author': thread_obj.author,
              'comments': Comment.objects.filter(thread=thread_id)}

    answers = []
    for answer_obj in Answer.objects.filter(originalthread=thread_id):
        answers.append({
            'id': answer_obj.id,
            'message': answer_obj.message,
            'author': answer_obj.author,
            'comments': Comment.objects.filter(thread=answer_obj.basepost_ptr.id)
        })

    return render(request, 'thread.html',
                  {'thread': thread,
                   'answers': answers,
                   'category': category_id,
                   'childcategory': childcategory_id})
