=====
django-allauth-wso2is
=====

Client connector module to work with wso2is.
Detailed documentation is in the "docs" directory.

Quick start
-----------

0. This module requires django-allauth prerrequisite

1. Add "allauth_wso2is" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'allauth_wso2is',
    ]

	Then customize the allauth provider: 

    ```
    WSO2IS_VERIFY_SSL=False
    OAUTH2_VERIFY_SSL=False
    ACCOUNT_EMAIL_VERIFICATION = 'none'
    ```
    and
    ```
    # Provider specific settings
    SOCIALACCOUNT_PROVIDERS = {
        'wso2is': {
            'WSO2_URL': 'https://wso2is.local:9443',
            'APP': {
                'client_id': 'XXXXXXX',
                'secret': 'YYYYYYYY',
                'key': ''
            }
        }
    }

    ```


2. urlconf changes: not needed

3. migrate changes: not needed 

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a site (you'll need the Admin app enabled).

   Then add the created site id to the settings.py file
    ```
    SITE_ID = 1
    ```


5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.