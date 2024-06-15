from django import forms
from .models import Films, Seances, Books, Subscribers, Sended_to_Subscribers

class SeancesForm(forms.ModelForm):
    class Meta:
        model = Seances
        fields = '__all__'

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'

class Sended_to_SubscribersForm(forms.ModelForm):
    class Meta:
        model = Sended_to_Subscribers
        fields = '__all__'