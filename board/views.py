from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from .models import Post, Message, Category, User
from .forms import PostForm, MessageForm
from .filter import PostFilter, MessageFilter
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class ProfileView(DetailView):
    model = User
    template_name = 'profile_list.html'
    context_object_name = 'user_one'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_not_author'] = not self.request.user.group.filter(name='authors').exists()
    #     return context


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts_all'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post_one'


@method_decorator(login_required(login_url='post_one'), name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'author_create_post.html'
    context_object_name = 'post_create'

    def form_valid(self, form):
        post_1 = form.save(commit=False)
        post_1.save()
        return super().form_valid(form)


@method_decorator(login_required(login_url='post_one'), name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'author_update_post.html'
    form_class = PostForm
    context_object_name = 'post_update'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


@method_decorator(login_required(), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'author_delete_post.html'
    success_url = reverse_lazy('posts')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'user_create_message.html'
    context_object_name = 'message_create'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        message = form.save(commit=False)
        post = Post.objects.get(pk=self.kwargs['pk'])
        message.on_post = post
        message.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_heading'] = Post.objects.get(pk=self.kwargs['pk']).heading
        return context


@method_decorator(login_required, name='dispatch')
class MessageDeleteView(MessageCreateView, DetailView):
    model = Message
    template_name = 'user_delete_message'
    context_object_name = 'message_one'


class MessageListView(ListView):
    model = Message
    template_name = 'messages.html'
    context_object_name = 'messages_all'

    def get_queryset(self):
        queryset = super().queryset()
        self.filterset = MessageFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


@method_decorator(login_required, name='dispatch')
class MessageDetailView(MessageCreateView, DetailView):
    model = Message
    template_name = 'message_one.html'
    context_object_name = 'message_one'


#-----------------------------------------------------------------------------------------------------------------------


class CategoryView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_post_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category)
        return queryset





