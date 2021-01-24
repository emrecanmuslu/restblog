from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_to_posts',
        null=False,
        blank=False,
        verbose_name='Kullanıcı'
    )
    title = models.CharField(
        null=False,
        blank=False,
        max_length=50,
        verbose_name='Başlık'
    )
    content = models.TextField(
        null=False,
        blank=False,
        verbose_name='İçerik'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Eklenme Tarihi'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'
        ordering = ['-created_at']