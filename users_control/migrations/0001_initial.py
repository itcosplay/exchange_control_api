# Generated by Django 4.0.4 on 2022-05-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Пользователь')),
                ('telegram_id', models.IntegerField()),
                ('permission_level', models.CharField(choices=[('A', 'Admin'), ('E', 'Executor'), ('S', 'Secretary'), ('U', 'Unknown')], default='U', max_length=50, verbose_name='Уровень прав')),
            ],
        ),
    ]