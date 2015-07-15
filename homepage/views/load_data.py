# Full path and name to your csv file
csv_filepathname="C:/Python34/Lib/site-packages/django/bin/finance/transaction/views/transactions.csv"
# Full path to your django project directory
your_djangoproject_home="C:/Python34/Lib/site-packages/django/bin/finance"
homepage = "C:/Python34/Lib/site-packages/django/bin/finance/homepage"

import sys,os
sys.path.append(your_djangoproject_home)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.py'
# import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance.settings")

from homepage import models as hmod

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print(row)
	if row[0] != 'Date': # Ignore the header row, import everything else
		transaction = hmod.Transaction()
		transaction.date = "'" + row[0] + "'"
		transaction.description = 'Test'
		transaction.original_description = 'Original description'
		transaction.amount = 4.34
		transaction.transaction_type = 'debit'
		transaction.category = 'Gas'
		transaction.account_name = 'Cody B Pettit'
		print(transaction)
		transaction.save()


			# transaction.description = '"' + row[1] + '"'
			# print(transaction.description)
			# print('"' + row[1] + '"')
			# transaction.original_description = '"' + row[2] + '"'
			# transaction.amount = row[3]
			# transaction.transaction_type = '"' + row[4] + '"'
			# transaction.category = '"' + row[5] + '"'
			# transaction.account_name = '"' + row[6] + '"'