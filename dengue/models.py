from django.db import models
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#1
class DengueArea(models.Model):
    daname=models.CharField(max_length=50)
    dadistrict = models.CharField(max_length=50) #choice field
    dadivision = models.CharField(max_length = 50) #choice field
    dalat = models.FloatField()
    dalon = models.FloatField()
    daalert = models.CharField(max_length = 100) #choice field
    dacreated_at= models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "denguearea"  
    def __str__(self):
        return self.daname
#2
class Medicals(models.Model):
    mname=models.CharField(max_length=500)
    maddress=models.CharField(max_length=500)
    mdistrict = models.CharField(max_length=50) #choice field
    mdivision = models.CharField(max_length = 50) #choice field
    mbed=models.IntegerField()
    mbedfullnot= models.CharField(max_length = 50) #choice field
    mfree= models.CharField(max_length = 50) #choice field
    mpublic= models.CharField(max_length = 50) #choice field
    mlat = models.FloatField()
    mlon = models.FloatField()    
    class Meta:  
        db_table = "medicals"  
    def __str__(self):
        return self.mname
#3
class News(models.Model):
    Newstitle=models.CharField(max_length=500)
    Newsdetails = RichTextUploadingField()
    Newsauthors = models.CharField(max_length=100)
    Newswhere = models.CharField(max_length=200)
    Newscreated_at= models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "news"  
    def __str__(self):
        return self.Newstitle