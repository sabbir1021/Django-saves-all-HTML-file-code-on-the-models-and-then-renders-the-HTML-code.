# Generated by Django 4.0.3 on 2022-06-26 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HtmlTemp',
            new_name='HtmlTemplate',
        ),
        migrations.RenameField(
            model_name='htmltemplate',
            old_name='html',
            new_name='html_code',
        ),
    ]
