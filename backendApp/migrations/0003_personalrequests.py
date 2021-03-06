# Generated by Django 2.2.6 on 2019-10-31 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backendApp', '0002_requestsmade_last_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRequests',
            fields=[
                ('requestsmade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backendApp.RequestsMade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('backendApp.requestsmade',),
        ),
    ]
