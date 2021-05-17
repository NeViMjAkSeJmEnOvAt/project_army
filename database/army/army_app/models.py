from django.db import models
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def img_path(instance, filename):
    return "images/" + filename


def img_path_rank(instance, filename):
    return "images/rank/" + filename

def img_path_ammo(instance, filename):
    return "images/ammo/" + filename


class Ammo(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno naboje.", null=False)
    weight = models.FloatField(help_text="váha kulky.", null=False)
    bullet_diameter = models.FloatField(help_text="průměr kulky.", null=False)
    bullet_lenght = models.FloatField(help_text="délka kulky.", null=False)

    armor_penetration = models.FloatField(help_text="prostreleni zbroje.", null=False)
    default_penetration = models.IntegerField(help_text="prostreleni tkání", null=False)
    muzzle_speed = models.IntegerField(help_text="úsťová rychlost", null=False)
    muzzle_energy = models.IntegerField(help_text="úsťová energie", null=False)

    image = models.ImageField(help_text="vlož obrázek náboje", upload_to=img_path_ammo, blank=True, null=True, verbose_name="Fotka")
    image_des = models.ImageField(help_text="vlož obrázek s popisem", upload_to=img_path_ammo, blank=True, null=True, verbose_name="Fotka popis")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_url(self):
        return ("ammo/" + self.id)


class Gun(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno zbrane.", null=False)
    weight = models.IntegerField(help_text="Zadej vahu zbrane.", null=False, default="1")
    lenght = models.IntegerField(help_text="Zadej delku zbrane.", null=False, default="1")
    lenght_barrel = models.IntegerField(help_text="Zadej delku hlavne zbrane.", null=False, default="1")

    ammo = models.IntegerField(help_text="Zadej mnozstvi munice.", null=False)
    ammo_type = models.ForeignKey('Ammo', on_delete=models.SET("5.56"), null=False, default="1")

    active_range = models.IntegerField(help_text="Zadej aktivni dostrel.", null=False, default='200')
    max_range = models.IntegerField(help_text="Zadej maximalni dostrel.", null=False, default='1000')
    fire_rate = models.IntegerField(help_text="Zadejte kadenci zbrane.", null=False, default='300')
    country = models.CharField(max_length=(50), help_text="Zadejte misto vyroby.", null=False, default='none')

    image = models.ImageField(help_text="vlož obrázek", upload_to=img_path, blank=True, null=True, verbose_name="Fotka")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ranks(models.Model):
    name = models.CharField(max_length=100, help_text="Zadej název hodnosti.", null=False)
    tree = models.CharField(max_length=100, help_text="Zadej název skupiny hodností.", null=False)
    score = models.IntegerField(null=False, default="1")

    image = models.ImageField(help_text="vlož obrázek", upload_to=img_path_rank, blank=True, null=True, verbose_name="Fotka")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Solider(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno vojaka.", null=False)
    date_of_birth = models.DateField(help_text="Zadej datum narezeni", null=False, default="1991-01-01")
    score_run = models.IntegerField(null=True, default="0")
    score_pushup = models.IntegerField(null=True, default="0")
    score_situp = models.IntegerField(null=True, default="0")

    rank = models.ForeignKey('Ranks', on_delete=models.SET("Vojín"), null=False, default="1")
    weapon = models.ForeignKey('Gun', on_delete=models.SET_NULL, null=True)
    activity = models.BooleanField(help_text="Je vojak prave aktivni?", null=False, default='True')
    country = models.CharField(max_length=255, help_text="Zadejte misto narozeni.", null=False, default='USA')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Platoon(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno skupiny.", null=False)
    leader = models.ForeignKey('Solider', on_delete=models.SET('Neurceno'), null=False)
    country = models.CharField(max_length=255, help_text="Zadejte misto nasazeni skupiny.", null=True, default='neurceno')
    specialization = models.CharField(max_length=255, help_text="Zadejte specializaci skupiny.", null=False, default='Zaloha')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


