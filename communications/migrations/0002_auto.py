from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='friend',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friend_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]