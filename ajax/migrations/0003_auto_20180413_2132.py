# Generated by Django 2.0.2 on 2018-04-13 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20180408_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('free', 'Free'), ('starter', 'Starter'), ('premium', 'Premium')], max_length=20)),
                ('devices', models.CharField(choices=[('movie', '720p'), ('episode', '1080p'), ('series', 'ULTRA HD')], max_length=1)),
                ('quality', models.CharField(choices=[('mobile', 'Mobile + Internet'), ('tv', 'TV'), ('all', 'All')], max_length=1)),
                ('movies_limit', models.IntegerField(max_length=20)),
                ('shows_limit', models.IntegerField(max_length=20)),
                ('download', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birthdate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='barners',
            name='for_type',
            field=models.CharField(choices=[('M', 'Movie'), ('S', 'Series')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cast',
            name='for_type',
            field=models.CharField(choices=[('M', 'Movie'), ('E', 'Episode')], max_length=1),
        ),
        migrations.AlterField(
            model_name='images',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='previews',
            name='forType',
            field=models.CharField(choices=[('Movie', 'Movie'), ('Episode', 'Episode'), ('Series', 'Series')], max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
