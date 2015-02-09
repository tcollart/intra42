import ldap3

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from localsettings import PASSWORD_42
from apps.students.models import Student


class Command(BaseCommand):
    help = 'Use ldap to populate the db with students'

    def handle(self, *args, **options):
        s = ldap3.Server("ldaps://ldap.42.fr", port=636, use_ssl=True, get_info=ldap3.GET_ALL_INFO)
        c = ldap3.Connection(s,
                             authentication=ldap3.AUTH_SIMPLE,
                             check_names=True,
                             auto_bind=True,
                             user="uid=tcollart,ou=july,ou=2013,ou=paris,ou=people,dc=42,dc=fr",
                             password=PASSWORD_42)
        c.search(search_base='ou=paris,ou=people,dc=42,dc=fr', search_filter='(ObjectClass=ftUser)',
                 search_scope=ldap3.SEARCH_SCOPE_WHOLE_SUBTREE, attributes=ldap3.ALL_ATTRIBUTES)

        for student in c.response:
            attributes = student['attributes']

            username = attributes['uid'][0] if 'uid' in attributes and len(attributes['uid']) else None
            first_name = attributes['givenName'][0] if 'givenName' in attributes and len(attributes['givenName']) else None
            last_name = attributes['sn'][0] if 'sn' in attributes and len(attributes['sn']) else None
            birth_date = None
            picture = attributes['jpegPhoto'][0] if 'jpegPhoto' in attributes and len(attributes['jpegPhoto']) else None
            phone_number = attributes['mobile'][0] if 'mobile' in attributes and len(attributes['mobile']) else None

            print(username)
            if username and username:
                user_obj = User(username=username, first_name=first_name, last_name=last_name, is_active=False)
                user_obj.save()
                student_obj = Student(user=user_obj,
                                      birth_date=birth_date,
                                      picture=picture,
                                      phone_number=phone_number,
                                      slug=user_obj.username)
                student_obj.save()