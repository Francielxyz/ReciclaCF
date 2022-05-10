from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Estado")
    uf = models.CharField(max_length=2, unique=True, verbose_name="UF")

    def __str__(self):
        return "{} - {}".format(self.nome, self.uf)

class Cidade(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Cidade")
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.nome, self.estado.uf)

class Perfil(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    data_nascimento = models.DateField(verbose_name="Data Nascimento")
    telefone1 = models.CharField(max_length=15, verbose_name="Telefone 1")
    telefone2 = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefone 2")
    email = models.EmailField(max_length=80, verbose_name="Email")
    observacao = models.CharField(max_length=255, blank=True, null=True, verbose_name="Observação")
    data_cadastro = models.DateTimeField(verbose_name="Data Cadastro")
    status = models.CharField(max_length=1, default="A")

    def __str__(self):
        return "{}".format(self.nome)

class Categoria(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Categoria")
    observacao = models.CharField(max_length=255, blank=True, null=True, verbose_name="Observação")
    data_cadastro = models.DateTimeField(verbose_name="Data Cadastro")
    status = models.CharField(max_length=1, default="A")

    def __str__(self):
        return "Categoria - {}".format(self.nome)

class Endereco_Armazenamento(models.Model):
    cep = models.IntegerField(verbose_name="CEP")
    bairro = models.CharField(max_length=150, verbose_name="Bairro")
    rua = models.CharField(max_length=50, verbose_name="Rua")
    numero = models.IntegerField(verbose_name="Nº")
    endereco_compartilhado = models.BooleanField(
        verbose_name="Endereço Compartilhado?", help_text="Este endereço será compartilhado para outros usuários")
    observacao = models.CharField(max_length=255, blank=True, null=True, verbose_name="Observação")
    data_cadastro = models.DateTimeField(verbose_name="Data Cadastro")
    status = models.CharField(max_length=1, default="A")

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "Rua: {}, {} - {}".format(self.rua, self.cidade.nome, self.cidade.estado.uf)

class Endereco_Armazenamento_Categoria(models.Model):
    endereco_armazenamento = models.ForeignKey(Endereco_Armazenamento, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return "CEP {} - Cidade {} - Categoria {}".format(
            self.endereco_armazenamento.cep, self.endereco_armazenamento.cidade.nome, self.categoria.nome)

class Item_Descartavel(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Item")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    observacao = models.CharField(max_length=255, blank=True, null=True, verbose_name="Observação")
    data_cadastro = models.DateTimeField(verbose_name="Data Cadastro")

    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    endereco_armazenamento = models.ForeignKey(Endereco_Armazenamento, on_delete=models.PROTECT)

    def __str__(self):
        return "{} com {} unidades na categoria {} e o responsavel é {}".format(
            self.nome, self.quantidade, self.categoria.nome, self.perfil.nome)