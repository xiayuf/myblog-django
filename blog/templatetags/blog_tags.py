from django import template

from ..models import Post, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_article_items():
    return Post.objects.all().order_by('-created_time')

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_tag_items():
    return Tag.objects.all()