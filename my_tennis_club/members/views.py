from django.http import HttpResponse
from django.template import loader
from .models import Member, RegisterForm
from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View




def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
      template = loader.get_template('main.html')
      return HttpResponse(template.render())

def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def ranking(request):
  mymembers = Member.objects.all().order_by('ranking_system').values()  
  template = loader.get_template('ranking.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
    
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
def login_page(request):
  mymembers = Member.objects.all().values() 
  template = loader.get_template('login.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
    







  
  


