from django.db import models
from django.core.validators import MaxValueValidator

class Trieda(models.Model):
    nazov = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nazov}" 
    
    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"
        ordering = ["nazov"]


class Ucitel(models.Model):
    titul = models.CharField(max_length=10, blank=True)
    meno = models.CharField(max_length=30)
    priezvisko = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254)
    heslo = models.CharField(max_length=50)
                                             

    def __str__(self):
        return f"{self.titul} {self.meno} {self.priezvisko} {self.email} {self.heslo}"
    
                
class Student(models.Model):
    meno = models.CharField(max_length=30)
    priezvisko = models.CharField(max_length=30)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length = 254)
    heslo = models.CharField(max_length=50)
                                                                                         
    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda} {self.email} {self.heslo}"
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]

class Odbor(models.Model):
    nazov = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Odbor"
        verbose_name_plural = "Odbory" 

class Tema(models.Model):
    nazov = models.CharField(max_length=60)
    popis = models.TextField(blank=True)
    konzultant = models.ForeignKey(Ucitel, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    odbor = models.ForeignKey(Odbor, on_delete=models.SET_NULL, null=True)
    konzultacie = models.IntegerField(validators=[MaxValueValidator(3)])
    CHOICES = (
        ('Voľne', 'Voľne'),
        ('Čakajúce', 'Čakajúce'),
        ('Obsadené', 'Obsadené'),
    )
    dostupnost = models.CharField(max_length=300, choices=CHOICES)

    def __str__(self):
        return f"{self.nazov} {self.popis} {self.konzultant} {self.student} {self.dostupnost} {self.odbor} {self.konzultacie}"

    def save(self, *args, **kwargs):
        if self.student is None:
            self.dostupnost = 'Voľne'
            self.konzultacie = 0
        else:
            if self.dostupnost == 'Voľne':
                self.dostupnost = 'Čakajúce' 
        super().save(*args, **kwargs)
    

