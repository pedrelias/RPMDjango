from pyexpat import model
import site
from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=100)
    continente = models.CharField(max_length=100)
    codigo_iso = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return f'{self.nome} - {self.continente} - {self.codigo_iso}'
    

class Cidades(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return f'{self.nome} - {self.pais}'
    
class Circuito(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Circuito'
        verbose_name_plural = 'Circuitos'

    def __str__(self):
        return f'{self.nome} - {self.pais} - {self.cidade}'

class CategoriaAutomobilismo(models.Model):
    nome = models.CharField(max_length=100)
    site_oficial = models.URLField()

    class Meta:
        verbose_name = 'Categoria do Automobilismo'
        verbose_name_plural = 'Categorias do Automobilismo'

    def __str__(self):
        return f'{self.nome} - {self.site_oficial}'
    
class Corrida(models.Model):
    nome = models.CharField(max_length=100)
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    numero_voltas = models.IntegerField()
    categoria = models.ForeignKey(CategoriaAutomobilismo, on_delete=models.CASCADE)
    vencedor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Corrida'
        verbose_name_plural = 'Corridas'

    def __str__(self):
        return f'{self.nome} - {self.circuito} - {self.numero_voltas} - {self.categoria} - {self.vencedor}'
    

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    fundacao = models.IntegerField()
    site_oficial = models.URLField()

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return f'{self.nome} - {self.pais} - {self.fundacao} - {self.site_oficial}'

class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    podios = models.IntegerField()
    pole_positions = models.IntegerField()
    vitorias = models.IntegerField()

    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural = 'Pilotos'

    def __str__(self):
        return f'{self.nome} - {self.equipe} - {self.pais} - {self.podios} - {self.pole_positions} - {self.vitorias}'
    

class Montadora(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    fundacao = models.IntegerField()
    site_oficial = models.URLField()

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return f'{self.nome} - {self.cidade} - {self.pais} - {self.fundacao} - {self.site_oficial}'

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE, related_name='carros')
    motor = models.CharField(max_length=100)
    peso = models.IntegerField()
    potencia = models.IntegerField()
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.modelo} - {self.ano} - {self.equipe} - {self.piloto} - {self.motor} - {self.peso} - {self.potencia} - {self.montadora}'

class Calendario(models.Model):
    corrida = models.ForeignKey(Corrida, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        verbose_name = 'Calendario'

    def __str__(self):
        return f'{self.corrida} - {self.data} - {self.hora}'

class Pontuacao(models.Model):
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    corrida = models.ForeignKey(Corrida, on_delete=models.CASCADE)
    posicao = models.IntegerField()
    pontos = models.IntegerField()

    class Meta:
        verbose_name = 'Pontuacao'

    def __str__(self):
        return f'{self.piloto} - {self.corrida} - {self.posicao} - {self.pontos}'



class CanalTransmissao(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    site_oficial = models.URLField()

    class Meta:
        verbose_name = 'Canal de Transmissao'
        verbose_name_plural = 'Canais de Transmissao'

    def __str__(self):
        return f'{self.nome} - {self.pais} - {self.site_oficial}'

class Transmissao(models.Model):
    corrida = models.ForeignKey(Corrida, on_delete=models.CASCADE)
    canal = models.ForeignKey(CanalTransmissao, on_delete=models.CASCADE)
    horario_inicio = models.DateTimeField()

    class Meta:
        verbose_name = 'Transmissao'
        verbose_name_plural = 'Transmissoes'

    def __str__(self):
        return f'{self.corrida} - {self.canal} - {self.horario_inicio}'



