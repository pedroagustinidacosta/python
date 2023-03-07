"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, signup, store, login, dologin, dashboard, cadastros, logout, changePassword, changePass, BuildingCreateView
from app.views import ApartmentCreateView,lista_de_alugueis, ApartmentUpdateView, RenterListView, RenterCreateView, RenterUpdateView, RenterDeleteView
from app.views import renter_detail, RentalListView, RentalCreateView, RentalUpdateView, RentalDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('signup/', signup),
    path('store/', store),
    path('login/', login),
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('cadastros/', cadastros),
    path('logout/', logout),
    path('changePassword/', changePassword),
    path('changePass/', changePass),
    path('cadastros/novo-edificio', BuildingCreateView.as_view(),name='edificios'),
    path('cadastros/novo-apartamento', ApartmentCreateView.as_view(),name='apartamentos'),
    path('alugueis/', lista_de_alugueis, name='lista_de_alugueis'),
    path('editar/apartamentos/<int:pk>', ApartmentUpdateView.as_view(),name='editarapartamento'),
    path('renters/', RenterListView.as_view(), name='renter_list'),
    path('cadastros/novo-locador/', RenterCreateView.as_view(), name='locador'),
    path('renter/<int:pk>/edit/', RenterUpdateView.as_view(), name='renter_edit'),
    path('renter/<int:pk>/delete/', RenterDeleteView.as_view(), name='renter_delete'),
    path('renter/<int:pk>/', renter_detail, name='renter_detail'),
    path('', RentalListView.as_view(), name='rental-list'),
    path('cadastros/nova-locacao/', RentalCreateView.as_view(), name='locacao'),
    path('<int:pk>/update/', RentalUpdateView.as_view(), name='rental-update'),
    path('<int:pk>/delete/', RentalDeleteView.as_view(), name='rental-delete'),
]




