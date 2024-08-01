from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'pub_date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва новини',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Короткий опис новини',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Повний текст новини',
            }),
            'pub_date': DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Дата та час публікації',
            }),
        }