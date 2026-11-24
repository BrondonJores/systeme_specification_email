import os


def _load_dotenv():
    try:
        with open(".env", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if not ligne or ligne.startswith("#") or "=" not in ligne:
                    continue
                cle, valeur = ligne.split("=", 1)
                os.environ.setdefault(cle.strip(), valeur.strip().strip("'\""))
    except FileNotFoundError:
        pass


_load_dotenv()

EMAIL = os.getenv("EMAIL_USER", "etudiant.test@gmail.com")
PASSWORD = os.getenv("EMAIL_PASSWORD", "xxxx xxxx xxxx xxxx")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
IMAP_HOST = "imap.gmail.com"

ARCHIVE_DIR = "archives"
