# build_files.sh
echo "########## BUILD START ##########"
pyhton3.9 -m pip install -r requirements.txt

python3.9 manage.py makemigrations
pyhton3.9 manage.py migrate

python3.9 manage.py collectstatic --noinput --clear
echo "########## BUILD END ##########"
