from django import forms
from .models import (Inscricao, Evento, Participante, Pergunta)

class InserirInscricao(forms.ModelForm):
    requer_certificado = forms.BooleanField( label='requer_certificado',required=True, initial=False,
        widget= forms.CheckboxInput(
           attrs= {'class': ''}
        )
    )

    eventoid = forms.ModelChoiceField(
        queryset=Evento.objects.all(),
        label='evento',
        empty_label='Escolha uma das opções',
        widget=forms.Select(
            attrs={'class':'input'}
        )
    )

    participanteutilizadorid = forms.ModelChoiceField(
        queryset=Participante.objects.all(),
        label='participante',
        empty_label='Escolha uma das opções',
        widget=forms.Select(
            attrs={'class':'input'}
        )
    )
    

    class Meta:
        model = Inscricao
        fields = ['eventoid', 'requer_certificado', 'participanteutilizadorid']


    