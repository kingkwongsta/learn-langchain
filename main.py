import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    print(OPENAI_API_KEY)
    pass
if __name__ == "__main__":
    main()