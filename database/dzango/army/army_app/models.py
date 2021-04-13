from django.db import models


class Solider(models.Model):
    id = models.IntegerField(max_length=999999, unique=True, null=False)
    name = models.CharField(max_length=50, help_text="Zadej jmeno vojaka.", null=False)
    age = models.IntegerField(max_length=3, help_text="Zadej vek vojaka", null=False)
    weapon = models.CharField(max_length=20, help_text="Zadej zbran vojaka", null=True)

    def __str__(self):
        return self.name

class Gun(models.Model):
    id = models.CharField(max_length=999999, unique=True, null=False)
    name = models.CharField(max_length=50, help_text="Zadej jmeno zbrane.", null=False)
    ammo = models.IntegerField(max_length=10, help_text="Zadej mnozstvi munice.", null=False)

    def __str__(self):
        return self.name

class Platoon(models.Model):
    id = models.CharField(max_length=999999, unique=True, null=False)
    name = models.CharField(max_length=50, help_text="Zadej jmeno skupiny.", null=False)
    leader = models.CharField(max_length=50, help_text="Zadej jmeno velitele skupiny.", null=False)

    def __str__(self):
        return self.name
