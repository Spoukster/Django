from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return render(request, 'main/index.html')

    # template = Template('Hello {{ name }}')
    # context = Context({'name': 'Yuriy'})

    template = get_template('main/index.html')
    context = {'name': 'Yuriy'}
    return HttpResponse(template.render(context))


def about(request):
    return render(
        request,
        'main/about.html',
        {
            'about_text': 'Это страница о Проекте'
        }
    )


def contacts(request):
    # return render(request, 'main/contacts.html')
    rendered_page = render_to_string(
        'main/contacts.html',
        {
            'contacts': [
                'Контакт 1',
                'Контакт 2',
                'Контакт 3'
            ]
        }
    )
    return HttpResponse(rendered_page)
