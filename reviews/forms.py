from django import forms
from .models import Review


class NewReviewForm(forms.ModelForm):
    rating = forms.CharField(label='Rating', widget=forms.TextInput(attrs={'min': 1,'max': '5', 'type': 'number'}))

    class Meta:
        model = Review
        fields = ('comment', 'rating',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['comment'].widget.attrs['autofocus'] = True
            self.fields['rating'].widget.attrs['max'] = 5
