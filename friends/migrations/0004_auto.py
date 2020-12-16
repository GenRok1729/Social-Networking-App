from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_friend_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='status',
            field=models.CharField(default='requested', max_length=20),
        ),
    ]
