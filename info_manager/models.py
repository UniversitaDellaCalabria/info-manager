from django.conf import settings
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

    def active_items(self):
        return Item.objects.filter(category=self, is_active=True)

    def translate_as(self, lang):
        """
        returns translation if available
        """
        trans = CategoryTranslation.objects.filter(category=self,
                                                   lang=lang,
                                                   is_active=True)
        if trans: return trans.first()
        else: return self

    def __str__(self):
        return '{}'.format(self.name)


class CategoryTranslation(models.Model):
    """
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    lang = models.CharField(choices=settings.LANGUAGES, max_length=3)
    name = models.CharField(max_length=255)
    description = RichTextField(default='', blank=True, null=True)
    is_active = models.BooleanField(default=True,
                                    help_text=_('If active, is visible'))

    @property
    def slug(self):
        return self.category.slug

    class Meta:
        ordering = ['lang']
        verbose_name = _('Category translation')
        verbose_name_plural = _('Categories translations')

    def __str__(self):
        return '{} [{}]'.format(self.category, self.lang)


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
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ordering', 'name']
        verbose_name = _('Info Item')
        verbose_name_plural = _('Info Items')

    def active_translations(self):
        return ItemTranslation.objects.filter(item=self, is_active=True)

    def translate_as(self, lang):
        """
        returns translation if available
        """
        trans = ItemTranslation.objects.filter(item=self,
                                               lang=lang,
                                               is_active=True)
        if trans: return trans.first()
        else: return self


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.name)


class ItemTranslation(models.Model):
    """
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    lang = models.CharField(choices=settings.LANGUAGES, max_length=3)
    name = models.CharField(max_length=255)
    description = RichTextField(default='', blank=True, null=True)
    is_active = models.BooleanField(default=True,
                                    help_text=_('If active, is visible'))

    class Meta:
        ordering = ['lang']
        verbose_name = _('Info Item translation')
        verbose_name_plural = _('Info Items translations')

    def __str__(self):
        return '{} [{}]'.format(self.item, self.lang)
