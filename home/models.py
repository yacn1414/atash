from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class SiteInformation(models.Model):
    siteNamePersian = models.CharField("اسم سایت به فارسی",max_length=20)
    logo = models.ImageField("لوگو سایت",upload_to='images/logo')
    siteNameEnglish = models.CharField("اسم سایت انگلیسی",max_length=20)
    telegram = models.CharField("تلگرام",max_length=15)
    phone = models.CharField("شماره",max_length=11)
    email = models.CharField("ایمیل",max_length=20)
    class Meta:
        verbose_name = 'اطلاعات سایت'
        verbose_name_plural = 'اطلاعات سایت'
    def _str__(self):
        return self.siteNameEnglish
class Categories(models.Model):
    title = models.CharField(max_length=20,verbose_name="اسم دسته بندی")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    def __str__(self):
        return self.title
    
class Posts(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    image = models.ImageField(upload_to="post/")
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Categories = models.ManyToManyField(Categories)
    status = models.BooleanField(default=False)
    hot = models.BooleanField(default=False)
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
    def __str__(self):
        return self.title
