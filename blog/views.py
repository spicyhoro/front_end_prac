from django.shortcuts import render,get_object_or_404, resolve_url
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Comment
from django.urls import reverse_lazy
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .serializers import PostSerializer

import time


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 2

    def get_template_names(self):
        if self.request.is_ajax():
            return ['blog/_post_list.html']
        return ['blog/index.html']




index = PostListView.as_view()
post_new = CreateView.as_view(model=Post, fields="__all__")
post_detail = DetailView.as_view(model=Post)
post_edit = UpdateView.as_view(model=Post, fields='__all__')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

class CommentCreatView(CreateView):
    model = Comment
    fields = ['message']

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk']) #kwargs는 url인자
        return super().form_valid(form)

    def get_success_url(self):
        #현재 저장한 object가 self.object에 존재함!!!
        return resolve_url(self.object.post)

comment_new = CommentCreatView.as_view()

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['message']

    def get_success_url(self):
        # 현재 저장한 object가 self.object에 존재함!!!(self.commnet인득?)
        return resolve_url(self.object.post)

comment_edit = CommentUpdateView.as_view(model=Comment, fields=['message'])

class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        # 현재 저장한 object가 self.object에 존재함!!!(self.commnet인득?)
        return resolve_url(self.object.post)

comment_delete = CommentDeleteView.as_view(model=Comment)


def post_list_json(request):
    qs = Post.objects.all()

    serializer = PostSerializer(qs, many=True)
    json_utf8_string = JSONRenderer().render(serializer.data)
    return HttpResponse(json_utf8_string, content_type='application/json; charset=utf-8')

