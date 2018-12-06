from django.forms import Form, fields
from django import forms


class SneakerForm(Form):
    title = fields.CharField(max_length=100)
    content = fields.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows': 15, 'cols': 100}))
    pic = fields.ImageField()
    sneakerReleaseDate = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class': 'datepicker'
                                }))
    color = fields.CharField(max_length=100)
    price = fields.IntegerField()

    store = fields.CharField(max_length=100)
    storepic = fields.ImageField()
    url = fields.URLField(max_length=100)

    reseller = fields.CharField(max_length=100)
    resellerlink = fields.URLField(max_length=100)


