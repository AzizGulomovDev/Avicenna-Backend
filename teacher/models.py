from django.db import models
from django.utils import timezone
from django.utils.translation import  gettext_lazy as _
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Subject"),help_text=_("Enter subject name"))
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Fan"
        verbose_name = _("Fanlar ")
        verbose_name_plural= _("Fanlar ")
class Teacher(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Ism sharif"),help_text=_("O'qituvchi ism sharifi ..."))
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    one_id = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name=_("Telefon raqami"), help_text=_("Telefon raqamini kiriting ..."))
    # salary = models.CharField(max_length=600,verbose_name=_("Salary"))
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.id:
            self.one_id = self.id +1000
        super(Teacher, self).save(*args, **kwargs)
    class Meta:
        db_table = "O'qituvchi"
        verbose_name = _("O'qituvchi ")
        verbose_name_plural = _("O'qituvchilar ")
class BlokTestlar(models.Model):
    image_file = models.CharField(max_length=15)
    week_code = models.CharField(max_length=100)
    fio = models.CharField(max_length=100)
    first_block = models.CharField(max_length=100)
    second_block = models.CharField(max_length=100)
    fan1= models.IntegerField()
    fan2= models.IntegerField()
    ona_tili=models.IntegerField()
    tarix= models.IntegerField()
    matematika = models.IntegerField()
    ball = models.CharField(max_length=10)
    local_number = models.CharField(max_length=30)
    sms_status = models.CharField(max_length=10)
    global_number = models.CharField(max_length=15)
    global_id = models.CharField(max_length=10)
    week_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Test"
    class Meta:
        verbose_name = "Blok Testlar"
        verbose_name_plural = "Blok Testlar"
class FanTest(models.Model):
    test_kodi = models.CharField(max_length=100)
    fan_nomi = models.CharField(max_length=100)
    oquvchi = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    teacher = models.CharField(max_length=50,default="G'ulomov Azizbek")
    test_soni = models.IntegerField()
    togri_javoblar= models.IntegerField()
    sana = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.fan_nomi} fanidan imtihon!"
    class Meta:
        verbose_name = "Fan Testlar"
        verbose_name_plural = "Fan Testlar"


