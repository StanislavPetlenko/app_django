from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


def home_news(request):
    # news = Article.objects.all()
    news = Article.objects.order_by('-pub_date')[:]  # - same that DESC else ASC; get 0, 1 element
    return render(request, 'news/news_home_page.html', {'news': news})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm
    # fields = ['title', 'anons', 'full_text', 'pub_date']


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def create_new(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_news')
        else:
            error = 'Невірно заповнена форма'
    form = ArticleForm()
    data = {'form': form,
            'error': error}
    return render(request, 'news/create.html', data)