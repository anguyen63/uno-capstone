# Generated by Django 2.1.1 on 2018-10-10 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0002_auto_20181009_1909'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='campus_partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.CampusPartner'),
        ),
        migrations.AddField(
            model_name='contact',
            name='community_partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.CommunityPartner'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
