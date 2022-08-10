from django import forms

from books.models import Review


class ReviewForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Review
        fields = ['content', 'image']
        labels = {'content': 'Your review'}
        widgets = {'content': forms.Textarea(attrs={'class': 'border rounded p-2 w-full',
                                                    'placeholder': 'Write your review here',
                                                    'rows': 6})}

