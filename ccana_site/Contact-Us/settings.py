INSTALLED_APPS [
    'sendemail.apps.SendemailConfig', # new
    ...
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
