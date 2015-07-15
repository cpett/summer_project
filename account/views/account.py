from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal

templater = get_renderer('account')


@view_function
def process_request(request):
  params = {}

  if request.user.is_authenticated():
    user_session = request.user
    userid = user_session.id
  else:
    return HttpResponseRedirect('/homepage/login/')

  checking = hmod.Account.objects.all().filter(user_id=userid, acc_type='Checking').order_by('account_name')
  credit_card = hmod.Account.objects.all().filter(user_id=userid, acc_type='Credit Card').order_by('account_name')
  investments = hmod.Account.objects.all().filter(user_id=userid, acc_type='Investments').order_by('account_name')
  loans = hmod.Account.objects.all().filter(user_id=userid, acc_type='loans').order_by('account_name')
  other = hmod.Account.objects.all().filter(user_id=userid, acc_type='Other').order_by('account_name')
  savings = hmod.Account.objects.all().filter(user_id=userid, acc_type='Savings').order_by('account_name')

  icheck = 0
  icredit = 0
  iinv = 0
  iloan = 0
  iothers = 0
  isaving = 0

  for check in checking:
    i = Decimal(check.amount)
    icheck += i
  print(icheck)

  for credit in credit_card:
    i = Decimal(credit.amount)
    icredit += i
  print(icredit)

  for inv in investments:
    i = Decimal(inv.amount)
    iinv += i

  for loan in loans:
    i = Decimal(loan.amount)
    iloan += i

  for others in other:
    i = Decimal(others.amount)
    iothers += i

  for saving in savings:
    i = Decimal(saving.amount)
    isaving += i

  iCash = icheck + isaving
  iDebt = icredit + iloan
  iLongT = iinv + iothers
  
  params['iCash'] = iCash
  params['iDebt'] = iDebt
  params['iLongT'] = iLongT

  params['checking'] = checking
  params['credit_card'] = credit_card
  params['investments'] = investments
  params['loans'] = loans
  params['other'] = other
  params['savings'] = savings

  return templater.render_to_response(request, 'account.html', params)

######################################################
###  Edit a account
@view_function
def edit(request):
  params = {}

  if request.user.is_authenticated():
    user_session = request.user
    user_id = user_session.id
  else:
    return HttpResponseRedirect('/homepage/login/')

  try:
    account = hmod.Account.objects.get(id=request.urlparams[0])
  except hmod.Account.DoesNotExist:
    return HttpResponseRedirect('/account/account/')

  form = AccountEditForm(initial={
    'account_name': account.account_name,
    'amount': account.amount,
    'acc_type': account.acc_type,
  })
  if request.method == 'POST':
    form = AccountEditForm(request.POST)
    if form.is_valid():
      account.account_name = form.cleaned_data['account_name']
      account.amount = (form.cleaned_data['amount'])
      account.acc_type = form.cleaned_data['acc_type']
      account.save()
      return HttpResponseRedirect('/account/account/')      

  params['form'] = form
  params['account'] = account

  return templater.render_to_response(request, 'account.edit.html', params)

class AccountEditForm(forms.Form):
  account_name = forms.CharField(label='Account Name')
  amount = forms.CharField(required=True)
  choices = (
    ('Checking', 'Checking'),
    ('Credit Card', 'Credit Card'),
    ('Investments', 'Investments'),
    ('Loans', 'Loans'),
    ('Other', 'Other'),
    ('Savings', 'Savings'),
    )
  acc_type = forms.ChoiceField(choices=choices, required=True, label='Account Type')
  #validation rules; i.e., not too huge a number

######################################################
###  Creates a new account
@view_function
def create(request):
  # params = {}
  if request.user.is_authenticated():
    user_session = request.user
    userid = user_session.id
  else:
    return HttpResponseRedirect('/homepage/login/')

  a1 = hmod.Account.objects.all().count()
  if a1 > 0:
	  a = hmod.Account.objects.all().order_by("-id")[0]
	  if a.account_name == '':
	    return HttpResponseRedirect('/account/account.edit/{}'.format(a.id))	

  account = hmod.Account()
  account.account_name = ''
  account.amount = None
  account.user_id = request.user.id
  account.acc_type = ''
  account.save()

  return HttpResponseRedirect('/account/account.edit/{}'.format(account.id))

######################################################
###  Deletes a new account
@view_function
def delete(request):
  try:
    account = hmod.Account.objects.get(id=request.urlparams[0])
  except hmod.DoesNotExist:
    return HttpResponseRedirect('/account/account/')
  account.delete()
  return HttpResponseRedirect('/account/account/')