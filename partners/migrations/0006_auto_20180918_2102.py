# Generated by Django 2.1 on 2018-09-19 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partners', '0005_campuspartner'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusPartnerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='campuspartner',
            old_name='name',
            new_name='campus_partner_name',
        ),
        migrations.AddField(
            model_name='campuspartneruser',
            name='campuspartner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.CampusPartner'),
        ),
        migrations.AddField(
            model_name='campuspartneruser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
