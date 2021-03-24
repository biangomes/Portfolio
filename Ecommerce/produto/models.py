from django.db import models
from django.conf import settings
import os

# Import de terceiros
from PIL import Image


# Tipos: V - variável, S - simples
opcoes = (
    ('V', 'Variavel'),
    ('S', 'Simples'),
)


# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField()
    tipo = models.CharField(choices=opcoes, default='V', max_length=1)

    # Metodo que redimensiona imagem
    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            print('retornando, largura original menor q nova largura')
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0.0)
    estoque = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variacao'
        verbose_name_plural = 'Variacoes'