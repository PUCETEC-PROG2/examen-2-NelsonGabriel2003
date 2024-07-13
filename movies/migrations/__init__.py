from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('synopsis',models.TextField(max_length=200)),
            ],
        ),
    ]
