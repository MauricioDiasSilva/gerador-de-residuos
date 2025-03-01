
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model

class Usuario(AbstractUser):
    pontos = models.IntegerField(default=0)
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    

class Residuo(models.Model):
    TIPO_CHOICES = [
        ('O', 'Orgânico'),
        ('R', 'Reciclável'),
        ('N', 'Não Reciclável'),
        ('L', 'Latinha'),
        ('F', 'Ferro'),
        ('P', 'Papelão'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    quantidade = models.FloatField()
    data_registro = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    @property
    def pontos(self):
        if self.tipo == 'R':
            return self.quantidade * 10
        elif self.tipo == 'L':
            return self.quantidade * 15
        elif self.tipo == 'F':
            return self.quantidade * 20
        elif self.tipo == 'P':
            return self.quantidade * 5
        else:
            return self.quantidade * 5


# residuos/models.py
class Coleta(models.Model):
    residuo = models.ForeignKey(Residuo, on_delete=models.CASCADE)
    data_coleta = models.DateTimeField()
    localizacao = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.residuo.usuario.pontos += self.residuo.pontos
        self.residuo.usuario.save()


# residuos/models.py
class Recompensa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    pontos_necessarios = models.IntegerField()
    empresa = models.CharField(max_length=255, blank=True, null=True)
    imagem = models.ImageField(upload_to='recompensas/', blank=True, null=True)  # Novo campo

    def __str__(self):
        return self.nome



