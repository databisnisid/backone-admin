from backone.models import BackOne
from project.models import Project
from orbit.models import Orbit, OrbitMulti
from baso.models import Baso
from connection.models import ConnectionStatus


def total_sites():
    return BackOne.objects.count()


def total_projects():
    return Project.objects.count()


def total_orbits():
    return ( Orbit.objects.count() + OrbitMulti.objects.count() )


def total_basos():
    return Baso.objects.count()


def sites_per_project():
    count = {}
    projects = Project.objects.all()
    for project in projects:
        count[project.name] = BackOne.objects.filter(project=project).count()

    return count


def sites_vs_baso():
    count = {}
    count['NO BASO'] = BackOne.objects.filter(baso=None).count()
    count['BASO'] = BackOne.objects.filter(baso__isnull=False).count()

    return count

def sites_per_status():
    count = {}
    status = ConnectionStatus.objects.all()
    for s in status:
        count[s.name] = BackOne.objects.filter(connection_status=s).count()

    return count
