from django.db import models

from modelcluster.fields import ParentalKey

from django.contrib import messages

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.models import Image
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from .email import send_form_email
from .forms import ContactForm

class HomePage(Page):
    body = RichTextField(blank=True)
    splash_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    splash_image_caption = models.CharField(blank=True, max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        MultiFieldPanel([
            ImageChooserPanel('splash_image'),
            FieldPanel('splash_image_caption'),
        ], 
            heading="Splash image"        
        )
        
    ]

class Contact(Page):
    email = models.EmailField(default="rim.kozlowski@gmail.com", verbose_name="Email hosta")
    # subtitle = models.TextField(verbose_name="Podtytuł")
    # title_main = models.TextField(verbose_name="Tytuł")
    # description = RichTextField(verbose_name="Opis")
    # subtitle_contact = models.TextField(verbose_name="Podtytuł")
    # title_contact = models.TextField(verbose_name="Tytuł")

    # content_panels = Page.content_panels + [
    #     # FieldPanel('email'),

    #     # MultiFieldPanel([
    #     #     FieldPanel('subtitle'),
    #     #     FieldPanel('title_main'),
    #     #     FieldPanel('description'),

    #     # ],
    #     #     heading="Informacje główne",
    #     #     classname="collapsible collapsed"
    #     # ),

    #     # MultiFieldPanel([
    #     #     FieldPanel('subtitle_contact'),
    #     #     FieldPanel('title_contact'),
    #     #     InlinePanel('management_persons', label='Członek zarządu'),
    #     #     InlinePanel('project_management_persons', label='Członek project management'),
    #     #     InlinePanel('sales_department_persons', label='Członek działu handlowego'),
    #     #     InlinePanel('purchasing_department_persons', label='Członek działu zakupów'),

    #     # ],
    #     #     heading="Kadra",
    #     #     classname="collapsible collapsed"
    #     # ),

    # ]

    def get_context(self, request, **kwargs):
        context = super(Contact, self).get_context(request)
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                send_form_email('Formularz kontaktowy ze strony', 'x', form, self.email)
                messages.info(request, 'Formularz został wysłany.')
            else:
                messages.error(request, 'Formularz zawiera błędy.')
        else:
            form = ContactForm()
        context['form'] = form
        return context
