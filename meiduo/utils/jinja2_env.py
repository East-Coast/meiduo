from jinja2 import Environment
from  django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import resolve

def jinja2_environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static':staticfiles_storage.url,
        'url':resolve
    })
    return  env