"""Lecture des mails (un seul rôle : lire)."""
import imaplib
from email import message_from_bytes
from email.header import decode_header

import config


def _decode(value):
    parts = decode_header(value or "")
    textes = []
    for texte, enc in parts:
        if isinstance(texte, bytes):
            textes.append(texte.decode(enc or "utf-8", errors="ignore"))
        else:
            textes.append(texte)
    return "".join(textes)


def lire_derniers(n=5):
    """Retourne les n derniers mails : expediteur, sujet, date, corps."""
    mails = []
    with imaplib.IMAP4_SSL(config.IMAP_HOST) as imap:
        imap.login(config.EMAIL, config.PASSWORD)
        imap.select("INBOX")
        _, ids = imap.search(None, "ALL")
        derniers = ids[0].split()[-n:]
        for num in reversed(derniers):
            _, data = imap.fetch(num, "(RFC822)")
            msg = message_from_bytes(data[0][1])
            corps = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        corps = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                brut = msg.get_payload(decode=True)
                corps = brut.decode(errors="ignore") if brut else str(msg.get_payload())
            mails.append(
                {
                    "expediteur": _decode(msg.get("From")),
                    "sujet": _decode(msg.get("Subject")),
                    "date": msg.get("Date", ""),
                    "corps": corps[:500],
                }
            )
    return mails
