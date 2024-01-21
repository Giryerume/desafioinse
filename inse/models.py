from django.db import models

# Create your models here.

class Inse(models.Model):
    NU_ANO_SAEB = models.IntegerField(default=0)
    CO_UF = models.IntegerField(default=0)
    SG_UF = models.CharField(max_length=2)
    NO_UF = models.CharField(max_length=100)
    CO_MUNICIPIO = models.IntegerField(default=0)
    NO_MUNICIPIO = models.CharField(max_length=100)
    ID_ESCOLA = models.IntegerField(default=0)
    NO_ESCOLA = models.CharField(max_length=100)
    TP_TIPO_REDE = models.IntegerField(default=0)
    TP_LOCALIZACAO = models.IntegerField(default=0)
    TP_CAPITAL = models.IntegerField(default=0)
    QTD_ALUNOS_INSE = models.IntegerField(default=0)
    MEDIA_INSE = models.FloatField(default=0.0)
    INSE_CLASSIFICACAO = models.CharField(max_length=100)
    PC_NIVEL_1 = models.FloatField(default=0.0)
    PC_NIVEL_2 = models.FloatField(default=0.0)
    PC_NIVEL_3 = models.FloatField(default=0.0)
    PC_NIVEL_4 = models.FloatField(default=0.0)
    PC_NIVEL_5 = models.FloatField(default=0.0)
    PC_NIVEL_6 = models.FloatField(default=0.0)
    PC_NIVEL_7 = models.FloatField(default=0.0)
    PC_NIVEL_8 = models.FloatField(default=0.0)

    def __str__(self):
        return self.NO_ESCOLA
    