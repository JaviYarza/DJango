from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
    text = forms.CharField(label="Text", max_length=200)
    
class BuscaLista(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    