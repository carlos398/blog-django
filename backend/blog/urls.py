import imp
from django.urls import path
from .views import (
    BlogHomePageView,
    DetailView
    )

app_name = 'blog'

urlpatterns = [
    path("", BlogHomePageView.as_view(), name="home"),
    path("<slug:slug>/", DetailView.as_view(), name="post_detail"),
]