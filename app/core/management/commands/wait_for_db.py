"""
Django command to wait until PG database is available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to wait for DB."""

    def handle(self, *args, **kwargs):
        """Entrypoint"""
        self.stdout.write('Waiting for DB...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('DB unavailable. wait fot 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Connected to DB.'))
