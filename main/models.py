from django.db import models

# Create your models here.


class Appel_Offre(models.Model):
    titre = models.CharField(max_length=200, null=True)
    detail = models.CharField(max_length=800, null=True)
    duree = models.CharField(max_length=200, null=True)
    #date_final = models.DateField(null=False, blank=False)
    secteur = models.ForeignKey(
        'Secteur', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titre


class Secteur(models.Model):
    titre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.titre


class postulation(models.Model):
    # info de user
    #file (CV)
    titre = models.ForeignKey(
        'Appel_Offre', null=True, on_delete=models.SET_NULL)
    detail = models.CharField(max_length=800, null=True)
    budget = models.FloatField(default=0, null=True)
    duree = models.CharField(max_length=20, null=True)
    nom_responsable = models.CharField(max_length=20, null=True)
    #file = models.FileField(upload_to='uploads/')
