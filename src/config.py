import os
import dotenv

dotenv.load_dotenv()

NAME = 'Hangman CLI'
PROGRAMING_LANGUAGE = "Python"
VERSION = 'v0.3'
AUTHOR = 'Rupnil Codes'

ONBOARDING = False
# LOCAL_DATABASE = False


SECRET_KEY = os.getenv('SECRET_KEY')
SECRET_KEY_BYTES = bytes(SECRET_KEY, 'utf-8')
