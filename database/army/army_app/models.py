from django.db import models

def img_path(instance, filename):
    return "images/" + filename

class Solider(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno vojaka.", null=False)
    date_of_birth = models.DateField(help_text="Zadej datum narezeni", null=False, default="1991-01-01")
    rank = models.CharField(max_length=50, help_text="Zadej hodnost vojaka.", null=False, default='privateD')
    weapon = models.ForeignKey('Gun', on_delete=models.SET_NULL, null=True)
    activity = models.BooleanField(help_text="Je vojak prave aktivni?", null=False, default='True')
    country = models.CharField(max_length=255, help_text="Zadejte misto narozeni.", null=False, default='USA')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Gun(models.Model):
    name = models.CharField(max_length=50, help_text="Zadej jmeno zbrane.", null=False)
    ammo = models.IntegerField(help_text="Zadej mnozstvi munice.", null=False)
    ammo_type = models.FloatField(help_text="Zadej typ munice.", null=False, default='9')
    active_range = models.IntegerField(help_text="Zadej aktivni dostrel.", null=False, default='200')
    max_range = models.IntegerField(help_text="Zadej maximalni dostrel.", null=False, default='1000')
    fire_rate = models.IntegerField(help_text="Zadejte kadenci zbrane.", null=False, default='300')
    image = models.ImageField(help_text="vlož obrázek", upload_to=img_path, blank=True, null=True, verbose_name="Fotka")

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
