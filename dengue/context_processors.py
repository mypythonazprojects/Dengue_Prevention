from dengue.models import *
from django.contrib.admin.models import LogEntry
from django.db import connection
import datetime
from datetime import date
from datetime import timedelta
def numbercount(request):
	logCount = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20].count()
	dacount= DengueArea.objects.count()
	args = {'logCount':logCount, 'dacount':dacount}
	return args