from wagtail.images.formats import Format, unregister_image_format, register_image_format
from django.utils.translation import ugettext_lazy as _


class ImageFigureFormat(Format):

    def image_to_html(self, *args, **kwargs):
        return "<figure>{}</figure>".format(super().image_to_html(*args, **kwargs))


unregister_image_format('fullwidth')
unregister_image_format('left')
unregister_image_format('right')

register_image_format(
    ImageFigureFormat('fullwidth', _('Full width'), 'richtext-image full-width', 'width-800')
)
register_image_format(
    ImageFigureFormat('left', _('Left-aligned'), 'richtext-image left', 'width-500')
)
register_image_format(
    ImageFigureFormat('right', _('Right-aligned'), 'richtext-image right', 'width-500')
)
