# Django Blog Lesson Steps

## Venv
- python3 -m venv myvenv
- virtualenv venv
- virtualenv venv --system-site-packages
- source venv/bin/activate

## Deactivation a Virtual Environment
- deactivate

## Reactivating a Virtual Environment
- source venv/bin/activate

## Uninstall Packages
- sudo pip3 uninstall packagename

## Install Django (Upto 2022)
- pip install django==1.11.29

## requirements.txt
- pip3 freeze --local > requirements.txt

## Start a Django Project in the Directory
- django-admin startproject blog .

## Change Its Mode to Be Executable to Run It
- chmod +x manage.py

## Initialise the Database and Get the Tables Ready
- ./manage.py migrate

## Allowing Hosts
- In settings.py: 
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                os.environ.get('HOSTNAME')]
```

## Run It in the Server
- python3 ./manage.py runserver

## Initialise Git
- git init

## .gitignore
- echo -e "*.sqlite3\n*.pyc\n.vscode\n/myvenv\n/venv\n__pycache__/" > .gitignore

## Upload Onto Github
- git add .
- git status 
- git commit -m "Created simple Django project"
- git remote add origin < the repository url >
- git push -u origin master

## Travis CI
- Select the project repository
- Click on Unknown 
- Copy and paste the Markdown result to the very bottom of the README.md file (Check raw edits of this README.md file)

## Start An App
- ./manage.py startapp posts

## Set Up the Directories
- In posts folder, create a 'templates' folder
- Create folders in workspace: media -> img
- Create folders in workspace: static -> css, img, js

## Settings
### Recognise the New App
- In settings.py, add 'posts', in INSTALLED_APPS for it to recognise the new app

### Recognise the Where the Template Direcory Is
- In settings.py, add the following in the TEMPLATES:
```python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

### Make Sure to Serve the Media Files Properly
- In settings.py, add the following at the end of the context_processors in TEMPLATES:
```python
'django.template.context_processors.media',
```

### Connect and Serve to the Right Directory
- In settings.py, add the following at the very of the file:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## Models, Admins and Forms
### models.py
```python
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title
```

### forms.py
```python
from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
```
- No views and dates included in the 'fields' variable, as users cannot edit them

### admin.py
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### Install the Pillow Library for Images
- sudo pip3 install pillow 
- pip3 freeze --local > requirements.txt
- ./manage.py makemigrations
- ./manage.py migrate

### views.py
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def get_posts(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
```

### blog -> urls.py
```python
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
```

### posts -> url.py
```python
from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
]
```
- d+ stands for decimal number

## Templates
- base.html, custom.css, blogpost.html, postdetail.html

## Add to Installed Apps
- In settings.py, under INSTALLED_APPS, add_
```python
'django_forms_bootstrap',
```

## Install Django Forms Bootstrap
- sudo pip3 install django-forms-bootstrap

## Create a Super-User
- ./manage.py createsuperuser

## Run Server
- python3 ./manage.py runserver

## Housekeeping
- In settings.py, add:
```python
if os.path.exists('env.py'):
    import env
```
- In settings.py, change the SECRET_KEY to:
```python
SECRET_KEY = os.environ.get("SECRET_KEY")
```

## Heroku
- Create a new app
- Go to resources
- Search for Heroku Postgres and select the free Hobby Dev
- A database key and value should appear in the conf vars
- Add the SECRET_KEY to the conf vars
- Comment in the DATABASE variable and replace it with:
```python
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Add an env.py file and add into it the following: 
```python
import os

os.environ.setdefault("SECRET_KEY", '<get the value of the SECRET_KEY from heroku conf>')
os.environ.setdefault("DATABASE_URL", '<get the value of the DATABASE_URLfrom heroku conf>')
```
- ./manage.py makemigrations
- ./manage.py migrate
- ./manage.py createsuperuser
- python3 ./manage.py runserver

### For Statics
- sudo pip3 install whitenoise
- pip3 freeze --local > requirements.txt

### settings.py
- In the 'MIDDLEWARE' variable, add:
```python
'whitenoise.middleware.WhiteNoiseMiddleware',
```
- Under the 'STATICFILES_DIRS' variable, add
```python 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
``` 

- Change the 'DATABASE' variable to the following:
```python
if "DATABASE_URL" in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    print("Postgres URL not found, using sqlite instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

### Procfile
- Create a Procfile
- Write the following line in it: web: gunicorn blog.wsgi:application

### Install gunicorn
- sudo pip3 install gunicorn

### Hostname
- Add the Heroku page hostname to the 'ALLOWED_HOSTS' variable in settings.py
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                os.environ.get('HOSTNAME')]
```
OR 
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'django-blog-test-app-ci.herokuapp.com']
```
##### Make sure to remove "https//:" and "/" from the Heroku URL in the value

### Deployment
- git add .
- git status 
- git commit -m "Added Heroku and Postgres support for deployment"
- git push

[![Build Status](https://travis-ci.com/Rian1010/django-blog-lessons.svg?branch=master)](https://travis-ci.com/Rian1010/django-blog-lessons)