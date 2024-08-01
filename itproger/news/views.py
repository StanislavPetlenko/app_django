from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def home_news(request):
    # news = Article.objects.all()
    news = Article.objects.order_by('-pub_date')[:]  # - same that DESC else ASC; get 0, 1 element
    return render(request, 'news/news_home_page.html', {'news': news})


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