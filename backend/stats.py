from collections import Counter


def repartition_expediteurs(mails, top=5):
    compteur = Counter(m["expediteur"] for m in mails)
    plus_frequents = compteur.most_common(top)
    labels = [exp[:30] for exp, _ in plus_frequents]
    valeurs = [nb for _, nb in plus_frequents]
    reste = sum(compteur.values()) - sum(valeurs)
    if reste:
        labels.append("Autres")
        valeurs.append(reste)
    return labels, valeurs
