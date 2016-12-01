from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, extra_classes):
    classes = value.css_classes(extra_classes)
    return value.as_widget(attrs={'class': classes})
