from django.conf import settings
from django.shortcuts import render
from django.utils import translation
from django.shortcuts import get_object_or_404

from . models import *


def _set_lang(request):
    language = request.session.get('language') or settings.LANGUAGE_CODE
    if request.method == 'GET' and 'lang' in request.GET:
        for k,v in settings.LANGUAGES:
            if k == request.GET['lang']:
                language = k
                request.session['language'] = k
                break

    if translation.get_language() != language:
        translation.activate(language)


def info_manager_index(request):
    _set_lang(request)
    template = "info_manager_index.html"
    categories = Category.objects.filter(is_active=1)
    d = {'categories': categories,}
    return render(request, template, d)


def info_page(request, slug):
    _set_lang(request)

    lang = request.GET.get('lang',
                           translation.get_language_from_request(request))
    template = "info_page.html"
    category = get_object_or_404(Category, slug=slug)
    data = {'category': category,
            'active_items': [item.translate_as(lang=lang)
                             for item in category.active_items()]}
    return render(request, template, data)
