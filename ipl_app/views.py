#imports
import json

# django
from django.shortcuts import render
from django.db.models import Count, Sum, F, Case, When

#rest_framework
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

#In app imports
from .models import Matches, Deliveries

# Create your views here.

class MatchesPlayedView(APIView):
    @swagger_auto_schema(responses={200: "OK"},tags=["Json Data"])
    def get(self, requst,format = None):
        queryset = Matches.objects.values('season').annotate(num_matches = Count('id')).order_by('season')
        context = {
        'matches_per_year' : list(queryset)
        }
        return Response(context)

class EconomicalBowlersView(APIView):
    @swagger_auto_schema(responses={200: "OK"},tags=["Json Data"])
    def get(self, request, season, format=None):
        queryset = (
            Deliveries.objects.filter(match_id__season=season)
            .values('bowler')
            .annotate(
                economy=
                    Sum(F('total_runs') - F('legbye_runs') - F('bye_runs')) * 6.0 / Count(
                    Case(
                        When(wide_runs=0, noball_runs=0, then=1),
                    ))  
            )
            .order_by('economy')[:10]
        )
        context ={
            'economy_bowler': [{'bowler' : bowler['bowler'], 'economy': round(bowler['economy'],2)} for bowler in queryset]
        }
        return Response(context)

class ExtraRunsConcededView(APIView):
    @swagger_auto_schema(responses={200: "OK"},tags=["Json Data"])
    def get(self, request, season, format=None):
        queryset = Deliveries.objects.filter(match_id__season = season).values('bowling_team').annotate(extra_runs = Sum('extra_runs')).order_by('bowling_team')
        context ={
            'extra_runs_conceded':list(queryset)
        }
        return Response(context)

class MatchesWonView(APIView):
    @swagger_auto_schema(responses={200: "OK"},tags=["Json Data"])
    def get(self, request, format=None):
        queryset = Matches.objects.values('season','winner').annotate(won_matches = Count('winner')).order_by('season')
        data_fromat ={}
        for entry in queryset:
            if str(entry['season']) in data_fromat:
                data_fromat[str(entry['season'])][entry['winner']] = entry['won_matches']
            else:
                data_fromat[str(entry['season'])] = {}

        context = {
            'number_of_matches_won' : data_fromat   
        }
        return Response(context)

class PlotMatchesPlayedView(APIView):
    @swagger_auto_schema(responses={200: "OK"},tags=["Plots"])
    def get(self,request,format=None):
        data = MatchesPlayedView().get(request.data).data
        return render(
            request,
            "matches_played.html",
            {'data': data['matches_per_year']}
        )
    
class PlotEconomicalBowlersView(APIView):
    @swagger_auto_schema(responses={200: "OK"},tags=["Plots"])
    def get(self, request,season, format=None):
        data = EconomicalBowlersView().get(request.data,season).data
        return render(
            request,
            'economy.html',
            {'data':data['economy_bowler']}
        )

class PlotExtraRunsConcededView(APIView):
    @swagger_auto_schema(responses={200: "OK"},tags=["Plots"])
    def get(self, request, season, format=None):
        data = ExtraRunsConcededView().get(request.data, season).data
        return render(
            request,
            'extra_runs.html',
            {'data':data['extra_runs_conceded']}
        )

class PlotMatchesWonView(APIView):
    @swagger_auto_schema(responses={200: "OK"},tags=["Plots"])
    def get(self,request, format=None):
        data = MatchesWonView().get(request.data).data
        return render(
            request,
            'matches_won.html',
            {'data':data['number_of_matches_won']}
        )
        
