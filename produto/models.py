import os

from django.conf import settings
from django.db import models
from PIL import Image


# Create your models here.
class Produto(models.Model):
    
    nome = models.CharField(max_length=200)
    descrisao_curta = models.TextField(max_length=200)
    descrisao_longa = models.TextField()
    imagem = models.ImageField(upload_to ='produto-imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0) 
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variações'),
            ('S', 'Simples'),
        )
    )


    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        
        if original_width <= new_width:
            img_pil.close()
            return 
            
        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality = 50,
        )




    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome
    