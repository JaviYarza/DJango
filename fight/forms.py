from django import forms

class CreateGato(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200)
    estilo = forms.MultipleChoiceField(label="Estilo de combate",widget=forms.CheckboxSelectMultiple,
                                          choices=(('Bonito', 'Bonito'),('Astuto', 'Astuto'),('Peligroso','Peligroso')))
    descr = forms.CharField(label="Descripción ", max_length=200)