from django.conf import settings
from django import forms
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from homepage.State import State
from django_mako_plus.controller.router import get_renderer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission, ContentType
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from finance.settings import MEDIA_ROOT as media

templater = get_renderer('transaction')

######################################################
###  Shows the list of events
@view_function
def process_request(request):
  params = {}

  if request.user.is_authenticated():
    user = request.user
    user_id = user.id
  else:
    return HttpResponseRedirect('/homepage/login/')

  transaction = hmod.Transaction.objects.all().filter(User_id=user_id).order_by('-date')
  trans_count = transaction.count()

  paginator = Paginator(transaction, 5)
  page = request.GET.get('page')
  try:
    transaction = paginator.page(page)
  except PageNotAnInteger:
    transaction = paginator.page(1)
  except EmptyPage:
    transaction = paginator.page(paginator.num_pages)

  upper = paginator.num_pages + 1
  pages = range(1, upper)
  previous_page = transaction.number -1
  next_page = transaction.number + 1

  params = {'transaction': transaction,
            'trans_count': trans_count,
            'pages': pages,
            'previous_page': previous_page,
            'next_page': next_page,
           }
  return templater.render_to_response(request, 'transaction.html', params)

######################################################
### In-site spreadsheet
class SheetForm(forms.Form):
  date = forms.DateField(label='')
  description = forms.CharField(label='')
  original_description = forms.CharField(label='')
  amount = forms.DecimalField(label='', required=True, max_digits=12, decimal_places=2)
  transaction_type = forms.CharField(label='', required=True, max_length=100)
  category = forms.CharField(label='', required=True, max_length=100)
  account_name = forms.CharField(label='', required=True, max_length=100)

@view_function
def error(request):
  params = {}
  return templater.render_to_response(request, 'transaction.error.html', params)

@view_function
def create(request):
  t = hmod.Transaction.objects.all().order_by("-id")
  if len(t) > 0:
    if t[0].date == '':
      return HttpResponseRedirect('/transaction/transaction.edit/{}'.format(t.id))
  if request.user.is_authenticated():
    user_session = request.user
    userid = user_session.id
  else:
    return HttpResponseRedirect('/homepage/login/')

  trans = hmod.Transaction()
  trans.User_id = userid
  trans.date = None
  trans.description = ''
  trans.original_description = ''
  trans.amount = None
  trans.transaction_type = ''
  trans.category = ''
  trans.account_name = ''
  trans.save()

  return HttpResponseRedirect('/transaction/transaction.edit/{}'.format(trans.id))

@view_function
def edit(request):
  params = {}

  if request.user.is_authenticated():
    user_session = request.user
    user_id = user_session.id
  else:
    return HttpResponseRedirect('/homepage/login/') 
  try:
    trans = hmod.Transaction.objects.get(id=request.urlparams[0])
  except hmod.Transaction.DoesNotExist:
    return HttpResponseRedirect('/transaction/transaction/')

  form = TransEditForm(initial={
    'date': trans.date,
    'description': trans.description,
    'original_description': trans.original_description,
    'amount': trans.amount,
    'transaction_type': trans.transaction_type,
    'category': trans.category,
    'account_name': trans.account_name,
  }, user=request.user)
  if request.method == 'POST':
    form = TransEditForm(request.POST, user=request.user)
    # form.fields['aquery'].queryset = hmod.Account.objects.filter(user_id=request.user)
    if form.is_valid():
      amount = Decimal(form.cleaned_data['amount'])
      if form.cleaned_data['transaction_type']=='debit' and amount>0:
        print('if statement')
        amount = amount*-1
      try:
        acc = hmod.Account.objects.all().filter(user_id=user_id)
        acc2 = acc.get(account_name=form.cleaned_data['account_name'])
      except:
        acc = hmod.Account()
        acc.user_id = user_id
        acc.account_name = form.cleaned_data['account_name']
        acc.amount = 0.00
        acc.save()
        return HttpResponseRedirect('/transaction/transaction.delete_all/')

      if trans.amount != amount:
        acc2.amount+=amount
        acc2.save()
        print(acc2.amount)

      trans.date = form.cleaned_data['date']
      trans.description = form.cleaned_data['description']
      trans.original_description = form.cleaned_data['original_description']
      trans.amount = amount
      trans.transaction_type = form.cleaned_data['transaction_type']
      trans.category = form.cleaned_data['category']
      trans.account_name = form.cleaned_data['account_name']
      trans.save()

      return HttpResponseRedirect('/transaction/transaction/')  

  params['form'] = form
  params['trans'] = trans
  return templater.render_to_response(request, 'transaction.edit.html', params)

