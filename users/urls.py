from django.urls import path
from users.views import Login, Logout, CreateAccount

urlpatterns = [path('login/', Login.as_view(), name='login'),
               path('logout/', Logout.as_view(), name='logout'),
               path('create_account/', CreateAccount.as_view(),
               name='create_account')]
