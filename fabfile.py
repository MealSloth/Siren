from fabric.api import *

env.hosts = ['localhost', 'test.mealsloth.com', 'mealsloth.com']

env.project_root = ''


def deploy_static():
    with cd(env.project_root):
        run('./manage.py collectstatic -v0 --noinput')