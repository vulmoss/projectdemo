from django.db import models

class Block(models.Model):
    name = models.CharField()
    desc = models.CharField()
    manager_name = models.CharField()
