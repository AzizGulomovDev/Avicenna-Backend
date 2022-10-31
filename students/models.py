from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.utils.html import format_html
viloyat = (
    ("Andijon","Andijon"),
    ("Buxoro","Buxoro"),
    ("Farg'ona","Farg'ona"),
    ("Jizzax","Jizzax"),
    ("Namangan","Namangan"),
    ("Navoiy","Navoiy"),
    ("Qashqadaryo","Qashqadaryo"),
    ("Qoraqalpog'iston","Qoraqalpog'iston"),
    ("Samarqand","Samarqand"),
    ("Sirdaryo","Sirdaryo"),
    ("Surxondaryo","Surxondaryo"),
    ("Xorazm","Xorazm"),
    ("Toshkent","Toshkent")
    
)
class Parent(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Nomi"),
                            help_text=_("Nomini kiriiting ..."))
    region = models.CharField(max_length=100,verbose_name=_("Region"), help_text=_("Viloyatni kiriting ..."),default="Qashqadaryo",choices=viloyat)
    address = models.CharField(max_length=100,verbose_name=_("Manzil"),help_text=_("Manzilni kiriting ..."))
    phone = models.CharField(max_length=100,verbose_name=_("Telefon raqam"),help_text=_("Telefon raqamni kiriting ..."))
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Ota ona"
        verbose_name = _("Ota ona ")
        verbose_name_plural = _("Ota onalar ")
    
class Student(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Ism sharif"),
                            help_text=_("Ism sharifni kiriting ..."))
    parent = models.ForeignKey(Parent,on_delete=models.CASCADE)
    address = models.CharField(max_length=100,verbose_name=_("Manzil"),help_text=_("Manzilni kiriting ..."))
    image = models.ImageField(upload_to="student-image",verbose_name=_("Image"),help_text=_("Rasm yuklang ..."))
    phone =  models.CharField(max_length=100,verbose_name=_("Telefon raqam"),help_text=_("Telefon raqam"))
    one_id = models.IntegerField(null=True,blank=True,unique=True)
    def __str__(self):
        return self.name
    @property
    def image_show(self):
        return format_html('<img src = {} width="60" height="60" style="border-radius:50%;"'.format(self.image.url))
    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        if self.id:
            self.one_id = self.id +1000
        super(Student, self).save(*args, **kwargs)
    class Meta:
        db_table = "O'quvchi"
        verbose_name = _("O'quvchi  ")
        verbose_name_plural = _("O'quvchilar ")