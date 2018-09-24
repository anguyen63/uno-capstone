# Generated by Django 2.1.1 on 2018-09-23 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partners', '0006_auto_20180918_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityPartnerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communitypartner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.CommunityPartner')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
