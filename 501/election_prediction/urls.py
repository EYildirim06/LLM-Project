from django.urls import path
from election_simulator.views import sample_result, sample_simple_random, sample_interval, sample_stratified

urlpatterns = [
    path('', sample_result, name='sample_result'),
    path('sample-simple-random/', sample_simple_random, name='sample_simple_random'),
    path('sample-interval/', sample_interval, name='sample_interval'),
    path('sample-stratified/', sample_stratified, name='sample_stratified'),
]
