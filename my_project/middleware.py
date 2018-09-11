from django.http import HttpResponseRedirect

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path not in ('/admin/', '/login/'):
            if not request.user.is_authenticated:
                print("Working?")
                return HttpResponseRedirect('/login/')

        response = self.get_response(request)

        return response