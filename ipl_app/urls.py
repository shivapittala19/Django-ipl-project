from django.urls import path
from . import views

urlpatterns = [
    path('matches-played',views.MatchesPlayedView.as_view(),name='matches-played'),
    path('matches-won',views.MatchesWonView.as_view(),name='matches-won'),
    path('economical-bowlers/<int:season>',views.EconomicalBowlersView.as_view(),name='economical-bowlers'),
    path('extra-runs/<int:season>',views.ExtraRunsConcededView.as_view(),name='extra-runs'),
    
    # plots
    path('matches-played-plot',views.PlotMatchesPlayedView.as_view(),name='matches-played-plot'),
    path('matches-won-plot',views.PlotMatchesWonView.as_view(),name='matches-won-plot'),
    path('economical-bowlers-plot/<int:season>',views.PlotEconomicalBowlersView.as_view(),name='economical-bowlers-plot'),
    path('extra-runs-plot/<int:season>',views.PlotExtraRunsConcededView.as_view(),name='extra-runs-plot'),
    
    # CRUD OPERATION ON MATCHES 
    path('matches/<int:pk>',views.MatchesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }),name='matches-crud'),
    path('matches-create',views.MatchesViewSet.as_view({'post': 'create',}),name='matches-crud'),
    
    # CRUD OPERATION ON DELIVERIES
    path('deliveries',views.DeliveriesViewSet.as_view({'post': 'create',}),name='deliveries'),
    path('deliveries/<int:pk>',views.DeliveriesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }),name='deliveries'),
   
]

