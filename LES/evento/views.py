from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import InserirInscricao
from .models import (Evento, Participante, Inscricao, Utilizador, Proponente)


def home(request):
    return render(request, 'evento/inicio.html')


def vieweventos(request):
    context = {
        'eventos' : Evento.objects.all()
    }
    return render(request, 'evento/vieweventos.html', context)

# class vieweventos(ListView):
#     modul = Evento
#     template_name = 'evento/vieweventos.html'
#     context_object_name = 'eventos'
#     def get_queryset(self):
#         proponente = get_object_or_404(Proponente, utilizadorid=self.kwargs.get('utilizadorid'))
#         return Evento.objects.filter(proponenteutilizadorid=proponente)
    

def criarinscricao(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InserirInscricao(request.POST)
        # check whether it's valid:
        if form.is_valid():
            evento_id_r = request.POST.get('eventoid')
            Evento_r = Evento.objects.get(pk=evento_id_r)
            participanteutilizadorid_r = request.POST.get('participanteutilizadorid')
            Participante_r = Participante.objects.get(pk=participanteutilizadorid_r)
            requer_certificado_r = ('requer_certificado')
            if requer_certificado_r == 'requer_certificado':
                requer_certificado_r = 1
            Inscricao_r = Inscricao(eventoid=Evento_r, requer_certificado=requer_certificado_r,
                                    participanteutilizadorid=Participante_r)
            Inscricao_r.save()
            return redirect(home)
        else:
            return redirect(criarinscricao)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InserirInscricao()

    return render(request, 'evento/inscricao.html', {'form': form})



# Create your views here.
