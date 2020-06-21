from django.http import HttpResponse

def index(request):
    return HttpResponse("你好,这是你的博客页面.")
