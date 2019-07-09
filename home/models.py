from flex.models import AbstractFlexPage


class HomePage(AbstractFlexPage):
    """ Home page model"""
    template = "flex/flex_page.html"

    max_count = 1

    class Meta:
        verbose_name = "Home page"
        verbose_name_plural = "Home pages"
