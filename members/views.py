from django.shortcuts import render,get_object_or_404
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpFrom,EditProfileFrom,ProfilePageForm,EditProfileInfoForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView,CreateView
from myeblog.models import Profile
# Create your views here.


class EditProfilePageView(generic.UpdateView):
   model = Profile
   template_name = 'registration/edit_user_profile.html'
   form_class = EditProfileInfoForm
   #fields= ['bio','profile_pic','website_url','whatsapp_url','insta_url','facebook_url','twitter_url']
   success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name  = 'registration/user_profile.html'

    def get_context_data(self,*args,**kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)

        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

class PasswordsChangeView(PasswordChangeView):
       form_class = PasswordChangeForm
       success_url = reverse_lazy('successfull_password_change')

def SuccessfulPasswordChangeView(request):
     return render(request,'registration/successful_password_change.html')

class UserRegisterView(generic.CreateView):
    form_class = SignUpFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileFrom
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
     

    def get_object(self):
        return self.request.user 

class  CreateProfileView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html' 

    #fields = '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)       