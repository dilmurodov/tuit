# Generated by Django 3.2.9 on 2021-11-22 11:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tuit', '0002_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('text', models.TextField(verbose_name='Текст Коммента')),
                ('time_cr', models.DateTimeField(auto_now_add=True, verbose_name='Время создание коммент')),
                ('time_up', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='tuit.post', verbose_name='автор')),
            ],
            options={
                'ordering': ('-time_cr',),
            },
        ),
    ]
