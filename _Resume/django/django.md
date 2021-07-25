# Django
<!-- TOC depthFrom:2 orderedList:true -->
- [Django](#django)
  - [Installation](#installation)
  - [Create Project](#create-project)
  - [Start Project Server](#start-project-server)
  - [Create App in the Project](#create-app-in-the-project)
  - [Config App in the Project](#config-app-in-the-project)
    - [Add app in Project](#add-app-in-project)
    - [Add directory in Project](#add-directory-in-project)
    - [Create directory in App](#create-directory-in-app)
      - [In the `urls.py`](#in-the-urlspy)
      - [In the `views.py`](#in-the-viewspy)
    - [Create Page](#create-page)
<!-- /TOC -->

## Installation

pip3 install Django

## Create Project

django-admin startproject `<projectName>`

## Start Project Server

pyton3 `manage.py` runserver

## Create App in the Project

python3 `manage.py` startapp `<appName>`

> **OBS:** first close the server and enter the project
>
> - **Codes:**
>   - Ctrl + C
>   - cd `<projectName>`

## Config App in the Project

### Add app in Project

> **Open:** `<projectName>`/settings.py
>
> **Add in: INSTALLED_APPS:** '`<appName>`'

### Add directory in Project

> **Open:** `<projectName>`/`urls.py`
>
> **Add in: urlpatterns:** path('`<appName>`/', include('`<appName>`.urls')

### Create directory in App

> **Open:** `<projectName>`/`<appName>`
>
> **Create:** `urls.py`

#### In the `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

#### In the `views.py`

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "<appName>/index.html", {})
```

### Create Page

> **Open:** `<projectName>`/`<appName>`
>
> **Create folders:** templates/`<pageName>`  
> **And Create file inside of templates/`<pageName>`**: index.html

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "<appName>/index.html", {})
```
