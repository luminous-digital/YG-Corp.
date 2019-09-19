from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImagePersonBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text="choose image")
    name = blocks.CharBlock(required=True, max_length=255, help_text="add name and surname")
    title = blocks.CharBlock(required=True, max_length=255, help_text="add title")
    appointed = blocks.DateBlock(required=False)
    biography = blocks.TextBlock(required=True, help_text="biography about")
    committees = blocks.CharBlock(required=False, max_length=255)

    class Meta:
        template = "streams/image_person_block.html"
        icon = "user"
        label = "Person panel"


class ImagePeopleBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        ImagePersonBlock()
    )

    class Meta:
        template = "streams/image_people_block.html"
        icon = "group"
        label = "People panel"
