from django import template
from custom.models import FooterSnippet

register = template.Library()


# Footer snippets
@register.inclusion_tag('custom/footer.html', takes_context=True)
def footer_elements(context):
    return {
        'footer_elements': FooterSnippet.objects.all(),
        'request': context['request'],
    }
