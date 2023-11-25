from django.db import models

# Create your models here.

class Matches(models.Model):
    season = models.IntegerField()
    city = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(auto_now=False)
    team1 = models.CharField(max_length=255, blank=True, null=True)
    team2 = models.CharField(max_length=255, blank=True, null=True)
    toss_winner = models.CharField(max_length=255, blank=True, null=True)
    toss_decision = models.CharField(max_length=10,blank=True, null=True)
    result = models.CharField(max_length=10,blank=True, null=True)
    dl_applied = models.IntegerField()
    winner = models.CharField(max_length=255, blank=True, null=True)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=255, blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True)
    umpire1 = models.CharField(max_length=255, blank=True, null=True)
    umpire2 = models.CharField(max_length=255, blank=True, null=True)
    umpire3 = models.CharField(max_length=255, blank=True, null=True)
    
class Deliveries(models.Model):
    id = models.AutoField(primary_key=True)
    match_id = models.ForeignKey(Matches,on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=255, blank=True, null=True)
    bowling_team = models.CharField(max_length=255, blank=True, null=True)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=255, blank=True, null=True)
    non_striker = models.CharField(max_length=255, blank=True, null=True)
    bowler = models.CharField(max_length=255, blank=True, null=True)
    is_super_over = models.IntegerField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=255, blank=True, null=True)
    dismissal_kind = models.CharField(max_length=255,blank=True, null=True)
    fielder = models.CharField(max_length=255, blank=True, null=True)

    