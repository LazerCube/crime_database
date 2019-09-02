# Education Management Website Application - College work

![Image of application. Showing admin home page with table of students](https://i.imgur.com/t0VCn5c.png)

Was written as part of a web server scriping module while I was a college and had to meet this specification:

- Implement a simple login system using web server scripting.
- Implement a web content management system that is able to do the following utilities in the numbered list below:
    1. View
    2. Add a new (user)
    3. Edit a user
    4. Delete a user
    5. Form validation (eg check password has at least one number and isn't a simple word)
    6. Filtering (based on Role Student/Admin)
- Implement Access rights to pages depending on the user login. e.g. administrator, operator, and/or visitor

## Getting started

1. To run the app it's requirements need to be installed on your system first `pip install -r requirements.txt`
2. Inorder to setup database `python project/manage.py migrate` must be run.
3. Then inorder to add students a superuser needs to be created first. Run `python project/manage.py createsuperuser` to create an admin account.
4. Start the web server with `python project/manage.py runserver`

Finally go to `localhost:8000` in a browser to view the application.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Python-pip](https://pypi.python.org/pypi/pip) - Dependency Management
- [virtualenv](https://pypi.org/project/virtualenv/) - A tool for creating isolated ‘virtual’ python environments
- [Sqlite](https://www.sqlite.org/index.html) - Database used
- [Bootstrap Theme](http://bootswatch.com) - Css framework. Theme used is called **yeti**