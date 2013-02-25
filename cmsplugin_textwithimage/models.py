from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _
from cms.models import CMSPlugin
from tinymce import models as tinymce_models



class TextWithImage(CMSPlugin):
    class Meta:
        verbose_name = 'Text mit Bild'
        verbose_name_plural = 'Text mit Bild'

    created = models.DateTimeField(_('Created'), auto_now_add = True)
    modified = models.DateTimeField(_('Modified'), auto_now = True)

    title = models.CharField(_('Title'), max_length=200, blank=True, null=True)
    #content = models.TextField(_('Content'), blank=True, null=True)
    content = tinymce_models.HTMLField()  
    image = models.ImageField(_('Image'), upload_to = 'uploads/images/textwithimage/', max_length=255, null=True, blank=True )
    image_description = models.CharField(_('Image description'), max_length=200, blank=True, null=True)
    
    IMAGE_POSITION_CHOICES = (
        ('left', _('Image left')),
        ('right', _('Image right')),
        ('bottom', _('Image bottom')),
        ('top', _('Image top')),
    )
    image_position = models.CharField(_('Image position'), max_length=6, choices=IMAGE_POSITION_CHOICES)

    IMAGE_BORDER_CHOICES = (
        ('border1', _('Border 1')),
        ('border2', _('Border 2')),
        ('border3', _('Border 3')),
    )
    image_border = models.CharField(_('Image border'), max_length=8, choices=IMAGE_BORDER_CHOICES, null=True, blank=True)

    is_published = models.BooleanField(_('Published'), default=True)

    def __unicode__(self):
        return self.title



