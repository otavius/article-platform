import re
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from app.managers import UserProfileManager
# Create your models here.

ARTICLE_STATUS = (("draft", "draft"), ("inprogress", "in progress"), ("published", "published"),)

class UserProfile(AbstractUser):
    email = models.EmailField(_("email address"), max_length=255, unique=True)
    objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Article(models.Model):
    class Meta: 
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    title = models.CharField(_("Title"),max_length=100)
    content = models.TextField(_("Content"),blank=True, default="")
    word_count = models.IntegerField(_("Word count"),blank=True, default="")
    twitter_post = models.TextField(_("Twitter Post"),blank=True, default="")
    status = models.CharField(_("Status"),max_length=20, choices=ARTICLE_STATUS,default="draft")
    created_at = models.DateTimeField(_("Created at"),auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"),auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("creator"), on_delete=models.CASCADE, related_name="article")
    


    def save(self,*args, **kwargs):
        text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)