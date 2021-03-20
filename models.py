from django.db import models
class Patient(models.Model):
    Pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    age = models.IntegerField()

    def __str__(self):
        return self.Pid
class Answer(models.Model):
    Pid = models.OneToOneField(Patient,on_delete=models.CASCADE,primary_key=True)
    Ansid = models.IntegerField()
class QuesAns(models.Model):
    Qid = models.IntegerField(primary_key=True)
    Question = models.CharField(max_length=70)

class Results(models.Model):
    Qid = models.OneToOneField(QuesAns, on_delete=models.CASCADE,primary_key=True)
    Ansid = models.IntegerField()
    Answers = models.CharField(max_length=70)







# Create your models here.
