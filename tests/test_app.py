# tests/test_app.py
from src.utils import greet

def test_greet():
    assert greet("Tester") == "Hello, Tester!"
