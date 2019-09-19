from wagtail.core import blocks


class EventConfirmBlock(blocks.ChoiceBlock):
    CONFIRMATION_YES = 1
    CONFIRMATION_NO = 0

    choices = (
        (CONFIRMATION_YES, "Yes"),
        (CONFIRMATION_NO, "No"),
    )


class EventBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True, max_length=264, help_text="event name")
    date = blocks.DateBlock(required=True)
    to_be_confirmed = EventConfirmBlock(required=True)


class EventListBlock(blocks.StructBlock):
    events = blocks.ListBlock(
        EventBlock()
    )

    class Meta:
        template = "streams/event_list_block.html"
        icon = "date"
        label = "Event list panel"
