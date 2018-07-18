from Park.models import Park
#from django_crontab.app_settings import Settings

def set_capacity_all_parks():

	parks = Park.objects.all()

	for park in parks:
		Park.set_capacity()
