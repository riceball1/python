from django import forms

from .models import Notes

# this can be used instead of passing fields in the views.py, can instead pass this form_class
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

        # clean up the layout of the form with widgets
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-5'})
        }

        labels = {
            'text': 'Write your thoughts here: '
        }

    
    # can add validation
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise forms.ValidationError('we only accept notes about Django!')
    #     return title