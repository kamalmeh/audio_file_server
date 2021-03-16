from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Song(models.Model):
    """
    name(string<100)
    duration(integer)
    uploaded(uploaded timestamp)
    """
    name = models.CharField(_("Name"), max_length=100)
    duration = models.IntegerField(_("Duration"))
    uploaded = models.DateTimeField(_("Uploaded"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Song_detail", kwargs={"pk": self.pk})

class Podcast(models.Model):
    """
    name(string<100 chars)
    duration(integer)
    uploaded(uploaded timestamp)
    host(string<100 chars)
    participants(List of participants max 10 items)
    """
    name = models.CharField(_("Name"), max_length=100)
    duration = models.IntegerField(_("Duration"))
    uploaded = models.DateTimeField(_("Uploaded"), auto_now=False, auto_now_add=True)
    host = models.CharField(_("Host"), max_length=100)
    participants = models.CharField(_("Participants"), max_length=1009)

    class Meta:
        verbose_name = _("Podcast")
        verbose_name_plural = _("Podcasts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Podcast_detail", kwargs={"pk": self.pk})

class AudioBook(models.Model):
    """
    title(string<100 chars)
    author(string<100 chars)
    narrator(string<100 chars)
    duration(integer)
    uploaded(uploaded timestamp)
    """
    title = models.CharField(_("Title"), max_length=100)
    author = models.CharField(_("Author"), max_length=100)
    narrator = models.CharField(_("Narrator"), max_length=100)
    duration = models.IntegerField(_("Duration"))
    uploaded = models.DateTimeField(_("Uploaded"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("AudioBook")
        verbose_name_plural = _("AudioBooks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("AudioBook_detail", kwargs={"pk": self.pk})
