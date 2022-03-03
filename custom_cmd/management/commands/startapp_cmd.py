from django.core.management.base import BaseCommand
import os
import sys

class Command(BaseCommand):
    help = 'Custom startapp Command to create new custom app'

    def add_arguments(self, parser):
        parser.add_argument('app_name')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        current_directory = os.getcwd()
        user_input = os.path.join(current_directory,app_name)
        if not os.path.exists(user_input):
            os.makedirs(user_input) 
        viewspath = os.path.join(user_input, 'views.py')
        views = open(viewspath, "a")
        mpath = os.path.join(user_input, 'models.py')
        m = open(mpath,"a")
        spath = os.path.join(user_input, 'serializers.py')
        s = open(spath,"a")
        sspath = os.path.join(user_input, 'services.py')
        ss = open(sspath,"a")
        ipath = os.path.join(user_input, '__init__.py')
        i = open(ipath,"a")
