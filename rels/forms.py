from django import forms
from rels.models import RealState

class RelsForm(forms.ModelForm):
    class Meta:
        model=RealState
        fields="__all__"
        
        widgets={
            'Address':forms.TextInput(attrs={"class":"form-control"}),
            'price':forms.NumberInput(attrs={"class":"form-control"}),
            'property_type':forms.TextInput(attrs={"class":"form-control"}),
            'number_of_bedrooms':forms.NumberInput(attrs={"class":"form-control"}),
            'square_footage':forms.NumberInput(attrs={"class":"form-control"}),
            'location':forms.TextInput(attrs={"class":"form-control"}),
            'property_image':forms.FileInput(attrs={"class":"form-control"}),
            'contact_deatils':forms.TextInput(attrs={"class":"form-control"}),
           
        }    