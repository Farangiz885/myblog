from django.shortcuts import render

from .models import Posts

def post_list(request):
    posts = Posts.objects.all()
    print(posts)
    return render(request, 'ok')

# Create your views here.
