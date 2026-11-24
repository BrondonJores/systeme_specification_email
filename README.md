# systeme_specification_email

Mini-système d'automatisation d'e-mails en Python (TP étudiant, ~1h40).
Interface Dash, logique mail en stdlib (`smtplib`, `imaplib`).

## Lancer le projet

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
EMAIL_USER="moi@gmail.com" EMAIL_PASSWORD="xxxx xxxx xxxx xxxx" python app.py
```

Puis ouvrir http://127.0.0.1:8050 dans le navigateur.

## Structure (SOLID light)

- `config.py` : identifiants et serveurs (un seul endroit).
- `backend/sender.py` : envoi de mails (S : un seul rôle).
- `backend/reader.py` : lecture des derniers mails.
- `backend/filters.py` : filtre, archivage, alerte mot-clé.
- `backend/stats.py` : stats pour les graphiques.
- `assets/style.css` : CSS du dashboard (chargé auto par Dash).
- `frontend/shell.py` : header, navbar et bouton Actualiser.
- `frontend/router.py` : 1 URL = 1 page.
- `frontend/pages/` : une page par section, chacune avec son layout et ses callbacks.
- `app.py` : assemble front + back.
