from django.forms import ModelForm
from .models import Apply , Job 




class ApplyForm(ModelForm):
    class Meta:
        model = Apply 
        fields = ['name','email','website','cv','cover_letter']
        
        
        
class JobForm(ModelForm):
    class Meta:
        model = Job 
        fields = '__all__'
        exclude = ('owner','slug')
        