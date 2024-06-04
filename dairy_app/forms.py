from django import forms

from . models import AnimalSelection
from . models import Contact
#build your forms here

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}))
    message= forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control','rows': 10}))

class AnimalSelectionForm(forms.Form):
    BREED_CHOICE = (
        ('brahman', 'Brahman'),
        ('hereford', 'Hereford'),
        ('scottish highland', 'Scottish Highland'),
        ('holstein', 'Holstein'),
        ('dexter', 'Dexter')
    )
    ANIMAL_GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    animal_id = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Unique identifier for the animal'}))
    breed = forms.CharField(widget=forms.Select(attrs={'placeholder': 'select animal breed'}, choices=BREED_CHOICE))
    animal_age = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Enter the animal age'}))
    gender = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Select the animal gender'}, choices=ANIMAL_GENDER))
    health_condition = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type any disease the animal has had', 'rows': 7}))