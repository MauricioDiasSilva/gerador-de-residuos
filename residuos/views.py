# residuos/views.py
from django.shortcuts import render, redirect
from .models import Residuo, Coleta, Recompensa,Residuo
from .forms import ResiduoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ResiduoSerializer

class ResiduoViewSet(viewsets.ModelViewSet):
    queryset = Residuo.objects.all()
    serializer_class = ResiduoSerializer
    permission_classes = [IsAuthenticated]


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'residuos/register.html', {'form': form})


@login_required
def listar_coletas(request):
    coletas = Coleta.objects.filter(residuo__usuario=request.user)
    return render(request, 'residuos/listar_coletas.html', {'coletas': coletas})



def home(request):
    residuos = Residuo.objects.all()
    coletas = Coleta.objects.all()
    recompensas = Recompensa.objects.all()
    context = {
        'residuos': residuos,
        'coletas': coletas,
        'recompensas': recompensas,
    }
    return render(request, 'residuos/home.html', context)


@login_required
def registrar_residuo(request):
    if request.method == "POST":
        form = ResiduoForm(request.POST)
        if form.is_valid():
            residuo = form.save(commit=False)
            residuo.usuario = request.user
            residuo.save()
            Coleta.objects.create(residuo=residuo, data_coleta=residuo.data_registro, localizacao="Local Padrão")
            return redirect('listar_coletas')
    else:
        form = ResiduoForm()
    return render(request, 'residuos/registrar_residuo.html', {'form': form})





def catalogo_recompensas(request):
    recompensas = Recompensa.objects.all()
    return render(request, 'residuos/catalogo_recompensas.html', {'recompensas': recompensas})

def trocar_recompensa(request, recompensa_id):
    recompensa = get_object_or_404(Recompensa, id=recompensa_id)
    if request.user.pontos >= recompensa.pontos_necessarios:
        request.user.pontos -= recompensa.pontos_necessarios
        request.user.save()
        # Aqui você pode adicionar lógica para registrar a troca ou enviar um e-mail de confirmação
        return redirect('catalogo_recompensas')
    else:
        return redirect('catalogo_recompensas')

