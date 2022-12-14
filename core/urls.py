from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('ranking/',views.ranking, name = 'ranking'),
    path('comissao/',views.comissao, name = 'comissao'),
    path('detalhado/',views.detal, name='detalhado'),
    path('mcfeed/',views.mcfeed, name='mcfeed'),
    path('campanha/', views.campanha, name='campanha'),
    path('prevcom/',views.prevcom, name='prevcom'),
    path('login/',views.login_user,name='login'),
    path('login/submit',views.submit_login),
    path('logout/',views.logout_user, name='logout'),
]