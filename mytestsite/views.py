from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Please check the news and polls")
