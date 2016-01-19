from django.core.management import call_command


def deploy_static():
    call_command('collectstatic', verbosity=0, interactive=False)