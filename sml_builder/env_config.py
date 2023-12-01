class EnvConfig:
    ENVIRONMENT_GA_CODE = {
        "dev": "placeholder-dev-code",
        "preprod": "placeholder-preprod-code",
        "prod": "placeholder-prod-code",
    }

    @staticmethod
    def get_environment_ga_code(environment):
        return EnvConfig.ENVIRONMENT_GA_CODE.get(environment, "placeholder-default")
