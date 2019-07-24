from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField

def _category_image_path(instance, filename):
    return 'categories/{}/{}'.format(instance.name, filename)

class Category(models.Model):
    """
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50)
    description = RichTextField(default='', blank=True, null=True)
    img_url = models.ImageField(_('Image'),
                                upload_to = _category_image_path,
                                blank=True, null=True)
    ordering = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True,
                                    help_text=_('If active, is visible'))

    class Meta:
        ordering = ['ordering', 'name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def has_active_conditions(self):
        active_conditions = Item.objects.filter(category=self,
                                                              is_active=True)
        return active_conditions

    def __str__(self):
        return '{}'.format(self.name)


class Item(models.Model):
    """
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = RichTextField(default='', blank=True, null=True)
    img_url = models.ImageField(_('Image'),
                                upload_to = _category_image_path,
                                blank=True, null=True)
    ordering = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True,
                                    help_text=_('If active, is visible'))

    class Meta:
        ordering = ['ordering', 'name']
        verbose_name = _('Info Item')
        verbose_name_plural = _('Info Items')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)
