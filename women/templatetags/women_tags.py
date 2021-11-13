from django import template
from women.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats' : cats, 'cat_selected' : cat_selected}

@register.inclusion_tag('women/menu.html', takes_context=True)
def menu(context):
    menu = [{'title': "О сайте", 'url_name': 'about'},
         {'title': "Добавить статью", 'url_name': 'add_page'},
         ]

    if not context['request'].user.is_authenticated:
        menu.pop(1)
    else:
        context['menu'] = menu
    return context