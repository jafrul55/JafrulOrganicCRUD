from django import forms
from .models import OrganicStoreModel
class OrganicStoreForm(forms.ModelForm):
    class Meta:
        model = OrganicStoreModel
        fields = ['product_name','farmer_name','category']
        
        
