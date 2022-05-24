# Generated by Django 4.0.4 on 2022-05-23 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Categoria')),
                ('observacao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Observação')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')),
                ('status', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco_Armazenamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField(verbose_name='CEP')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('rua', models.CharField(max_length=50, verbose_name='Rua')),
                ('numero', models.IntegerField(verbose_name='Nº')),
                ('endereco_compartilhado', models.BooleanField(help_text='Este endereço será compartilhado para outros usuários', verbose_name='Endereço Compartilhado?')),
                ('observacao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Observação')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')),
                ('status', models.CharField(default='A', max_length=1)),
                ('categoria', models.ManyToManyField(to='cadastro.categoria')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Estado')),
                ('uf', models.CharField(max_length=2, unique=True, verbose_name='UF')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome Completo')),
                ('data_nascimento', models.DateField(verbose_name='Data Nascimento')),
                ('telefone1', models.CharField(max_length=15, verbose_name='Telefone 1')),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone 2')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('observacao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Observação')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')),
                ('status', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Descartavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Item')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('observacao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Observação')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.categoria')),
                ('endereco_armazenamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.endereco_armazenamento')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.perfil')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.estado'),
        ),
    ]
