# Paint_solve
 <p> use python 9.0 to use mysql database connector mysqlclient
<br>
cd into paint_solve/paint_solve and change settings.py to add database 
name of the database, password </p>
```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '', 
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306'
    }
}

```

 1
```
 pip install -r requirements.txt
```
 2
cd into paint_solve_ver_1 directory and run following commands
```
  source virt/Scripts/activate
```
 3
cd into paint_solve and run 
```
 python manage.py makemigrations
```
 4
```
 python manage.py migrate
```
 5
```
 python manage.py runserver
```
