import logging

from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

from allauth_wso2is.utils import import_from_settings
import urllib3


#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Suppress only the single warning from urllib3 needed.
#requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# import ssl
# print('openssl=%s'%(ssl.OPENSSL_VERSION))
# Get an instance of a logger

logger = logging.getLogger(__name__)
verify_ssl = import_from_settings('WSO2IS_VERIFY_SSL', True)
logger.debug('> wso2is: verify_ssl=%s' % verify_ssl)

if ( not verify_ssl  ):
	urllib3.disable_warnings()

class Wso2isAccount(ProviderAccount):
	
	def to_str(self):
		dflt = super(Wso2isAccount, self).to_str()
		return self.account.extra_data.get('name', dflt)


class Wso2isProvider(OAuth2Provider):
	id = 'wso2is'
	name = 'Wso2-IdentityServer'
	account_class = Wso2isAccount

	def get_default_scope(self):
		return ['openid', 'email', 'name']

	def extract_uid(self, data):
		return str(data['id'])

	def extract_common_fields(self, data):
		return dict(
			email=data.get('email'),
			username=data.get('username'),
			name=data.get('name'),
			user_id=data.get('user_id'),
			# picture=data.get('picture'),
		)


provider_classes = [Wso2isProvider]