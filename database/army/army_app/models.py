from django.db import models


class Solider(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno vojaka.", null=False)
    age = models.IntegerField(help_text="Zadej vek vojaka", null=False)
    rank = models.CharField(max_length=50, help_text="Zadej hodnost vojaka.", null=False)
    weapon = models.ForeignKey('Gun', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Gun(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno zbrane.", null=False)
    ammo = models.IntegerField(help_text="Zadej mnozstvi munice.", null=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Platoon(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno skupiny.", null=False)
    leader = models.CharField(max_length=50, help_text="Zadej jmeno velitele skupiny.", null=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
