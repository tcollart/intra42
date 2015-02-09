from django.contrib.auth.models import User


class ImpersonateMiddleware(object):
    """
    log in: http://localhost/?__logas=[USERID]
    log out (back to admin): http://localhost/?__unlogas=True
    """
    def process_request(self, request):
        if request.user.is_superuser and "__logas" in request.GET:
            request.session['logas_slug'] = request.GET["__logas"]
        elif "__unlogas" in request.GET:
            del request.session['logas_slug']
        if request.user.is_superuser and 'logas_slug' in request.session:
            request.user = User.objects.get(username=request.session['logas_slug'])


