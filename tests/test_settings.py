import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from settings import Settings

load_dotenv(".env.test")


def test_settings():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ML_OPS_TEST"
    assert settings.API_KEY == "1234mykey56789"
