from .models import bharatanatyam,keyboard,guitar,kuchipudi,westerndance,music,video
from django import forms;


class galleryForm(forms.ModelForm):
    #no-separate fields are required(taken from model-Movies-class)
    class Meta:
        model=music,bharatanatyam,keyboard,guitar,kuchipudi,westerndance
        fields='__all__'
        labels={'image': ''}
class videoForm(forms.ModelForm):
    class Meta:
        model=video
        fields='__all__'