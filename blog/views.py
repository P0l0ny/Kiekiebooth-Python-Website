from django.shortcuts import render
from .models import Post


#function to display info on home page
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context, {'title' : 'Home'})
   
#function to display info on about page   
def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
