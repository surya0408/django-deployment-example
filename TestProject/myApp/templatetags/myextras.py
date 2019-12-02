from django import template

register = template.Library()

@register.filter(name='sayHi')
def sayHi(value):
	return 'Hi'+value