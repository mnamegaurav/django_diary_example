from django.forms import ModelForm
from .models import Notes

class TextForm(ModelForm):
    class Meta:
        model = Notes
        fields = ('text',)

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['text']