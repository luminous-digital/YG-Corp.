from wagtail.core import blocks

from .rte import RichTextBlock


class LeftColumnItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255, help_text="add title")
    email = blocks.CharBlock(required=False, max_length=255, help_text="add email")


class LeftColumnContact(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255, help_text="add title")
    sub_title = blocks.CharBlock(required=False, max_length=255, help_text="add sub title")

    items = blocks.ListBlock(
        LeftColumnItemBlock(required=False)
    )


class RightColumnItemBlock(blocks.StructBlock):
    city = blocks.CharBlock(required=False, max_length=255, help_text="add city")
    address_line_1 = blocks.CharBlock(required=False, max_length=255, help_text="add address")
    address_line_2 = blocks.CharBlock(required=False, max_length=255, help_text="add address")
    address_line_3 = blocks.CharBlock(required=False, max_length=255, help_text="add address")
    country = blocks.CharBlock(required=False, max_length=255, help_text="add country")
    right_column_text_editor = RichTextBlock(required=False, label="Right column text")
    telephone = blocks.CharBlock(required=False, max_length=255, help_text="add telephone")
    email_address = blocks.CharBlock(required=False, max_length=255, help_text="add email")
    website = blocks.URLBlock(required=False, help_text="add website address")


class RightColumnContact(blocks.StructBlock):
    title = blocks.CharBlock(required=False, max_length=255, help_text="add title")
    items = blocks.ListBlock(
        RightColumnItemBlock(required=False)
    )


class ContactInfoBlock(blocks.StructBlock):
    left_column = LeftColumnContact(required=False)
    right_column = RightColumnContact(required=False)
    contact_text_editor = RichTextBlock(required=False, label="Contact text editor")

    class Meta:
        template = "streams/contact_block.html"
        icon = "mail"
        label = "Contact panel"
