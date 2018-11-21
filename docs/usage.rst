=====
Usage
=====

To use Django Oauth2 Clients in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'oauth_clients.apps.OauthClientsConfig',
        ...
    )

Add Django Oauth2 Clients's URL patterns:

.. code-block:: python

    from oauth_clients import urls as oauth_clients_urls


    urlpatterns = [
        ...
        url(r'^', include(oauth_clients_urls)),
        ...
    ]
