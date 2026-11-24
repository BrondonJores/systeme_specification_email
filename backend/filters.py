"""Filtres, archivage et alerte (un seul rôle : traiter les mails lus)."""
import os
import re

import config
from backend.sender import envoyer


def filtrer(mails, expediteur=None, sujet_contient=None, motif=None):
    """Filtre une liste de mails. Critères optionnels et cumulables."""
    resultats = []
    for mail in mails:
        if expediteur and expediteur.lower() not in mail["expediteur"].lower():
            continue
        if sujet_contient and sujet_contient.lower() not in mail["sujet"].lower():
            continue
        if motif and not re.search(motif, mail["corps"], re.IGNORECASE):
            continue
        resultats.append(mail)
    return resultats


def archiver(mail, categorie):
    """Sauvegarde un mail en .txt dans archives/<categorie>/."""
    dossier = os.path.join(config.ARCHIVE_DIR, categorie)
    os.makedirs(dossier, exist_ok=True)
    nom = re.sub(r"[^\w\-]", "_", mail["sujet"][:30]) or "sans_sujet"
    chemin = os.path.join(dossier, f"{nom}.txt")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(
            f"De : {mail['expediteur']}\n"
            f"Sujet : {mail['sujet']}\n"
            f"Date : {mail['date']}\n\n{mail['corps']}"
        )
    return chemin


def alerter_si_mot_cle(mails, mot_cle, destinataire):
    """Envoie une alerte mail si mot_cle trouvé. Retourne le nb d'alertes."""
    alertes = 0
    for mail in mails:
        if re.search(mot_cle, mail["sujet"] + mail["corps"], re.IGNORECASE):
            envoyer(
                destinataire,
                "Système",
                "Alerte",
                f"Mot-clé '{mot_cle}' trouvé dans : {mail['sujet']}",
            )
            alertes += 1
    return alertes
