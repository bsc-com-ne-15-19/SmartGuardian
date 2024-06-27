import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

"""
This module initializes and configures the Celery application for the dcelery project.

The Celery application is used for asynchronous task processing in the Django project.
It sets the default Django settings module and configures the Celery application using
the settings from the Django project.

Functions:
    - None

Classes:
    - None

Variables:
    - app: The Celery application instance.

Usage:
    - This module is imported and used by other modules in the project to define
      and execute Celery tasks.

Note:
    - This module assumes that the Django project is already set up and the necessary
      settings are configured.
"""