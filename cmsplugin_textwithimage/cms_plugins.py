#from django.utils.translation import ugettext_lazy as _
#from django.utils.translation import ugettext as _
from django.db import models
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_textwithimage.models import *


class TextWithImagePlugin(CMSPluginBase):
    model = TextWithImage
    name = "Text mit Bild"
    render_template = "text_with_image.html"
    
    def render(self, context, instance, placeholder):

        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(TextWithImagePlugin)
