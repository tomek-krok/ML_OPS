from pydantic_settings import BaseSettings
from pydantic import field_validator, ValidationError


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT")
    def validate_environment(value):
        #     # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        env_variables = ["dev", "test", "prod"]

        if value in env_variables:
            return value
        else:
            raise ValidationError()
