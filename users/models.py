from django.db import models


class Users(models.Model):
    info_id = models.AutoField(primary_key=True)
    agg_id = models.TextField(null=True, blank=True)
    family_name = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'users'
        managed = False
