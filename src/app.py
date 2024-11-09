# src/app.py
from src.utils import greet

def main():
    print("Starting the application...")
    message = greet("World")
    print(message)

if __name__ == "__main__":
    main()
