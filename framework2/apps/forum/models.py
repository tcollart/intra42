from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

"""
    Category:
        - Name

    ChildCategory(Category):
        - Name
        - Category

    Threads:
        - Author
        - Message
        - Category / ChildCategory
        - First thread, Answer or Comment
"""


class BaseCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BaseCategory, self).save(*args, **kwargs)


class Category(BaseCategory):
    pass


class ChildCategory(BaseCategory):
    father = models.ForeignKey(Category, related_name='FatherCategory')


class BasePost(models.Model):
    author = models.ForeignKey(User, related_name='ThreadUser')
    message = models.TextField(max_length=10000, blank=False)


class Thread(BasePost):
    title = models.CharField(max_length=100, blank=False)
    category = models.ForeignKey(BaseCategory, related_name='OriginalCategory')

    def __str__(self):
        return self.title


class Answer(BasePost):
    originalthread = models.ForeignKey(Thread, related_name='AnswerThread')


class Comment(models.Model):
    thread = models.ForeignKey(BasePost, related_name='CommentThread')
    author = models.ForeignKey(User, related_name='CommentAuthor')
    message = models.TextField()