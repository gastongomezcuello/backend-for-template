from django import forms

from coins.models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"
        exclude = ["user", "balance"]
