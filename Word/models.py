from django.db import models

class Wordturkum(models.Model):
    name = models.CharField(max_length=500)
    search = models.CharField(max_length=500)
    

    def __str__ (self):
        return self.name

class Word(models.Model):
    wordyordamchi = models.CharField(max_length=500)
    wordturkumi =  models.ForeignKey(Wordturkum, on_delete=models.SET_NULL, null=True)
    wordxalqaroteg = models.CharField(max_length=500)
    worduzbekteg = models.CharField(max_length=500)
    wordsof = models.CharField(max_length=500)
    wordshakl = models.CharField(max_length=500)
    wordmanotur = models.CharField(max_length=500)
    worduslubiyxoslanish = models.CharField(max_length=500)
    wordsofturkum = models.CharField(max_length=500,blank=True,null=True)
    text = models.CharField(max_length=500)

    def __str__ (self):
        return self.wordyordamchi