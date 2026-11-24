import smtplib
from email.message import EmailMessage

import config


def envoyer(destinataire, nom, prenom, message, fichier=None):
    msg = EmailMessage()
    msg["From"] = config.EMAIL
    msg["To"] = destinataire
    msg["Subject"] = f"Bonjour {prenom} {nom}"
    msg.set_content(f"Bonjour {prenom} {nom},\n\n{message}")

    if fichier:
        with open(fichier, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=fichier,
            )

    with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT, timeout=30) as smtp:
        smtp.login(config.EMAIL, config.PASSWORD)
        smtp.send_message(msg)
    return True
