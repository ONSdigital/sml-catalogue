class EnvConfig:
    ENVIRONMENT_GA_CODE = {
        "dev": "4e1D59Ur2Qp1tABXx",
        "preprod": "v9By2ndgSQ5Jx7abY30mxw",
        "prod": "ETsGJBpGMS4CXqLVsXqy",
    }

    @staticmethod
    def get_environment_ga_code(environment):
        return EnvConfig.ENVIRONMENT_GA_CODE.get(environment, "placeholder-default")
