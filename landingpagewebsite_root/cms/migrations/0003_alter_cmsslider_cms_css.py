# Generated by Django 4.1.3 on 2022-12-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
    ]
