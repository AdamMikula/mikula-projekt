from django.db import models

class Trieda(models.Model):
    nazov = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nazov}" 
    
    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"
        ordering = ["nazov"]


class Ucitel(models.Model):
    titul = models.CharField(max_length=20)
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    heslo = models.CharField(max_length=30)
                                             

    def __str__(self):
        return f"{self.titul} {self.meno} {self.priezvisko} {self.email} {self.heslo}"
    
                
class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    odbor = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length = 254)
    heslo = models.CharField(max_length=30)
                                                                                         
    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.odbor} {self.trieda} {self.email} {self.heslo}"
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]

class Tema(models.Model):
    nazov = models.CharField(max_length=20)
    popis = models.TextField(blank = True)
    konzultant = models.ForeignKey(Ucitel, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    CHOICES = (
        ('VO', 'Voľne'),
        ('CA', 'Čakajúce'),
        ('OB', 'Obsadené'),
    )
    dostupnost = models.CharField(max_length=300, choices = CHOICES)

    def __str__(self):
        return f"{self.nazov} {self.popis} {self.konzultant} {self.student} {self.dostupnost}"