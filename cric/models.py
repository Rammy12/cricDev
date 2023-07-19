from django.db import models

# Create your models here.


class ipl(models.Model):
    match_name=models.CharField(max_length=200,default="")
    batting_team=models.CharField(max_length=200,default="",blank=False)
    bowling_team=models.CharField(max_length=200,default="",blank=False)
    city=models.CharField(max_length=200,default="",blank=False)
    current_score=models.IntegerField(default=0)
    overs=models.DecimalField(max_digits=3,default=0,decimal_places=1)
    wickets=models.IntegerField(default=0)
    last_five=models.IntegerField(default=0)
    pridicted_score=models.DecimalField(max_digits=4,decimal_places=1,default=0)
    def __str__(self):
        return self.batting_team


class odis(models.Model):
    match_name=models.CharField(max_length=200,default="")
    batting_team=models.CharField(max_length=200,default="",blank=False)
    bowling_team=models.CharField(max_length=200,default="",blank=False)
    city=models.CharField(max_length=200,default="",blank=False)
    current_score=models.IntegerField(default=0)
    overs=models.DecimalField(max_digits=3,default=0,decimal_places=1)
    wickets=models.IntegerField(default=0)
    last_ten=models.IntegerField(default=0)
    pridicted_score=models.DecimalField(max_digits=4,decimal_places=1,default=0)
    def __str__(self):
        return self.batting_team


class t20men(models.Model):
    match_name=models.CharField(max_length=200,default="")
    batting_team=models.CharField(max_length=200,default="",blank=False)
    bowling_team=models.CharField(max_length=200,default="",blank=False)
    city=models.CharField(max_length=200,default="",blank=False)
    current_score=models.IntegerField(default=0)
    overs=models.DecimalField(max_digits=3,default=0,decimal_places=1)
    wickets=models.IntegerField(default=0)
    last_five=models.IntegerField(default=0)
    pridicted_score=models.DecimalField(max_digits=4,default=0,decimal_places=1)
    def __str__(self):
        return self.batting_team
