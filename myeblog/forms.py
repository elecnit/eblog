from django import forms
from .models import Post,Category

cats= Category.objects.all().values_list('name','name')




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','body','snippet','header_image')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            #'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            'category':forms.Select(choices=cats,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control1'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
            
        }   

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','snippet')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            
            'body':forms.Textarea(attrs={'class':'form-control1'}),

            'snippet':forms.Textarea(attrs={'class':'form-control'}),
        }   

