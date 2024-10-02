from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.list  import ListView
from django.views.generic.detail  import DetailView
from django.views.generic import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


#register
class UserRegister(FormView):
    template_name='base/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('task')

    def form_valid(self, form) -> HttpResponse:
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(UserRegister,self).form_valid(form)

    def get(self, request: HttpRequest, *args: str, **kwargs ) -> HttpResponse:
        
        if self.request.user.is_authenticated:
            return redirect('task')
        else:
            return super(UserRegister,self).get(*args,**kwargs)


#login
class UserLogin(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    
    def get_success_url(self) -> str:
        return reverse_lazy('task')


#logout
class UserLogout(LogoutView):
    template_name='base/logout.html'

    next_page=reverse_lazy('login')



class TaskList(LoginRequiredMixin,ListView):
    model=Task

    def get_context_data(self, **kwargs ):
        context=super().get_context_data(**kwargs)
        context['object_list']=context['object_list'].filter(user=self.request.user)
        context['count']=context['object_list'].filter(complete=False).count()
        

        search_input=self.request.GET.get('Search-area') or ''

        if search_input:
            context['object_list']=context['object_list'].filter(title__icontains=search_input)

        context['search_input']=search_input
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','complete','date_of_expiry']
    success_url=reverse_lazy('task')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete','date_of_expiry']
    success_url=reverse_lazy('task')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model= Task
    success_url=reverse_lazy('task')
