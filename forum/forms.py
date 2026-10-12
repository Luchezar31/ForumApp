from crispy_forms.helper import FormHelper
from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forum.mixins import ReadOnlyMixin
from forum.models import PostBaseModel, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model=PostBaseModel
        fields='__all__'
        widgets={
            'language':forms.RadioSelect(
                attrs={
                    'class':'radio-select'
                }
            )
        }

    def clean(self):

        cleaned_data = super().clean()

        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('context')
        for word in content.split():
            if title.lower()==word.lower():
                raise ValidationError('The content must not contains title.')

        return cleaned_data


    




class PostCreateForm(PostBaseForm):

    class Meta(PostBaseForm.Meta):
        exclude = ('author','approved')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'

class PostEditForm(PostBaseForm):
    pass

class PostDeleteForm(ReadOnlyMixin ,PostBaseForm):
    pass


class SearchForm(forms.Form):
        query = forms.CharField(
            label='',
            required=False,
            max_length=100,
            widget=forms.TextInput(
                attrs={
                    'placeholder':'Search posts'
                }
            )
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('comment',)
        labels = {
            'comment':''
        }
        widgets = {
            'comment':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Add comment...'
                }
            )
        }

CommentFormSet = formset_factory(CommentForm, extra=1)