from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_, logout as logout_
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Building, Apartment, Renter, Rental


# Create your views here.

def home(request):
    if User.objects.filter(is_superuser=True).exists():
        # Um usuário admin já existe, não faz nada
        pass
    else:
        # Cria um novo usuário admin
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@biopark.com',
            password='123'
        )
        admin_user.save()
    if request.user.is_authenticated:
        return redirect('/cadastros/')

    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')

# função para cadastro de usuário
def store(request):
    data = {}
    if (request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'As senhas são diferentes'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['first-name']
        user.last_name = request.POST['last-name']
        user.is_superuser = 0
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'login.html', data)

#função para  chamar a tela de login do usuário
def login(request):
    return render(request, 'login.html')

#função que valida os dados de login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login_(request, user)
        return redirect('/cadastros/')
    else:
        data['msg'] = 'Dados inválidos'
        data['class'] = 'alert-danger'
        return render(request, 'login.html', data)


# função que retorna a página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')


# função que realiza o logout do sistema
def logout(request):
    logout_(request)
    return render(request, 'home.html')


# função que retorna a página para alterar a senha do usuário
def changePassword(request):
    return render(request, 'dashboard/changepass.html')

# função que retorna
def changePass(request):
    data = {}
    user = User.objects.get(email=request.user.email)
    password = request.POST.get('oldpassword')

    if user.check_password(password) and request.POST['newpassword'] != password:

        user.set_password(request.POST['newpassword'])
        user.save()
        logout_(request)
        data['msg'] = 'Senha alterada com sucesso, faça login novamente!'
        data['class'] = 'alert-success'
        return render(request, 'login.html', data)
    else:

        data['msg'] = 'Verifique as senhas'
        data['class'] = 'alert-danger'
        return render(request, 'dashboard/changepass.html', data)


def cadastros(request):
    return render(request, 'cadastros/home.html')


def lista_de_alugueis(request):
    rentals = Rental.objects.all()
    return render(request, 'dashboard/home.html', {'rentals': rentals})

##Criando as classes

class BuildingCreateView(CreateView):
    model = Building
    fields = ['nome', 'endereco', 'andares']
    template_name = 'cadastros/add-building.html'
    success_url = reverse_lazy('edificios')

class BuildingListView(ListView):
    model = Building
    context_object_name = 'buildings'


class BuildingUpdateView(UpdateView):
    model = Building
    fields = ['nome', 'endereco', 'andares']


class BuildingDeleteView(DeleteView):
    model = Building
    success_url = reverse_lazy('building-list')


class ApartmentCreateView(CreateView):
    model = Apartment
    fields = ['edificio', 'numero', 'quartos', 'preco']
    template_name = 'cadastros/add_apartment.html'
    success_url = reverse_lazy('apartamentos')

class ApartmentListView(ListView):
    model = Apartment
    context_object_name = 'apartments'



class ApartmentUpdateView(UpdateView):
    model = Apartment
    fields = ['edificio', 'numero', 'quartos', 'preco']
    template_name = 'cadastros/add_apartment.html'
    success_url = reverse_lazy('editarapartamento')


class ApartmentDeleteView(DeleteView):
    model = Apartment
    success_url = reverse_lazy('apartment-list')

class RenterListView(ListView):
    model = Renter
    template_name = 'renter_list.html'
    context_object_name = 'renters'

class RenterCreateView(CreateView):
    model = Renter
    template_name = 'cadastros/add-renter.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('locador')

class RenterUpdateView(UpdateView):
    model = Renter
    template_name = 'renter_form.html'
    fields = ['nome', 'email']

class RenterDeleteView(DeleteView):
    model = Renter
    template_name = 'renter_confirm_delete.html'
    success_url = reverse_lazy('renter_list')


def renter_detail(request, pk):
    renter = get_object_or_404(Renter, pk=pk)
    return render(request, 'renter_detail.html', {'renter': renter})


class RentalListView(ListView):
    model = Rental
    template_name = 'rental_list.html'
    context_object_name = 'rentals'

class RentalCreateView(CreateView):
    model = Rental
    fields = ['locador', 'apartamento', 'data_inicio', 'data_fim']
    template_name = 'cadastros/add-renter.html'
    success_url = reverse_lazy('locacao')

class RentalUpdateView(UpdateView):
    model = Rental
    fields = ['locador', 'apartamento', 'data_inicio', 'data_fim']
    template_name = 'rental_form.html'

class RentalDeleteView(DeleteView):
    model = Rental
    success_url = reverse_lazy('rental-list')
    template_name = 'rental_confirm_delete.html'
