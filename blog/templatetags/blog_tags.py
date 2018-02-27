from django import template
from django.db.models.aggregates import Count

from ..models import Post, Category, Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]
    
@register.simple_tag
def get_article_items():
    return Post.objects.all().order_by('-created_time')

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return Category.objects.annotate(num_posts=Count('post')).filter()

@register.simple_tag
def get_tag_items():
    #return Tag.objects.all()
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)