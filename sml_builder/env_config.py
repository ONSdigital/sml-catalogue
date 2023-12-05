class EnvConfig:
    ENVIRONMENT_GA_CODE = {
        "dev": "MBGteKWsXZpOgxp0C4pztA",
        "preprod": "v9By2ndgSQ5Jx7abY30mxw",
        "prod": "ETsGJBpGMS4CXqLVsXqy",
    }

    @staticmethod
    def get_environment_ga_code(environment):
        return EnvConfig.ENVIRONMENT_GA_CODE.get(environment, "placeholder-default")
