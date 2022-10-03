import logging

from django.db import migrations

from core.utils import insert_role_right_for_system

logger = logging.getLogger(__name__)


def add_rights(apps, schema_editor):
    insert_role_right_for_system(64, 157101)  # Payment plan
    insert_role_right_for_system(64, 157102)
    insert_role_right_for_system(64, 157103)
    insert_role_right_for_system(64, 157104)
    insert_role_right_for_system(64, 157106)


class Migration(migrations.Migration):
    dependencies = [
        ('contribution_plan', '0009_contributionplan_roles_for_admin')
    ]

    operations = [
        migrations.RunPython(add_rights),
    ]
