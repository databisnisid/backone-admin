from backone.models import BackOne
from connection.models import ConnectionStatus
from notification.telegram import send_notification_telegram


def get_site_connection_status():
    connection_status = ConnectionStatus.objects.all()

    con_status_members = {}
    members = []
    for cs in connection_status:
        site_members = BackOne.objects.filter(
            connection_status=cs
        )

        #if cs.name=='ON PROGRESS':
        for sm in site_members:
            members.append(sm.name)

        #con_status_members = dict(enumerate(members))
        con_status_members[cs.name] = site_members.count()
    #con_status['ON PROGRESS']['members'] = dict(members)

    #print(con_status_members)

    return con_status_members


def send_report_connection_status():
    cstatus = get_site_connection_status()

    print(cstatus)

    title = 'Report - Connection Status\n'
    message = ' '.join('{}: {}; \n'.format(key, val) for key, val in cstatus.items())
    #for key, val in connection_status.items():
    #    message.join('{}: {}\n'.format(key, val))

    #print(title, message)
    send_notification_telegram(title, message)

