class EnvConfig:
    ENVIRONMENTS = {
        'dev': 'GTM-DEV-ID',
        'preprod': 'GTM-PREPROD-ID',
        'prod': 'GTM-PROD-ID',
    }

    @staticmethod
    def get_environment_name(environment):
        return EnvConfig.ENVIRONMENTS.get(environment, 'GTM-DEFAULT-ID')
