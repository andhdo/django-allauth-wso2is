# -*- coding: utf-8 -*-
import requests
import logging

from allauth.socialaccount import app_settings
from allauth_wso2is.provider import Wso2isProvider
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)
from allauth_wso2is.utils import import_from_settings

# Get an instance of a logger
logger = logging.getLogger(__name__)

class Wso2isOAuth2Adapter(OAuth2Adapter):
    provider_id = Wso2isProvider.id
    supports_state = True

    settings = app_settings.PROVIDERS.get(provider_id, {})
    provider_base_url = settings.get("WSO2_URL")

    access_token_url = '{0}/oauth2/token'.format(provider_base_url)
    authorize_url = '{0}/oauth2/authorize'.format(provider_base_url)
    profile_url = '{0}/oauth2/userinfo?schema=openid'.format(provider_base_url)


    def complete_login(self, request, app, token, response):
        verify_ssl = import_from_settings('WSO2IS_VERIFY_SSL', True)        
        extra_data = dict()
        try:
            extra_data = requests.get(
                self.profile_url, 
                params={
                    'access_token': token.token
                },
                verify=verify_ssl
            ).json()
        except Exception as e:
            logger.error('> complete_login error(2) %s'%(e))

        extra_data = {
            'user_id': extra_data['sub'],
            'id': extra_data['sub'],
            'name': extra_data['sub'],
            'email': extra_data['email']
        }

        return self.get_provider().sociallogin_from_response(
            request,
            extra_data
        )

oauth2_login = OAuth2LoginView.adapter_view(Wso2isOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(Wso2isOAuth2Adapter)
