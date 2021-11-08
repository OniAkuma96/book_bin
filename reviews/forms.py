from django import forms
from .models import Review


class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['comment'].widget.attrs['autofocus'] = True
