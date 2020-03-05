
import os 
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_system.settings')
django.setup()

users  = [
    {'username':'testuser','password':'default2054'  ,'phone':'982922828'},
    {'username':'testuser1','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser2','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser3','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser4','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser5','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser6','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser7','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser8','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser9','password':'default2054' ,'phone':'982922828'},
    {'username':'testuser10','password':'default2054','phone':'982922828'},
    {'username':'testuser11','password':'default2054','phone':'982922828'},
    {'username':'testuser12','password':'default2054','phone':'982922828'},
    {'username':'testuser13','password':'default2054','phone':'982922828'},
    {'username':'testuser14','password':'default2054','phone':'982922828'}
]
from users.models import User 

for user in users:
    usr = User.objects.create(
            username =user['username'],
            phone   =user['phone']
        )
    usr.set_password(user['password'])
    usr.save()
print("User Inserted SuccessFully")



