from django.db import models
from django.urls import reverse


# Create your models here.
class Automobilio_modelis(models.Model):
    marke = models.CharField('Marke', max_length=15)
    modelis = models.CharField('Modelis', max_length=15)

    class Meta:
        verbose_name = 'Automobilio_modelis'
        verbose_name_plural = 'Automobilio_modeliai'

    def __str__(self):
        return f'{self.marke} {self.modelis}'


class Automobilis(models.Model):
    valst_nr = models.CharField('Valstybinis nr.', max_length=6)
    auto_modelis_id = models.ForeignKey('Automobilio_modelis', verbose_name='Modelis', on_delete=models.SET_NULL, null=True)
    vin = models.CharField('VIN kodas', max_length=17)
    klientas = models.CharField('Klientas', max_length=30)

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

    def __str__(self):
        return f'{self.valst_nr} {self.auto_modelis_id}'


class Uzsakymas(models.Model):
    data = models.DateField('Data', blank=True)
    automobilis_id = models.ForeignKey('Automobilis', verbose_name='Automobilis',
                                       on_delete=models.SET_NULL, null=True, related_name='uzsakymai')
    suma = models.FloatField('Suma')

    UZSK_STATUS = (
        ('e', 'Eileje'),
        ('p', 'Priimtas'),
        ('v', 'Vykdomas'),
        ('a', 'Galima atsiimti')
    )

    status = models.CharField(max_length=1, choices=UZSK_STATUS, blank=True, default='e', help_text='Statusas')

    class Meta:
        verbose_name = 'Uzsakymas'
        verbose_name_plural = 'Uzsakymai'

    def __str__(self):
        return f'{self.data} - {self.automobilis_id} - {self.suma}'


class Paslauga(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=50)
    kaina = models.FloatField('Kaina')

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

    def __str__(self):
        return f'{self.pavadinimas}: {self.kaina}'


class Uzsakymo_eilute(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', verbose_name='Paslauga', on_delete=models.SET_NULL, null=True)
    uzsakymas_id = models.ForeignKey('Uzsakymas', verbose_name='Uzsakymas',
                                     on_delete=models.SET_NULL, null=True, related_name='uzsak_eil')
    kiekis = models.IntegerField('Kiekis')
    kaina = models.FloatField('Kaina')

    class Meta:
        verbose_name = 'Uzsakymo_eilute'
        verbose_name_plural = 'Uzsakymo_eilutes'

    def __str__(self):
        return f'{self.paslauga_id} {self.uzsakymas_id} {self.kiekis} - {self.kaina}'
