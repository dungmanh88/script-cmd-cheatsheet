yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
yum -y install python36u && \
yum -y install python36u-pip && \
yum -y install python36u-devel
mkdir -p src
cd src
python3.6 -m venv manage-ip-env
manage-ip is your programming environment
source manage-ip-env/bin/activate
-> start to use
pip install Django

verify:
python -m django --version
2.1

https://docs.djangoproject.com/en/2.1/intro/tutorial01/
django-admin startproject manage_ip_project
cd manage_ip_project
python manage.py runserver
