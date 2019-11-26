Basic Installation for Django 

Rename Project : project_name
https://stackoverflow.com/questions/53024807/changing-a-project-name-in-django
from Coder S 


In wsgi.py:

1 Rename line 2 and 14 :

"""
WSGI config for renameProjectHere project.
...
"""


from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'renameProjectHere.settings')

dont forget to change the wsgi.py in the app_name
## renameProjectHere.settings
## old is project_name


In setting.py: 

#line 53

ROOT_URLCONF = 'renameProjectHere.urls'

#line 71 django 2.2 default code

WSGI_APPLICATION = 'renameapp_name.wsgi.application'

In manage.py 

#line 8
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')

After this  change your project now run python mange.py runserver




Rename First app :  app_name
https://stackoverflow.com/questions/8408046/how-to-change-the-name-of-a-django-app
from : Srikar Appalaraju 


Follow these steps to change an app's name in Django:

    1. Rename the folder which is in your project root

    2. Change any references to your app in their dependencies, i.e. the app's views.py, urls.py , 'manage.py' , and settings.py files.

    

    (3. Edit the database table django_content_type with the following command:)    No database create 
         UPDATE django_content_type SET app_label='<NewAppName>' WHERE app_label='<app_name>'
    

    (4. Also if you have models, you will have to rename the model tables. ) No models create 
        For postgres use ALTER TABLE <oldAppName>_modelName RENAME TO <newAppName>_modelName. 
        For mysql too I think it is the same (as mentioned by @null_radix)
    

    5.(For Django >= 1.7) Update the django_migrations table to avoid having your previous migrations re-run: 
        UPDATE django_migrations SET app='<NewAppName>' WHERE app='<OldAppName>'.
        
    
    6. If your models.py 's Meta Class has app_name listed, make sure to rename that too (mentioned by @will).
    
    7. If you've namespaced your static or templates folders inside your app,
        you'll also need to rename those. For example, rename old_app/static/old_app to new_app/static/new_app.
    
    8. For renaming django models, you'll need to change django_content_type.name entry in DB. 
        For postgreSQL use UPDATE django_content_type SET name='<newModelName>' where name='<oldModelName>' AND app_label='<OldAppName>'


Meta point (If using virtualenv): 
    Worth noting, if you are renaming the directory that contains your virtualenv,
    there will likely be several files in your env that contain an absolute path and will also need to be updated. 
    If you are getting errors such as ImportError: No module named ... 
    this might be the culprit. (thanks to @danyamachine for providing this).





python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py createsuperuser : https://docs.djangoproject.com/en/1.8/intro/tutorial02/

