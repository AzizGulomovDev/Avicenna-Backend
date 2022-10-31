from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class BotUsers(models.Model):
    telegram = models.CharField(max_length=100,unique=True)
    fullname = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.fullname
    class Meta:
        verbose_name = _("Bot foydalanuvchilari")
        verbose_name_plural = _("Bot foydalanuvchilari")