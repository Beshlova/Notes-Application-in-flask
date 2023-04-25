Flask Notes Application

Overview

This is a notes application in flask that allows users to sign-in(sign-up and login),create,edit and delete notes. It is not meant to be of any useful real-world application but showcase my backend programming skils.

Content description

It is developed within a 'WEBSITE' directory that contains:-

1. An '__init__.py' FILE which is our application factory.

2. A 'views.py' FILE that defines the routes for our views(navigation,home,notes) except authentication related ones.

3. An 'auth.py' FILE that defines the routes for our authentication pages(signup,login,logout).

4. A 'forms.py' FILE that contains forms for the routes.

5. A 'models.py' FILE that has the database tables for the User class and Note class.

6. An 'app.py' FILE that runs our application but is IN THE MAIN directory.

7. A templates FOLDER that contains templates for the base,home,signup,login,notes and update-notes

