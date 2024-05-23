create a folder name as backend .
create virtual environment (env) 
# py -m venv env
create a Project but firstly you have to activate the  venv ( env\Scripts\activate)
# django-admin startproject my_tennis_club
create a app name as members 
# py manage.py startapp members
To run server 
# py manage.py runserver
1 project contains 1 or more than one app  
every app has view ,template and model
#  MVT architeture(working )
django dispacture dicide karta kha bhejna hai url = > view = > ka kaam hai model se data pull karna fir wo template ko send  kar dega 
# makemigration => jo bhi changes hue hai unki file bna leta hai (admin mai changes karna hoga phele)=(app bhi resgiter karna hoga settings.py mai)