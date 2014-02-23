suni
====
Kindergarten Management


Cloning
----
git clone https://github.com/soulsplit/suni.git


About
----
This project is a kindergarten management application utilizing [django](https://www.djangoproject.com/) and its admin interface.


Security
----
Please make sure to adapt your settings.py by creating your own SECRET_KEY and disabling the DEBUG flags.
To generate a key you can use [django-extensions](https://github.com/django-extensions/django-extensions) and the following command:

```bash
python manage.py generate_secret_key
```

The key below should not be used by anyone.

```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8s_secu%8q0yrl^#$(eb-8b$ezkc7%(gd2df=l_u@!!&9mh3vw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
```


Setup
----
To prepare you environment you will have to have the following installed:

- django-extensions
- south
- werkzeug


You can install it like this:

```bash
pip install south werkzeug django-extensions
```

Database Management
----
By default this project uses postgreSQL.

To create the database simply execute:

```bash
createdb suni -U postgres
```

To drop the database simply execute:

```bash
dropdb suni -U postgres
```

To manage migrations for the models to the database this project relies on [South](http://south.readthedocs.org/en/latest/)
You need to synchronize your models at the beginning and create migrations if you changed something.

Initially:

```bash
python manage.py syncdb
python manage.py migrate
```

After some changes:

```bash
python manage.py schemamigration kindergarten --auto
python manage.py migrate kindergarten
```


Theming and extended features
----
I have been playing with [django-admin-tools](https://bitbucket.org/izi/django-admin-tools/wiki/Home) but it is disabled by default. You can enable it by just uncommenting some lines in the settings.py and urls.py
I didn't want to make it a dependency from the start as I feel that everybody should decide by themselves if they want that. Additionally, I ran into this [bug](https://bitbucket.org/izi/django-admin-tools/issue/133/recent-actions-links-have-an-unecessary).


ToDo
----
- Testing password recovery
- Enhancing interface and usability
