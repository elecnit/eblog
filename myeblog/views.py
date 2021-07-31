from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from django.urls import reverse_lazy,reverse
from .forms import PostForm,EditForm
from django.http  import HttpResponseRedirect
# Create your views here.
#def home(request):
 #   return render(request, 'home.html')


def LikeView(request , pk):
  post = get_object_or_404(Post,id=request.POST.get('post_id'))
  liked = False
  if post.likes.filter(id = request.user.id).exists():
    post.likes.remove(request.user)
    liked = False
  else:
    post.likes.add(request.user)
    liked = True  
  return HttpResponseRedirect(reverse('detail_view',args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class Post_Detail_view(DetailView):
    model = Post 
    template_name = 'detail.html'   
    def get_context_data(self,*args,**kwargs):
        context = super( Post_Detail_view,self).get_context_data()
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
       
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
          liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class Add_Post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = ['title','author','body',]   
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)       

class Add_Category_Post(CreateView):
    model = Category
    #form_class = PostForm
    fields = '__all__'
    template_name = 'add_category_post.html'

def CategoryView(request,cats):
    cats1 = Category.objects.get(name=cats.replace('-',' '))
    print(cats1)
    category_post = Post.objects.filter(category=cats1.id)
    return render(request, 'categories.html',{"cats":cats.title().replace('-',' '),"category_post":category_post})


class UpdatePostview(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
   # fields = ['title','body']    
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'    
    success_url = reverse_lazy('home')


