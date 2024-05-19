from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Kategor(models.Model):
    name=models.TextField()
    img=models.ImageField()
    def get_absolute_url(self):
        return f'/katalog/{self.id}'
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Категория"
        verbose_name = "Категории"

    def __str__(self):
        return self.name
class Stat(models.Model):
    name=models.TextField()
    kategor=models.ForeignKey(Kategor,on_delete=models.RESTRICT)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Характеристика"
        verbose_name = "Характеристики"

    def __str__(self):
        return self.name
class Company(models.Model):
    name_company=models.TextField()
    def __str__(self):
        return self.name_company
    class Meta:
        verbose_name_plural = "Компания"
        verbose_name = "Компании"

    def __str__(self):
        return self.name_company
class Pod_kat(models.Model):
    name=models.TextField()
    stat=models.ManyToManyField(Stat)
    kateg=models.ForeignKey(Kategor,on_delete=models.RESTRICT)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Под категории"
        verbose_name = "Под категории"

    def __str__(self):
        return self.name
class Imgtovar(models.Model):
    img=models.ImageField(null=True)
class New(models.Model):
    text=models.TextField()
    img=models.ImageField(null=True)
    data=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новости"

    def __str__(self):
        return self.data
class Tovar(models.Model):
    name=models.TextField()
    comp=models.ForeignKey(Company,on_delete=models.RESTRICT)
    price=models.IntegerField()
    keteg=models.ForeignKey(Kategor,on_delete=models.RESTRICT)
    stat=models.ManyToManyField(Stat)
    img=models.ImageField(null=True)
    pod_kat=models.ManyToManyField(Pod_kat)

    class Meta:
        verbose_name_plural = "Товар"
        verbose_name = "Товары"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/katalog-inform-tovar/{self.id}/'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='profil',default='profil/default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name_plural = "Профиль"
        verbose_name = "Профили"

    def __str__(self):
        return self.user

class Koment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    rating=models.TextField()
    parent=models.ForeignKey(
        'self',on_delete=models.SET_NULL,blank=True,null=True,related_name='+'
    )
    tov=models.ForeignKey(Tovar,on_delete=models.CASCADE,related_name='reviews')

    class Meta:
        verbose_name_plural = "Комментарий"
        verbose_name = "Комментарий"

    def __str__(self):
        return self.user.username

class Submodal(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message=models.TextField()

    class Meta:
        verbose_name_plural = "Поддержка"
        verbose_name = "Поддержка"

    def __str__(self):
        return self.name
