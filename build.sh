# build_files.sh
echo "########## BUILD START ##########"
uname -a

echo "username: $USER"
ifconfig

sudo systemctl status sshd

python3.9 -m pip install pip==21.3.1


# python3.9 -m pip install --upgrade setuptools
python3.9 -m pip install -r requirements.txt

python3.9 manage.py makemigrations
python3.9 manage.py migrate

python3.9 manage.py collectstatic --noinput --clear
echo "########## BUILD END ##########"
