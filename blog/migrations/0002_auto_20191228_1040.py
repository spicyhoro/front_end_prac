# Generated by Django 2.2.7 on 2019-12-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]