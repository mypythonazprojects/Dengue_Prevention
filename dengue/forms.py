from django import forms  
from django.contrib.admin import widgets
from django.forms.widgets import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime
from dengue.models import *
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DengueAreaForm(forms.ModelForm):
    division = (
        ('Barishal', 'Barishal',),('Chittagong', 'Chittagong',),('Dhaka', 'Dhaka',),('Khulna', 'Khulna',),('Mymensingh', 'Mymensingh',),('Rajshahi', 'Rajshahi',),('Rangpur', 'Rangpur',),('Sylhet', 'Sylhet',),
    )
    district = (
        ('Barishal', 'Barishal',),('Chittagong', 'Chittagong',),('Dhaka', 'Dhaka',),('Khulna', 'Khulna',),('Mymensingh', 'Mymensingh',),('Rajshahi', 'Rajshahi',),('Rangpur', 'Rangpur',),('Sylhet', 'Sylhet',),
    )
    alert = (
        ('Dangerous', 'Dangerous',),('Very Dangerous', 'Very Dangerous',),('Safe', 'Safe',),
    )
    daname=  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'inlineFormInputGroup', 'placeholder':'sylhet,sadar,jalalbad.'}),required=True,max_length=400)    
    dadistrict= forms.CharField(widget=forms.Select(attrs={'class':'sel5','name':'state'}, choices=district))
    dadivision = forms.CharField(widget=forms.Select(attrs={'class':'sel6'}, choices=division))
    dalat=  forms.FloatField(min_value=0,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'00.000'}),required=True) 
    dalon=  forms.FloatField(min_value=0,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'00.000'}),required=True)    
    daalert=  forms.CharField(widget=forms.Select(attrs={'class':'sel7'}, choices=alert))    
    class Meta:  
        model = DengueArea  
        fields = "__all__"



#class HeaderColor(forms.ModelForm):
#    hcolor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'book shelf', 'value':'A-00 (Room-300)'}),required=True,max_length=400)
#    class Meta:  
#        model = BooksShelf  
#        fields = "__all__"



#proble solved
'''


I had the same problem, my solution now is to use the ChoiceField instead of the ModelChoiceField. I believe this makes sense, since we do not want the user to select model instances, but distinct attribute values throughout one table column and the same attribute might well correspond to several model instances.

class SearchForm(forms.Form):
    # get the distinct attributes from one column
    entries = Locality.objects.values_list('islandgroup', flat=True).distinct('islandgroup')
    # change the entries to a valid format for choice field
    locality_choices = [(e, e) for e in entries]
    # the actual choice field
    island_group = forms.ChoiceField(
        required=False,
        choices=locality_choices)

This way Django's inbuilt validation performs exactly what we want, i.e. checking whether a member of the set of all possible attributes from one column was selected.

'''