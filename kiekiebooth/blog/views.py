from django.shortcuts import render

#post details displayed on home.html
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 8, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 9, 2019'
    }
]

#function to display info on home page
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context, {'title' : 'Home'})
   
#function to display info on about page   
def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
