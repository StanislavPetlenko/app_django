from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    data = {
        'home_page_name': 'Home page',
        'values': ['Some', 'Hello', '1234']
    }
    # return HttpResponse('<h3>This is home page from site</h3>')
    return render(request, 'main_page/home.html', data)


def about(request):
    # return HttpResponse('<h3>Now you may read about us</h3>')
    return render(request, 'main_page/about.html')


def contacts(request):
    # return HttpResponse('<h3>Now you may read about us</h3>')
    return render(request, 'main_page/contacts.html')