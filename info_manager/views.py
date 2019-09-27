from django.conf import settings
from django.shortcuts import render
from django.utils import translation
from django.shortcuts import get_object_or_404

from . models import *


def info_manager_index(request):
    categories = Category.objects.filter(is_active=True)
    lang = request.GET.get('lang',
                           translation.get_language_from_request(request))
    d = {'categories': [cat.translate_as(lang=lang)
                        for cat in categories]
    }
    return render(request, "info_manager_index.html", d)


def info_page(request, slug):
    lang = request.GET.get('lang',
                           translation.get_language_from_request(request))
    category = get_object_or_404(Category, slug=slug)
    data = {'category': category,
            'active_items': [item.translate_as(lang=lang)
                             for item in category.active_items()]}
    return render(request, "info_page.html", data)
