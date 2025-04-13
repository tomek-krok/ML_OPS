from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @validator("environment")
    def validate_environment(cls, value):
        # implement me!
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)

        value = "ZERO"

        # add implementation here !!! now we will jump to lab 02

        return value
