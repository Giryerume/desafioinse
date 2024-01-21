from django import forms

class PlanilhaForm(forms.Form):
    planilha = forms.FileField()

