# Key_test

##### Test project for profiles with some features:

* Authentication for pages(main, edit), custom login/logout page;

* Middleware, which stores all requests and their execution time;

* Template context processor, which add django.conf.settings to
context;

* Assigned calendar widget to date field;

* Saving IP of user who makes edit and time of edit, when data in edit form is changes;

* Template tag, which gets any model object, and renders a link of change view in admin interface;

* Django command, which prints all models and object counts in the project;

* Signal handler, which creates a note in database when every model is created/edited/deleted.

---

##### In this project was used:
* Unit tests
* Bootstrap-datepicker
* django-environ - `allows you to use Twelve-factor methodology to configure your Django application with environment variables.`
* django-widget-tweaks - `tweak the form field rendering in templates, not in python-level form definitions.`
* ipython - `is a command shell for interactive computing, that offers introspection, rich media, shell syntax, tab completion, and history. `
* pip-tools - `a set of command line tools to help you keep your pip-based packages fresh.`
* psycopg2-binary - `python-PostgreSQL Database Adapter.`
