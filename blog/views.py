from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post # .model is because it is in the same directory as viewss.py
from django.views.generic import (ListView, DetailView
, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# Create your views here.

# posts = [
#     {
#         'author':'Demehin Ibukun',
#         'title': 'Creating blog website',
#         'content':'It is still boothing',
#         'date_posted':'26 May 2020',
#     },
#     {
#         'author':'Demehin Mayowa',
#         'title': 'Creating blog website again',
#         'content':'It is still boothing again',
#         'date_posted':'30 May 2020',
#     },
# ]

def home(request):
    # context = {
    #     'posts':posts
    # }
    # return render(request,'blog/home.html', context)
    context = {
        'posts':Post.objects.all()
    }
    
    return render(request,'blog/home.html', context)

class PostListView(ListView): #same as def home(request)
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html: this is the default pattern of html class based views look for, but we changed it here with this variable to another template of our choosing
                                    #blog/post_list.html
    context_object_name = 'posts' #<model>_<viewtype>: this is the default object that contains a full list of all post in the model. We changed it here in this variable name on this line
                                    #post_list
    ordering = ['-date_posted']

    paginate_by = 5

class UserPostListView(ListView):
    model=Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView): # it expects a <model>_form.html template in blog folder under templates
    model = Post
    fields = ['title', 'content']# fields = __all__
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # it expects a <model>_form.html template in blog folder under templates
    model = Post
    fields = ['title', 'content']# fields = __all__
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): #Login followed by user followed by detail. you must follow this order as the class will inherit them from left to right
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'New ABout'})



# class based view
# 1. list view
# 2. detail views
# 3. create views
# 4. update views
# 5. delete view
# 6. template view
# 7. form view