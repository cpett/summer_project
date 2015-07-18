from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from datetime import datetime
from django import forms
from .. import dmp_render, dmp_render_to_response
import homepage.models as hmod
from homepage.State import State
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

# @view_function
# def process_request(request):
#   return HttpResponseRedirect('/homepage/index/')


######################################################
###  Edit a user
@view_function
def edit(request):
  params = {}

  try:
    user = hmod.Users.objects.get(id=request.urlparams[0])
  except hmod.Users.DoesNotExist:
    return HttpResponseRedirect('/homepage/index/')

  form = SignupForm(initial={
    'username': user.username,
    'password': user.password,
    # 'security_question': user.security_question,
    'email': user.email,
    'first_name': user.first_name,
    'last_name': user.last_name,
    'address1': user.address1,
    'address2': user.address2,
    'city': user.city,
    'state': user.state,
    'country': user.country,
    'zip': user.zip,
    'group': user.groups.all(),
  })
  if request.method == 'POST':
    form = SignupForm(request.POST)
    form.userid = user.id
    if form.is_valid():
      print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
      user.username = form.cleaned_data['username']
      user.set_password(form.cleaned_data['password'])
      user.email = form.cleaned_data['email']
      # user.security_question = form.cleaned_data['security_question']
      user.first_name = form.cleaned_data['first_name']
      user.last_name = form.cleaned_data['last_name']
      user.address1 = form.cleaned_data['address1']
      user.address2 = form.cleaned_data['address2']
      user.city = form.cleaned_data['city']
      user.state = form.cleaned_data['state']
      user.zip = form.cleaned_data['zip']
      user.country = form.cleaned_data['country']

      try:
        group = Group.objects.get(name='Guest')
      except Group.DoesNotExist:
        return HttpResponseRedirect('/homepage/index/')
      group.user_set.add(user)

      user.save()
      return HttpResponseRedirect('/homepage/index/')      

  params['form'] = form
  params['user'] = user

  return templater.render_to_response(request, 'signup.edit.html', params)
######################################################
###  Creates a new user
@view_function
def create(request):
  # params = {}
  u = hmod.Users.objects.all().order_by("-id")[0]
  if u.username == '':
    return HttpResponseRedirect('/homepage/signup.edit/{}'.format(u.id))

  user = hmod.Users()
  user.username = ''
  user.password = ''
  user.security_question = ''
  user.first_name = ''
  user.last_name = ''
  user.address1 = ''
  user.address2 = ''
  user.city = ''
  user.state = ''
  user.zip = ''
  user.country = ''
  user.save()

  return HttpResponseRedirect('/homepage/signup.edit/{}'.format(user.id))

@view_function
def signup(request):
  template_vars = {}
  form = SignupForm()
  if request.method == 'POST':
    form = SignupForm(request.POST)
    form.userid = user.id
    if form.is_valid():
      username = form.cleaned_data['username']
      set_password(form.cleaned_data['password'])
      email = form.cleaned_data['email']
      # user.security_question = form.cleaned_data['security_question']
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      address1 = form.cleaned_data['address1']
      address2 = form.cleaned_data['address2']
      city = form.cleaned_data['city']
      state = form.cleaned_data['state']
      zip = form.cleaned_data['zip']
      country = form.cleaned_data['country']
      return HttpResponseRedirect('/homepage/index/')

  template_vars['form'] = form

  return dmp_render_to_response(request, 'signup.html', template_vars)

class SignupForm(forms.Form):
  username = forms.CharField(label='Username')
  password = forms.CharField(label='Password', widget=forms.PasswordInput)
  email = forms.CharField(label='Email')
  # security_question = forms.CharField(label='First Name', required=True, max_length=100)
  first_name = forms.CharField(label='First Name', required=True, max_length=100)
  last_name = forms.CharField(label='Last Name', required=True, max_length=100)
  address1 = forms.CharField(label='Address 1', required=True, max_length=100)
  address2 = forms.CharField(label='Address 2', required=False, max_length=100)
  city = forms.CharField(label='City', required=True, max_length=50)
  state = forms.ChoiceField(State.STATE_CHOICES)
  country = forms.CharField(label='Country', required=True, max_length=50)
  zip = forms.CharField(label='ZIP', required=True, max_length=5)
  #userid from form.userid = user.id

######################################################
###  Deletes a new user
@view_function
def delete(request):
  try:
    user = hmod.Users.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/homepage/index/')
  user.delete()
  return HttpResponseRedirect('/homepage/index/')

@view_function
def check_username(request):
  username = request.REQUEST.get('u')

  user_count = hmod.Users.objects.filter(username=username).count()
            #.exclude(id=self.userid).count() #self aka (this) calls form.userid because this section of the area is IN the form
  if user_count >= 1:
    # bad (already exists)
    return HttpResponse("0")
  # good (doesn't exist)
  return HttpResponse("1")
    # user_count = hmod.Users.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count() #self aka (this) calls form.userid because this section of the area is IN the form
    # if user_count >= 1:
    #   raise forms.ValidationError("This username is not available.  Please select another username.")
    # return self.cleaned_data['username']
  

 

#  @view_function
# def check_creds(request):
#   username = request.REQUEST.get('u')
#   password = request.REQUEST.get('p')

#   #check the username
#     #okay if current user
#   user_count = hmod.Users.objects.filter(username=username).count()
#           #.exclude(id=self.userid).count() #self aka (this) calls form.userid because this section of the area is IN the form
#   if user_count >= 1:
#     # bad (already exists)
#     return HttpResponse("0")
#   # good (doesn't exist)
#   return HttpResponse("1")