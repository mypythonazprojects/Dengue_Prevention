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