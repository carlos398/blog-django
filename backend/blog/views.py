from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Post

class BlogHomePageView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.postobjects.all()
        return context


class DetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.filter(slug = self.kwargs.get('slug'))
        return context