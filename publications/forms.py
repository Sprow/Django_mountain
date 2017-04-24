from django import forms

class PublicationForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())
    image = forms.FileField()


class PublicationCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea())
