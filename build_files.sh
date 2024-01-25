 echo "BUILD START"
 python3.11 -m pip install -r requirements.txt
 python3.11 manage.py collectstatic --noinput --clear
 python manage.py makemigrations  
 python manage.py migrate  
 echo "BUILD END"