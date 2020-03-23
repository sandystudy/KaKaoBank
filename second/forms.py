from django import forms

from .models import Kakaomap

class MapForm(forms.ModelForm):

    class Meta:
        model = Kakaomap
        fields = ('title', 'text', 'lat', 'long',)