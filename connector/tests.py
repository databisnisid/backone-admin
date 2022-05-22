from django.test import TestCase
from .drivers import orbit


def test_orbit():
    q_current, q_total, q_day = orbit.get_quota()

    print(q_total)
    print(q_current)
    print(q_day)

