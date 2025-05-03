import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app


def test_welcome_root():
    assert app.welcome_root() == {"message": "Welcome to the ML API"}
