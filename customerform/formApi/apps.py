from django.apps import AppConfig
from .models import Requestforms

def do_stuff(sender, **kwargs):
    mymodel = sender.get_model('Requestforms')
    mymodel.objects.get() # etc...

class MyAppConfig(AppConfig):
    name = 'formApi'

    def ready(self):
        post_migrate.connect(do_stuff, sender=self)