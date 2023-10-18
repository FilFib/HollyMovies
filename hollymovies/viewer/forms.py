import re
from xml.dom import ValidationErr
from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, ModelForm
)
from viewer.utils import PastMonthField, capitalized_validator

from viewer.models import Genre, Movie


class MovieForm(ModelForm):
   
  class Meta:
    model = Movie
    fields = '__all__'

  title = CharField(validators=[capitalized_validator])
  rating = IntegerField(min_value=1, max_value=10)
  released = PastMonthField()
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control'

  def clean_description(self):
    # Force each sentence of the description to be capitalized.
    initial = self.cleaned_data['description']
    sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
    cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
    self.cleaned_data['description'] = cleaned

  def clean(self):
    result = super().clean()
    if result['genre'].name == 'commedy' and result['rating'] > 5:
      raise ValidationErr(
        "Commedies aren't so good to be rated over 5."
      )
    return result
  

# class MovieForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'