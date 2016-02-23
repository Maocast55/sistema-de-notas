from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            print 'update ' + str(user.pk)
            user.set_password('1234')
            user.save()
