from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post, Project, Review
from sPortFolio.settings import PROJECT_ROOT
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, FormView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required




def aboutView(request):
    return render(request, "about.html")

# @login_required
# def message_to_user(request):
#     if request.method == "POST":
#         form = MessageForm(request, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("message_sent")
#     else:
#         form = MessageForm(request)

#     return render(request,
#                   "email_messages/message_to_user.html",
#                   {"form": form})

# @login_required
# def message_sent(request):
#     return render(request,
#                   "email_messages/message_sent.html")


class BlogListView(ListView):
    model = Post
    print('STATIC_ROOT' + PROJECT_ROOT)
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'project.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'review.html', {'reviews': reviews})
