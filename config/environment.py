ENVIRONMENT = 'local'
SETTINGS_MODULE = 'config.settings.local'

if ENVIRONMENT == 'local':
    SETTINGS_MODULE = 'config.settings.local'

if ENVIRONMENT == 'prod':
    SETTINGS_MODULE = 'config.settings.production'