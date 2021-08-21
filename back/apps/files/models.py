from django.db import models
from datetime import datetime, timezone
from apps.accounts.models import User

class Files(models.Model):
    name = models.fields.CharField("Name", max_length=100)
    path = models.fields.CharField("Path", max_length=150)
    last_date_update = models.fields.DateTimeField("Last date update")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    last_date_info = models.fields.DateTimeField("Last date info", auto_now=True)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self) -> str:
        return self.name

    @property
    def days_until_update(self):
        if self.last_date_update is None:
            return 0

        dif = datetime.now(timezone.utc) - self.last_date_update
        return dif.days