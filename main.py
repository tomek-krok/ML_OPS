import argparse
from dotenv import load_dotenv
from settings import Settings

import yaml
import os


def export_envs(environment: str = "dev") -> None:
    exist = load_dotenv(".env." + environment)

    print(f"my env exist is {exist}")

    if not exist:
        raise Exception(f"Environment file .env.{environment} does not exist")


def import_yaml():
    with open("secrets.yaml", "r") as f:
        secrets = yaml.safe_load(f)

    for key, value in secrets.items():
        print(key, value)
        os.environ[key] = value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    secrets = import_yaml()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
