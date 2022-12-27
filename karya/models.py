from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Kategori"


class Artikel(models.Model):
    nama = models.CharField(max_length=100,blank=True,null=True)
    deskripsi = models.CharField(max_length=100,blank=True,null=True)
    pencipta = models.CharField(max_length=100,blank=True,null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    harga = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return "{} - {}".format(self.nama, self.deskripsi)
    
    class Meta:
        verbose_name_plural = "Artikel"
    