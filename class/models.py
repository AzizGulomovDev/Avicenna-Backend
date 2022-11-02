from django.db import models
from django.utils.translation import gettext_lazy as _
from students.models import Student
# Create your models here.
class Tuitor(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Ism sharif"),
                            help_text=_("Ism sharifini kiriting ..."))
    phone = models.CharField(max_length=100,verbose_name=_("Telefon raqami"),help_text=_("Telefon raqamini kiriting ..."))
    about = models.TextField(verbose_name=_("O'qutuvchi haqida"),help_text=_("O'qituvchi haqida ma'lumot"))
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Tuitor"
        verbose_name= _("Tuitor ")
        verbose_name_plural = _("Tuitorlar ")
class ClassRoom(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Sinf nomi"),help_text=_("Sinf nomini kiriting ..."))
    student = models.ManyToManyField(Student)
    tuitor = models.ForeignKey(Tuitor,on_delete=models.CASCADE)
    lesson_time = models.TextField(verbose_name=_("Dars vaqti"),help_text=_("Dars vaqtini kiriting"))
    def __str__(self):
        return f"{self.name} sinfi"
    class Meta:
        db_table = 'Sinfxona'
        verbose_name= _("Sinfxona ")
        verbose_name_plural = _("Sinfxonalar ")
from students.models import Student
# Create your models here.
class Davomat(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,to_field='one_id')
    date = models.DateField()
    bool = models.BooleanField(default=False)
    sinf = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.sinf.name} - {self.student.name}"
    class Meta:
        db_table = "Davomat "
        verbose_name = _("Davomat")
        verbose_name_plural = _("Davomatlar")