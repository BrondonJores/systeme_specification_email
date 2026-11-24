import os

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL_USER", "etudiant.test@gmail.com")
PASSWORD = os.getenv("EMAIL_PASSWORD", "xxxx xxxx xxxx xxxx")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
IMAP_HOST = "imap.gmail.com"

ARCHIVE_DIR = "archives"
