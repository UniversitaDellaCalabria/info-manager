from django.conf import settings
from django.shortcuts import render
from django.utils import translation

from . models import *

def info_manager_index(request):
    language = request.session.get('language') or settings.LANGUAGE_CODE

    if request.method == 'GET' and 'lang' in request.GET:
        for k,v in settings.LANGUAGES:
            if k == request.GET['lang']:
                language = k
                request.session['language'] = k
                break

    if translation.get_language() != language:
        translation.activate(language)

    template = "info_manager_index.html"
    categories = Category.objects.filter(is_active='True')
    d = {'categories': categories}
    return render(request, template, d)
