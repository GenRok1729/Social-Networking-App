from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_customnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='status',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
