# -*- coding: utf-8 -*-

import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Client(TimeStampedModel):
    uid = models.UUIDField(_("UID"), default=uuid.uuid4, unique=True)
    name = models.CharField(_("Name"), max_length=100, unique=True)
    client_id = models.CharField(_("Client id"), max_length=255, unique=True)
    client_secret = models.CharField(_("Client secret"), max_length=255)
    authorization_endpoint = models.URLField(_("Authorization endpoint"), max_length=255)
    token_endpoint = models.URLField(_("Token endpoint"), max_length=255, blank=True, default='')

    class Meta:
        verbose_name = _("Oauth2 client")
        verbose_name_plural = _("Oauth2 clients")


class AccessToken(TimeStampedModel):
    client = models.ForeignKey(Client, verbose_name=_("Client"))
    token_type = models.CharField(_("Token type"), max_length=255)
    expires_in = models.IntegerField(_("Expires in"))
    access_token = models.CharField(_("Access token"), max_length=255)
    refresh_token = models.CharField(_("Refresh token"), max_length=255)
    
    class Meta:
        verbose_name = _("Access token")
        verbose_name_plural = _("Access tokens")    
