from django.core.management import call_command


def dbbackup_job():
    try:
        call_command('dbbackup')

    except:
        pass