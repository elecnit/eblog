from django.contrib.auth.forms  import UserCreationForm,UserChangeForm,PasswordChangeForm

from django.contrib.auth.models import User
from django import forms
from myeblog.models import Profile


#class UserPasswordChangeForm(PasswordChangeForm):
 #   class Meta:
  #      fields = ('old Password')

class EditProfileInfoForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','website_url','whatsapp_url','facebook_url','insta_url','twitter_url')
  
        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control1'}),
            #'profile_pic':forms.TextInput(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'whatsapp_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'insta_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
            
        }   

class ProfilePageForm(forms.ModelForm):
   class Meta: 
     model = Profile
     fields = ('bio','profile_pic','website_url','whatsapp_url','facebook_url','insta_url','twitter_url')
    
     widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            #'profile_pic':forms.TextInput(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'whatsapp_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'insta_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
            
        }   
    
 
#widget=forms.EmailField(attrs={'class':'form-control'},,widget= forms.TextInput(attrs={'class':'form-control'}
class SignUpFrom(UserCreationForm):
        email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
        first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
        last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
  
   
        class Meta:
          model = User
          fields = ('username','first_name','last_name','email','password1','password2')
       
      
            
     
        def __init__(self,*args,**kwargs):
           super(SignUpFrom, self).__init__(*args, **kwargs)    
           self.fields['username'].widget.attrs['class'] = 'form-control'
           self.fields['password1'].widget.attrs['class'] = 'form-control'#,widget=forms.CheckboxInput(attrs={'class':'form-check'})
           self.fields['password2'].widget.attrs['class'] = 'form-control'#,widget=forms.TextInput(attrs={'class':'form-control'})
         


class EditProfileFrom(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
   # date_joined = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password','last_login')       


        