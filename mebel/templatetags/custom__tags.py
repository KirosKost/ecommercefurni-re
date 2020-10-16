from django import template

register = template.Library()


@register.filter(name='class')
def add_css(field, class_name):
    return field.as_widget(attrs={'class': class_name})
