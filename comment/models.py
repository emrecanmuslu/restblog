from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_to_comments',
        null=False,
        blank=False,
        verbose_name='Kullanıcı'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_to_comments',
        null=False,
        blank=False,
        verbose_name='Makale'
    )
    content = models.TextField(
        null=False,
        blank=False,
        verbose_name='Yorum'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='parent_to_comment',
        null=True,
        blank=True,
        verbose_name='Yorum'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Yorum Tarihi'
    )

    def __str__(self):
        return self.content + " " + self.user.username

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def any_children(self):
        return Comment.objects.filter(parent=self).exists()

    class Meta:
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
        ordering = ['-created_at']
