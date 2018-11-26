from django.contrib import admin
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse
from django.utils.translation import ugettext
from django.conf.urls import url
from django.utils.six import print_
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from . import models


class TokenInline(admin.TabularInline):
    fields = ('token_type', 'expires_in', 'access_token', 'refresh_token')
    readonly_fields = fields
    extra = 0
    model = models.AccessToken


class ClientAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'client_id', 'authorization_endpoint', 'token_endpoint',
        'creator', 'created', 'modified')
    fields = ('uid', 'name', 'client_id', 'client_secret', 'authorization_endpoint',
        'token_endpoint', 'creator', 'created', 'modified', 'complete_authorization_url')
    readonly_fields = ('uid', 'creator', 'created', 'modified', 'complete_authorization_url')
    inlines = [TokenInline]

    def complete_authorization_url_name(self):
        info = self.model._meta.app_label, self.model._meta.model_name
        return 'admin:%s_%s_complete_authorization' % info

    def complete_authorization_url(self, obj):
        name = self.complete_authorization_url_name()
        return reverse(name, args=(obj.uid,))

    def get_urls(self):
        urls = super(ClientAdmin, self).get_urls()
        print(urls)
        info = self.model._meta.app_label, self.model._meta.model_name
        my_urls = [
            url(r'^(.+)/complete-authorization/$', self.complete_authorization, name='%s_%s_complete_authorization' % info),
        ]
        return my_urls + urls

    def complete_authorization(self, request, uid):
        "View to complete oauth2 authorization"
        client = get_object_or_404(models.Client, uid=uid)
        redirect_url = self.complete_authorization_url(client)
        redirect_url = request.build_absolute_uri(redirect_url)
        client.complete_authorization(request, redirect_url)
        msg = ugettext("Oauth client authorized.")
        self.message_user(request, msg, messages.INFO)
        url_name = 'admin:{}_{}_change'.format(self.model._meta.app_label, self.model._meta.model_name)
        return redirect(url_name, client.pk)

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.creator = request.user
        super(ClientAdmin, self).save_model(request, obj, form, change)

    def response_change(self, request, obj):
        if '_authorize-client' in request.POST:
            redirect_url = self.complete_authorization_url(obj)
            redirect_url = request.build_absolute_uri(redirect_url)
            authorization_url = obj.start_authorization_url(request, redirect_url)
            return redirect(authorization_url)
        return super(ClientAdmin, self).response_change(request, obj)


admin.site.register(models.Client, ClientAdmin)