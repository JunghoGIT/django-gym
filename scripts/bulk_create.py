import os
import django
from datetime import datetime
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "config.settings")
django.setup()

from study.models import Nothing

#------------------------------------------------

start = datetime.now()

for i in range(5):
    Nothing.objects.create(contents=f'test{i}')
time = datetime.now()-start

print(f'objects.save() : {time}')

# ------------------------------------------------

start = datetime.now()

n_list = [Nothing(contents=f'test{i}') for i in range(5)]

Nothing.objects.bulk_create(n_list)

time = datetime.now()-start

print(f'bulk_create : {time}')

Nothing.objects.all().delete()

print(connection.queries)