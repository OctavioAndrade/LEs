# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'campus'


class Edificio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.DO_NOTHING, db_column='CampusID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'edificio'


class Equipamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    tipo_equipamentoid = models.ForeignKey('TipoEquipamento', models.DO_NOTHING, db_column='Tipo_EquipamentoID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'equipamento'


class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade')  # Field name made lowercase.
    aprovado = models.IntegerField(db_column='Aprovado')  # Field name made lowercase.
    dia = models.DateField(db_column='Dia')  # Field name made lowercase.
    hora_de_inicio = models.TimeField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duracao = models.IntegerField(db_column='Duracao')  # Field name made lowercase.
    campusid = models.IntegerField(db_column='CampusID', blank=True, null=True)  # Field name made lowercase.
    formulariofeedbackid = models.ForeignKey('Formulario', models.DO_NOTHING, db_column='FormularioFeedbackID', related_name='feedbackid')  # Field name made lowercase.
    formularioinscricaoid = models.ForeignKey('Formulario', models.DO_NOTHING, db_column='FormularioInscricaoID')  # Field name made lowercase.
    tipo_de_eventoid = models.ForeignKey('TipoDeEvento', models.DO_NOTHING, db_column='Tipo de EventoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    proponenteutilizadorid = models.ForeignKey('Proponente', models.DO_NOTHING, db_column='ProponenteUtilizadorID', blank=True, null=True)  # Field name made lowercase.
    nome_de_evento = models.CharField(db_column='Nome de evento', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.nome_de_evento

    class Meta:
        managed = True
        db_table = 'evento'


class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inscricaoid = models.ForeignKey('Inscricao', models.DO_NOTHING, db_column='InscricaoID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'feedback'


class Formulario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_eventoid = models.ForeignKey('TipoDeEvento', models.DO_NOTHING, db_column='Tipo de EventoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_de_formularioid = models.ForeignKey('TipoDeFormulario', models.DO_NOTHING, db_column='Tipo de FormularioID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'formulario'


class Inscricao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    requer_certificado = models.IntegerField(db_column='Requer Certificado', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    presenca = models.IntegerField(db_column='Presenca', blank=True, null=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    participanteutilizadorid = models.ForeignKey('Participante', models.DO_NOTHING, db_column='ParticipanteUtilizadorID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'inscricao'


class Logistica(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_inicio = models.TimeField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duracao = models.IntegerField(db_column='Duracao', blank=True, null=True)  # Field name made lowercase.
    valido = models.TextField(db_column='Valido', blank=True, null=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    tipo_equipamentoid = models.ForeignKey('TipoEquipamento', models.DO_NOTHING, db_column='Tipo_EquipamentoID', blank=True, null=True)  # Field name made lowercase.
    tipo_servicoid = models.ForeignKey('TipoServico', models.DO_NOTHING, db_column='Tipo_ServicoID', blank=True, null=True)  # Field name made lowercase.
    tipos_de_recursosid = models.ForeignKey('TiposDeRecursos', models.DO_NOTHING, db_column='Tipos de recursosID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'logistica'


class Notificacoes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    criadoem = models.IntegerField(db_column='CriadoEm', blank=True, null=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'notificacoes'


class Opcoes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    perguntaid = models.ForeignKey('Pergunta', models.DO_NOTHING, db_column='PerguntaID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'opcoes'


class Participante(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.

    def __str__(self):
        return self.utilizadorid.nome
    

    class Meta:
        managed = True
        db_table = 'participante'


class Pergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    formularioid = models.ForeignKey(Formulario, models.DO_NOTHING, db_column='FormularioID')  # Field name made lowercase.
    tipo_de_perguntaid = models.ForeignKey('TipoDePergunta', models.DO_NOTHING, db_column='Tipo de PerguntaID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'pergunta'


class PeriodoEquipamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_inicio = models.TimeField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duracao = models.IntegerField(db_column='Duracao', blank=True, null=True)  # Field name made lowercase.
    equipamentoid = models.ForeignKey(Equipamento, models.DO_NOTHING, db_column='EquipamentoID')  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'periodo_equipamento'


class PeriodoSala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_inicio = models.TimeField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duracao = models.IntegerField(db_column='Duracao')  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    salaid = models.ForeignKey('Sala', models.DO_NOTHING, db_column='SalaID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'periodo_sala'


class PeriodoServico(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_de_inicio = models.TimeField(db_column='Hora de inicio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duracao = models.IntegerField(db_column='Duracao', blank=True, null=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    servicosid = models.ForeignKey('Servicos', models.DO_NOTHING, db_column='ServicosID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'periodo_servico'


class Proponente(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'proponente'


class Respostas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    inscricaoid = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='InscricaoID')  # Field name made lowercase.
    opcoesid = models.ForeignKey(Opcoes, models.DO_NOTHING, db_column='OpcoesID')  # Field name made lowercase.
    perguntaid = models.ForeignKey(Pergunta, models.DO_NOTHING, db_column='PerguntaID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'respostas'


class Sala(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade')  # Field name made lowercase.
    fotos = models.IntegerField(db_column='Fotos', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobilidade_reduzida = models.IntegerField(db_column='Mobilidade reduzida')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    edificioid = models.ForeignKey(Edificio, models.DO_NOTHING, db_column='EdificioID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'sala'


class Servicos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    preco_base = models.FloatField(db_column='Preco base')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_servicoid = models.ForeignKey('TipoServico', models.DO_NOTHING, db_column='Tipo_ServicoID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'servicos'


class TipoDeEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo de evento'


class TipoDeFormulario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo de formulario'


class TipoDePergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tipo de pergunta'


class TipoEquipamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_equipamento'


class TipoServico(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_servico'


class TiposDeRecursos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_recurso = models.IntegerField(db_column='Tipo de recurso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'tipos de recursos'


class Utilizador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numero_telefone = models.CharField(db_column='Numero telefone', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    interno = models.IntegerField(db_column='Interno', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'utilizador'
