# Variables in HTMl witch Django
<!-- TOC -->
- [Variables in HTMl witch Django](#variables-in-html-witch-django)
  - [Open directory with container css](#open-directory-with-container-css)
  - [If and Else If](#if-and-else-if)
  - [For](#for)
  - [Block with content](#block-with-content)
  - [Link relative page](#link-relative-page)
<!-- /TOC -->
## Open directory with container css

Create folder static with container css files.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="stylesheet" href="{% static '<appName>/styles.css' %}">
    </head>
```

## If and Else If

```html
{% if <parameter> %}
    <!-- html it's if -->
{% else %}
    <!-- html it's else -->
{% endif %}
```

## For

```html
<ul>
    {% for task in tasks %}
        <li>{{ task }}</li>
    {% endfor %}  
</ul>
```

## Block with content

Import for example header of content.

```html
{% extends "tasks/layout.html" %}

{% block body %}
<!-- Code -->
{% endblock %}
```

## Link relative page

First create name of app

In: `urls.py` add:

```python
app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]
```

After link pages

In: pages add:

```html
<a href="{% url 'tasks:add' %}">Add a New Task</a>
```

python3 manage.py migrate