from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, Max, Min, Avg, Sum, F
import datetime
from datetime import timedelta, date

templater = get_renderer('dashboard')


@view_function
def process_request(request):
  params = {}

  if request.user.is_authenticated():
    user_session = request.user
    userid = user_session.id
  else:
    return HttpResponseRedirect('/homepage/login/')

  acc_id = hmod.Account.objects.all().filter(user_id=userid, acc_type="Credit Card").values_list('id')

  account = hmod.Account.objects.all().filter(user_id=userid).values_list('account_name', 'amount').order_by('-amount')
  types = hmod.Account.objects.all().filter(user_id=userid).values_list('account_name', 'amount', 'acc_type').order_by('-amount')
  trans = hmod.Transaction.objects.all().exclude(account_id=acc_id).filter(User_id=userid).values_list('date', 'transaction_type', 'amount', 'category', 'account_name').order_by('date')

  date = hmod.Transaction.objects.distinct('date').order_by('date')

  for d in date:
    start_date = d.date
    break
  for d in date:
    end_date = d.date

  d = start_date
  delta = datetime.timedelta(days=1)

  hmod.DebCred.objects.all().delete()

  while d <= end_date:
    for tran in trans:
      if tran[0] == d: #if trans_date == date crawl go on
        time = tran[0]
        t = time.strftime('%Y-%m-%d')
        y = time.strftime('%Y')
        m = time.strftime('%m')
        if tran[1] == "credit": #if trans_type == credit go on
          i = hmod.DebCred.objects.all().filter(year = y, month = m, tran_type='credit').count()
          if i == 1:
            cred = hmod.DebCred.objects.get(year = y, month = m, tran_type='credit')
            cred.cost += tran[2]
            cred.save()
          else:
            cred = hmod.DebCred()
            cred.date = t
            cred.year = y
            cred.month = m
            cred.cost = tran[2]
            cred.tran_type = 'credit'
            cred.save()
        else:
          i = hmod.DebCred.objects.all().filter(year = y, month = m, tran_type='debit').count()
          if i == 1:
            deb = hmod.DebCred.objects.get(year = y, month = m, tran_type='debit')
            deb.cost += tran[2] * -1
            deb.save()
          else:
            deb = hmod.DebCred()
            deb.date = t
            deb.year = y
            deb.month = m
            deb.cost = tran[2] * -1
            deb.tran_type = 'debit'
            deb.save()
    d += delta

  debcred = hmod.DebCred.objects.all().values_list('date', 'cost', 'tran_type', 'year', 'month').order_by('date')

  dc_json = json.dumps(list(debcred), cls=DjangoJSONEncoder)
  params['dc_json'] = dc_json

  acc_json = json.dumps(list(account), cls=DjangoJSONEncoder)
  types_json = json.dumps(list(types), cls=DjangoJSONEncoder)
  trans_json = json.dumps(list(trans), cls=DjangoJSONEncoder)

  params['acc_json'] = acc_json
  params['types_json'] = types_json
  params['trans_json'] = trans_json
  params['account'] = account

  return templater.render_to_response(request, 'dashboard.html', params)
