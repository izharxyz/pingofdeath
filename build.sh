# build_files.sh
echo "########## BUILD START ##########"
uname -a

echo "username: $USER"#
 
python3 -m venv venv 

python3.9 -m pip install --upgrade setuptools
python3 -m pip install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py collectstatic --noinput --clear
echo "########## BUILD END ##########"
