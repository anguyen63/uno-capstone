# Generated by Django 2.2.1 on 2019-11-02 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0005_auto_20191024_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campuspartner',
            name='partner_status',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partners.PartnerStatus', verbose_name='Campus Partner Status'),
        ),
        migrations.AlterField(
            model_name='communitypartner',
            name='partner_status',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='partners.PartnerStatus', verbose_name='Community Partner Status'),
        ),
    ]