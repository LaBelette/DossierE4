from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    homme = 'homme'
    femme = 'femme'
    all = 'all'

    GENRE_CHOICES = (
        (homme, 'Homme étrange'),
        (femme, 'Femme étrange'),
    )
    PREFERENCES_CHOICES = (
        (homme, 'Homme'),
        (femme, 'Femme'),
        (all, 'Peu importe'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    genre = models.CharField(choices=GENRE_CHOICES, max_length=255)
    preference = models.CharField(choices=PREFERENCES_CHOICES, max_length=255)
    def __str__(self):
        return 'Profil de {}'.format(self.user)


class Strangething(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='strangething')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def numb_of_like(self):
        likes = Like.objects.filter(strangething=self)
        return len(likes)

    def __str__(self):
        return 'Chose étrange de {} --- {} --- {}'.format(self.user, self.title, self.date)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    strangething = models.ForeignKey(Strangething, on_delete=models.CASCADE, related_name='like')

    class Meta:
        unique_together = (('user', 'strangething'),)
        index_together = (('user', 'strangething'),)

    def __str__(self):
        return 'Like de {} sur {}'.format(self.user, self.strangething)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    strangething = models.ForeignKey(Strangething, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'strangething','text'),)
        index_together = (('user', 'strangething', 'text'),)

    def __str__(self):
        return 'Commentaire de {} sur {} le {}'.format(self.user, self.strangething, self.date)
