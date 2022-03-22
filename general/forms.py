from django import forms

class Appeal(forms.Form):
    name = forms.CharField(label="Ваши ФИО", max_length=50)
    e_mail = forms.EmailField(label="Ваш E-mail", max_length=30)
    filial = forms.CharField(label='Филиал ПАО "Ростелеком"', max_length=20)
    message = forms.CharField(label="Ваше обращение", widget=forms.Textarea)
    required_css_class = "form1"
