# Generated by Django 3.2 on 2023-03-04 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_featured_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('sender', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('detail', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_pic',
            field=models.ImageField(help_text='อัปโหลดรูปภาพหน้าปก', null=True, upload_to='cover/'),
        ),
    ]
