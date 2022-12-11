from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Article
from .forms import ArticleForm


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/update.html'
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'news/delete.html'
    success_url = '/news/'


def news_home(request):
    news = Article.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была не верной'
    else:
        form = ArticleForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)
