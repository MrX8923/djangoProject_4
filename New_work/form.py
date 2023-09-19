from django import forms
from .models import Image


class OurForm(forms.Form):
    name = forms.CharField(
        label='Login',
    )
    num = forms.IntegerField(
        label='Pass',
        required=False,
        max_value=100,
        widget=forms.PasswordInput,
        initial=12,
    )


class PetForm(forms.Form):
    name = forms.CharField(
        label='Кличка',
        max_length=20
    )
    breed = forms.CharField(
        label='Порода',
        required=False,
        max_length=20
    )
    age = forms.IntegerField(
        label='Возраст',
        required=False,
    )
    color = forms.CharField(
        label='Окрас',
        required=False,
        max_length=20
    )
    food = forms.CharField(
        label='Корм',
        required=False,
        max_length=20
    )
    image = forms.ImageField(
        label='Фото',
        required=False,
    )


class ThirdForm(forms.Form):
    field_1 = forms.DecimalField(
        label='Decimal',
        decimal_places=2,
        required=False
    )
    field_2 = forms.EmailField(
        label='e-mail',
        required=False,
    )
    field_3 = forms.BooleanField(
        label='Choose',
        required=False,
    )
    field_4 = forms.CharField(
        widget=forms.Textarea(
            attrs={"cols": "5", "rows": "5"}
        ),
        required=False
    )
    field_5 = forms.NullBooleanField(
        label="Yes?",
        required=False
    )
    field_6 = forms.URLField(
        label='url',
        required=False,
        help_text='http://www.e1.ru'
    )
    field_7 = forms.FilePathField(
        label='File',
        path='C:\\Users\\TheEvil\\Desktop',
        allow_folders=True,
        required=False,
        match='.*\.txt'
    )
    field_8 = forms.ImageField(
        required=False,
    )
    field_9 = forms.FileField(
        required=False,
    )
    field_10 = forms.TypedChoiceField(
        required=False,
        choices=(
            (1, 'RU'),
            (2, 'EN'),
            (3, 'FR')
        )
    )