@view_function
def delete(request):
  try:
    trans = hmod.Transaction.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/transaction/transaction/')
  trans.delete()
  return HttpResponseRedirect('/transaction/transaction/')

@view_function
def delete_all(request):
  if request.user.is_authenticated():
    user_session = request.user
    userid = user_session.id
  else:
    return HttpResponseRedirect('/homepage/login/')
  try:
    trans = hmod.Transaction.objects.all().filter(User_id=userid)
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/transaction/transaction/')
  for tran in trans:
    tran.delete()
  return HttpResponseRedirect('/transaction/transaction/')

@view_function
def upload(request):
  params = {}
  if request.user.is_authenticated():
    user_session = request.user
    userid = user_session.id  
  if request.method == 'POST':
    form = UploadFile(request.POST, request.FILES)
    if form.is_valid():
      files = hmod.StockUpload.objects.all().filter(user=request.user)
      if files.count() > 0:
        for f in files:
          f.delete()
      trans = form.save(commit=False)
      trans.user = request.user
      trans.filepath = media
      trans.save()
      handle_uploaded_file(userid)
      return HttpResponseRedirect('/transaction/transaction/') 
  else:
    form = UploadFile()

  params['form'] = form
  return templater.render_to_response(request, 'transaction.upload.html', params)

def handle_uploaded_file(userid):
  try:
    t_file = hmod.StockUpload.objects.all().get(user=userid)
  except:
    return HttpResponseRedirect('/transaction/transaction/')
  fp = 'media' + str(t_file.transaction)[1:]
  import csv
  filepath = fp
  dataReader = csv.reader(open(filepath), delimiter=',', quotechar='"')

  for row in dataReader:
    if row[0] != 'Date': # Ignore the header row, import everything else
      amount = Decimal(row[3])
      date = row[0]
      date = datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y-%m-%d")
      if row[4] == 'debit':
        amount = amount*-1
      
      acc = hmod.Account.objects.all().filter(user_id=userid)
      try:
        acc2 = hmod.Account.objects.get(account_name=row[6])
      except:
        acc = hmod.Account()
        acc.user_id = userid
        acc.account_name = row[6]
        acc.amount = 0.00
        acc.acc_type = 'Other'
        acc.save()

      acc2 = hmod.Account.objects.get(account_name=row[6])
      
      transaction = hmod.Transaction()
      transaction.User_id = userid
      transaction.date = date
      transaction.description = row[1]
      transaction.original_description = row[2]
      transaction.amount = amount
      transaction.transaction_type = row[4]
      transaction.category = row[5]
      transaction.account_id = acc2.id
      transaction.account_name = row[6]
      transaction.save()

      acc2.amount += amount
      acc2.save()

  trans_count = hmod.Transaction.objects.all().count()
  if trans_count < 1:
    return HttpResponseRedirect('/transaction/transaction.error/')
  
class UploadFile(forms.ModelForm):
  class Meta:
    model = hmod.StockUpload
    fields = ('transaction',)
    
class TransEditForm(forms.Form):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    request = kwargs.pop('request', None)
    super(TransEditForm, self).__init__(*args, **kwargs)

    if user==None:
      user = kwargs.pop('user')
    # Obtain items for user
    if user is not None:
      aquery = hmod.Account.objects.all().filter(user_id=user.id).values_list('account_name', flat=True).order_by('account_name').distinct('account_name')
      aquery_choices = [('', 'None')] + [(id, id) for id in aquery]

      self.fields['account_name'].choices = aquery_choices

  iquery = hmod.Transaction.objects.values_list('category', flat=True).order_by('category').distinct('category')
  iquery_choices = [('', 'None')] + [(id, id) for id in iquery]

  date = forms.DateField(required=True, widget=forms.TextInput(attrs={'class':'datepicker'}))
  description = forms.CharField(required=True)
  original_description = forms.CharField(label="Original Description", required=True)
  amount = forms.DecimalField(required=True, max_digits=12, decimal_places=2)
  type_choices = (
      ('debit', 'debit'),
      ('credit', 'credit'),
    )
  transaction_type = forms.ChoiceField(label="Transaction Type", required=True, choices=type_choices)
  category = forms.ChoiceField(choices=iquery_choices, required=True)  
  account_name = forms.ChoiceField(label="Account Name", required=True)
  
