from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import *
from .forms import *


class PostView(ListView):
    paginate_by = 2
    model = Post
    template_name = 'blog/PostList.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context



class PostCategoryView(ListView):
    paginate_by = 2
    model = Post
    template_name = 'blog/PostList.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['cat_id'] = self.kwargs['cat_id']
        return context

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['cat_id'])


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/PostDetail.html'
    slug_url_kwarg = 'post_slug'


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'blog/PostCreate.html'
    success_url = reverse_lazy('PostList')


class PostEdit(UpdateView):
    model = Post
    template_name = 'blog/PostCreate.html'
    success_url = reverse_lazy('PostList')
    slug_url_kwarg = 'post_slug'
    fields = '__all__'


class AddCategory(CreateView):
    form_class = AddCategoryForm
    template_name = 'blog/CreateCategory.html'
    success_url = reverse_lazy('PostList')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/Register.html'
    success_url = reverse_lazy('PostList')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/Login.html'

    def get_success_url(self):
        return reverse_lazy('PostList')


def logOutUser(request):
    logout(request)
    return redirect('Login')


class MovieList(ListView):
    model = Movie
    template_name = 'blog/MovieList.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()
        return context


class MovieCategoryView(ListView):
    model = Movie
    template_name = 'blog/MovieList.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()
        return context

    def get_queryset(self):
        return Movie.objects.filter(genre_id=self.kwargs['genre_id'])