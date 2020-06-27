# -*- coding: utf-8 -*-
from allauth_wso2is.provider import Wso2isProvider
from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase


class Wso2isTests(OAuth2TestsMixin, TestCase):
    provider_id = Wso2isProvider.id

    def get_mocked_response(self):
        return MockedResponse(200, """
            {
                "email": "admin@wso2.com",
                "id": 2,
                "sub": 2,
                "identities": [],
                "name": "Mr Bob"
            }
        """)
