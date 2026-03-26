# Formation Odoo 18 — Gestion des Employés, Départements et Contrats

**Public cible** : Responsables RH, Assistants RH, Gestionnaires de paie
**Niveau** : Débutant à intermédiaire
**Durée estimée** : 1 journée (7h)
**Prérequis** : Savoir naviguer dans Odoo (menus, formulaires, filtres)

---

## Objectifs de la formation

À l'issue de cette formation, le stagiaire sera capable de :

- Créer et organiser la structure hiérarchique des départements
- Créer et gérer les fiches employés complètes
- Établir et suivre les contrats de travail
- Utiliser les filtres, regroupements et vues pour analyser les données RH
- Archiver, réactiver et corriger des enregistrements

---

## Plan de la journée

| Heure       | Module                              |
|-------------|-------------------------------------|
| 09h00–09h30 | Présentation de l'interface RH      |
| 09h30–11h00 | Module 1 — Les départements         |
| 11h00–12h30 | Module 2 — Les employés             |
| 12h30–13h30 | Pause déjeuner                      |
| 13h30–15h30 | Module 3 — Les contrats             |
| 15h30–16h30 | Module 4 — Recherche et rapports    |
| 16h30–17h00 | Exercice de synthèse + Q&A          |

---

## Présentation de l'interface RH

### Accéder au module Employés

Depuis le menu principal d'Odoo 18 :

1. Cliquer sur l'icône **grille d'applications** (en haut à gauche)
2. Sélectionner **Employés**

Le module s'ouvre sur la liste de vos employés en vue **Kanban** (cartes).

### Les vues disponibles

En haut à droite de chaque liste, des icônes permettent de changer de vue :

| Icône | Vue      | Utilisation                                 |
|-------|----------|---------------------------------------------|
| ☰     | Liste    | Voir plusieurs enregistrements en tableau   |
| ⊞     | Kanban   | Vue par cartes (défaut pour les employés)   |
| 📊    | Graphique| Analyse visuelle (histogramme, camembert)   |
| 📅    | Calendrier| Planification (absences, entretiens)       |

### Le menu de configuration RH

Aller dans **Employés > Configuration** pour accéder à :

- **Départements** — structure de l'entreprise
- **Postes** — intitulés de fonction
- **Types de contrats** — CDI, CDD, Stage, etc.
- **Plans d'activités** — modèles de suivi RH

---

## Module 1 — Les Départements

### Qu'est-ce qu'un département dans Odoo ?

Un département regroupe des employés autour d'une même fonction dans l'entreprise (ex : Comptabilité, Informatique, Commercial). Odoo permet de créer une hiérarchie : un département peut avoir des sous-départements.

**Exemple de structure** :
```
Entreprise ABC
├── Direction Générale
├── Finance
│   ├── Comptabilité
│   └── Contrôle de gestion
└── Technique
    ├── Développement
    └── Infrastructure
```

---

### 1.1 Créer un département

**Chemin** : Employés > Configuration > Départements > **Nouveau**

| Champ              | Description                                              | Obligatoire |
|--------------------|----------------------------------------------------------|-------------|
| Nom                | Intitulé du département                                  | Oui         |
| Responsable        | L'employé qui dirige ce département                      | Non         |
| Département parent | Pour créer une hiérarchie (sous-département)             | Non         |
| Société            | La société à laquelle appartient ce département          | Oui (auto)  |

**Étapes** :

1. Aller dans **Employés > Configuration > Départements**
2. Cliquer sur **Nouveau**
3. Saisir le **Nom** du département
4. (Optionnel) Sélectionner un **Responsable** parmi les employés existants
5. (Optionnel) Choisir un **Département parent** si c'est un sous-département
6. Cliquer sur **Enregistrer**

> **Remarque** : Le responsable d'un département doit être un employé déjà créé dans Odoo. Si vous créez les départements avant les employés, laissez ce champ vide et revenez-y ensuite.

---

### 1.2 Modifier un département

1. Aller dans **Employés > Configuration > Départements**
2. Cliquer sur le département à modifier
3. Modifier les champs souhaités
4. Cliquer sur **Enregistrer**

---

### 1.3 Archiver un département

Archiver permet de désactiver un département sans le supprimer (les données historiques sont conservées).

1. Ouvrir le département
2. Cliquer sur le menu **Action** (⚙️ engrenage) > **Archiver**
3. Confirmer dans la fenêtre de dialogue

Pour voir les départements archivés : activer le filtre **Archivé** dans la barre de recherche.

---

### 1.4 Voir les employés d'un département

Depuis la fiche d'un département :

- Le bouton **Employés** (en haut à droite de la fiche) indique le nombre d'employés et permet d'accéder directement à leur liste.

---

### Exercice 1 — Créer la structure de l'entreprise

> **Durée** : 20 minutes

Créer les départements suivants pour la société **Formation SA** :

| Département         | Parent              | Responsable (laisser vide) |
|---------------------|---------------------|-----------------------------|
| Direction Générale  | *(aucun)*           |                             |
| Ressources Humaines | Direction Générale  |                             |
| Finance             | Direction Générale  |                             |
| Comptabilité        | Finance             |                             |
| Informatique        | Direction Générale  |                             |
| Développement       | Informatique        |                             |

**Vérification** : Dans la liste des départements, vous devez voir 6 lignes. Le département **Comptabilité** doit afficher **Finance** comme parent.

---

## Module 2 — Les Employés

### Qu'est-ce que la fiche employé ?

La fiche employé centralise toutes les informations d'un collaborateur : identité, poste, coordonnées professionnelles, informations privées, et historique des contrats. Elle est divisée en plusieurs **onglets**.

---

### 2.1 Créer un employé

**Chemin** : Employés > Employés > **Nouveau**

#### Onglet "Informations sur le travail"

C'est l'onglet principal, affiché en premier à l'ouverture de la fiche.

| Champ              | Description                                                  | Obligatoire |
|--------------------|--------------------------------------------------------------|-------------|
| Nom                | Nom complet de l'employé                                     | Oui         |
| Poste              | Fonction officielle (ex : Développeur, Comptable)            | Non         |
| Titre du poste     | Intitulé personnalisé (affiché sur les documents)            | Non         |
| Département        | Département de rattachement                                  | Non         |
| Responsable        | Le manager direct (autre employé Odoo)                       | Non         |
| Coach              | Référent pour l'intégration ou le développement              | Non         |
| Lieu de travail    | Site ou bureau de l'employé                                  | Non         |
| Email professionnel| Adresse email de l'entreprise                                | Non         |
| Téléphone pro      | Numéro de téléphone au bureau                                | Non         |
| Mobile pro         | Numéro de portable professionnel                             | Non         |

#### Onglet "Informations privées"

Contient les données sensibles — **accès réservé aux gestionnaires RH**.

| Champ                 | Description                                       |
|-----------------------|---------------------------------------------------|
| Adresse privée        | Domicile de l'employé (lié au carnet d'adresses) |
| Email privé           | Email personnel                                   |
| Téléphone privé       | Numéro personnel                                  |
| Date de naissance     | Pour calculer l'âge, l'ancienneté                |
| Lieu de naissance     |                                                   |
| Nationalité           |                                                   |
| Numéro d'identification| Numéro de carte d'identité                       |
| Numéro de passeport   |                                                   |
| Genre                 | Homme / Femme / Autre                             |
| Situation familiale   | Célibataire, Marié(e), Divorcé(e)…               |
| Nombre d'enfants à charge |                                               |
| Niveau d'études       | Primaire, Secondaire, Licence, Master, Doctorat  |

#### Onglet "Paramètres RH"

| Champ              | Description                                               |
|--------------------|-----------------------------------------------------------|
| Type d'employé     | Employé / Étudiant / Freelance / Autre                    |
| Utilisateur lié    | Compte Odoo associé (pour se connecter à Odoo)            |
| Fuseau horaire     | Utile pour les équipes internationales                    |
| Coût horaire       | Utilisé dans les feuilles de temps                        |

#### Onglet "CV" (Compétences et Expériences)

Permet d'enregistrer le parcours de l'employé :
- **Expériences** : postes précédents, formations suivies, certifications
- **Compétences** : langues, outils, savoir-faire avec un niveau d'évaluation

---

### 2.2 Étapes de création d'un employé — Pas à pas

1. Aller dans **Employés > Employés**
2. Cliquer sur **Nouveau**
3. Saisir le **Nom** de l'employé (champ en haut, en grand)
4. Ajouter sa **photo** en cliquant sur le cadre image (haut à droite)
5. Renseigner le **Poste**, le **Département**, et le **Responsable**
6. Saisir l'**email professionnel** et le **téléphone**
7. Cliquer sur l'onglet **Informations privées**
8. Renseigner la **date de naissance**, l'**adresse privée**, la **situation familiale**
9. Cliquer sur l'onglet **Paramètres RH**
10. Associer un **utilisateur Odoo** si l'employé doit se connecter
11. Cliquer sur **Enregistrer**

---

### 2.3 Créer un poste de travail

Avant de renseigner le poste d'un employé, il faut que le poste existe dans le référentiel.

**Chemin** : Employés > Configuration > Postes > **Nouveau**

| Champ       | Description                          |
|-------------|--------------------------------------|
| Nom         | Intitulé du poste (ex : Chef de projet) |
| Département | Département concerné                 |
| Description | Description des missions             |

Il est aussi possible de créer un poste **à la volée** directement depuis la fiche employé : cliquer dans le champ **Poste**, taper le nom, puis sélectionner **Créer "..."**.

---

### 2.4 Rechercher et filtrer les employés

La barre de recherche en haut de la liste offre plusieurs options :

**Filtres rapides** :
- **Mon équipe** — uniquement vos subordonnés directs
- **Mes favoris** — employés marqués en favori
- **Archivé** — employés désactivés

**Regroupements** :
- Par **Département**
- Par **Responsable**
- Par **Poste**
- Par **Société**

**Exemple** : Pour voir tous les employés du département Informatique regroupés par poste :
1. Cliquer sur la barre de recherche
2. Sélectionner **Regrouper par > Département**
3. Puis **Regrouper par > Poste**

---

### 2.5 Archiver un employé (départ)

Quand un employé quitte l'entreprise, il ne faut **pas le supprimer** (risque de perte de données historiques). Il faut l'**archiver**.

1. Ouvrir la fiche de l'employé
2. Cliquer sur le menu **Action** (⚙️) > **Archiver**
3. Odoo demande un **motif de départ** :
   - Démission
   - Fin de contrat
   - Licenciement
   - Retraite
   - Décès
   - Autre
4. Saisir la **date de départ**
5. Confirmer

L'employé disparaît de la liste principale mais reste accessible via le filtre **Archivé**.

---

### Exercice 2 — Créer les employés

> **Durée** : 30 minutes

Créer les employés suivants. Utiliser les départements créés dans l'exercice 1.

| Nom              | Poste               | Département         | Responsable      | Email                        |
|------------------|---------------------|---------------------|------------------|------------------------------|
| Sophie Laurent   | Directrice Générale | Direction Générale  | *(aucun)*        | s.laurent@formationsa.fr     |
| Marc Dupont      | Responsable RH      | Ressources Humaines | Sophie Laurent   | m.dupont@formationsa.fr      |
| Julie Chen       | Responsable Finance | Finance             | Sophie Laurent   | j.chen@formationsa.fr        |
| Paul Morin       | Comptable           | Comptabilité        | Julie Chen       | p.morin@formationsa.fr       |
| Léa Bernard      | Chef de projet IT   | Développement       | Sophie Laurent   | l.bernard@formationsa.fr     |
| Antoine Petit    | Développeur         | Développement       | Léa Bernard      | a.petit@formationsa.fr       |

Ensuite :
- Revenir sur le département **Ressources Humaines** et définir **Marc Dupont** comme responsable
- Revenir sur le département **Finance** et définir **Julie Chen** comme responsable
- Revenir sur le département **Développement** et définir **Léa Bernard** comme responsable

**Vérification** : Ouvrir la fiche de **Antoine Petit** — son responsable doit être Léa Bernard, et son département Développement.

---

## Module 3 — Les Contrats

### Qu'est-ce qu'un contrat dans Odoo ?

Le contrat de travail dans Odoo enregistre la relation contractuelle entre l'entreprise et l'employé : type de contrat, dates, salaire. Il conditionne également le calcul de la paie (module Paie).

Chaque employé peut avoir **plusieurs contrats successifs** (ex : CDD transformé en CDI), mais **un seul contrat actif** à la fois.

---

### 3.1 Les statuts d'un contrat

Un contrat passe par plusieurs états au cours de sa vie :

| Statut       | Signification                                              |
|--------------|------------------------------------------------------------|
| **Nouveau**  | Contrat créé mais pas encore validé                        |
| **En cours** | Contrat actif, l'employé travaille sous ce contrat         |
| **Expiré**   | La date de fin est passée (CDD terminé)                    |
| **Annulé**   | Contrat annulé avant son démarrage                         |

**Cycle de vie** :
```
Nouveau ──► En cours ──► Expiré
              │
              └──► Annulé
```

---

### 3.2 Accéder aux contrats

**Depuis la fiche employé** :
1. Ouvrir la fiche de l'employé
2. Cliquer sur le bouton **Contrats** (en haut à droite, avec le nombre de contrats)

**Depuis le menu** :
- Employés > Employés > (ouvrir un employé) > bouton Contrats
- Ou : Employés > (selon configuration) > Contrats

---

### 3.3 Créer un contrat

**Chemin** : Fiche employé > bouton **Contrats** > **Nouveau**

| Champ              | Description                                                    | Obligatoire |
|--------------------|----------------------------------------------------------------|-------------|
| Référence          | Nom du contrat (ex : "CDI - Marc Dupont")                      | Oui         |
| Employé            | Sélectionné automatiquement depuis la fiche                    | Oui         |
| Type de contrat    | CDI, CDD, Alternance, Stage, etc.                              | Oui         |
| Date de début      | Date de prise de poste                                         | Oui         |
| Date de fin        | Obligatoire pour un CDD — laisser vide pour un CDI             | Non         |
| Salaire brut mensuel | Rémunération mensuelle en euros                              | Oui         |
| Responsable RH     | La personne RH en charge du suivi                              | Non         |
| Notes              | Informations complémentaires (avantages, primes, clauses…)     | Non         |

> **CDI vs CDD** :
> - **CDI** (Contrat à Durée Indéterminée) : laisser la **date de fin vide**
> - **CDD** (Contrat à Durée Déterminée) : obligatoirement une **date de fin**

---

### 3.4 Étapes de création d'un contrat — Pas à pas

1. Ouvrir la fiche de l'employé concerné
2. Cliquer sur le bouton **Contrats** en haut à droite
3. Cliquer sur **Nouveau**
4. Vérifier que l'**Employé** est correct
5. Saisir la **Référence** du contrat (ex : "CDI - Antoine Petit - 2024")
6. Choisir le **Type de contrat** (CDI, CDD…)
7. Saisir la **Date de début**
8. Pour un CDD : saisir la **Date de fin**
9. Saisir le **Salaire brut mensuel**
10. Cliquer sur **Enregistrer**
11. Cliquer sur **Confirmer** pour passer le contrat en statut **En cours**

---

### 3.5 Confirmer un contrat

Un contrat créé est d'abord au statut **Nouveau** (brouillon). Pour l'activer :

- Cliquer sur le bouton **Confirmer** (barre de statut en haut ou bouton vert)
- Le statut passe à **En cours**

> **Attention** : Une fois confirmé, le salaire et les dates ne sont plus modifiables directement. Pour corriger une erreur, repasser en **Nouveau** via le bouton **Remettre en brouillon**.

---

### 3.6 Gérer un CDD qui se termine

Quand la date de fin d'un CDD est atteinte, Odoo passe automatiquement le contrat en statut **Expiré** (via une tâche planifiée quotidienne).

**Options à l'expiration** :
1. **Renouveler** : créer un nouveau contrat avec une nouvelle date de début
2. **Transformer en CDI** : créer un nouveau contrat CDI sans date de fin
3. **Ne pas renouveler** : archiver l'employé

---

### 3.7 Voir l'historique des contrats d'un employé

Depuis la fiche de l'employé, le bouton **Contrats** affiche le **nombre total** de contrats (actifs + passés). Cliquer dessus pour voir la liste complète avec les dates et statuts.

---

### 3.8 Configurer les types de contrats

**Chemin** : Employés > Configuration > Types de contrats

Odoo 18 propose par défaut plusieurs types. Vous pouvez en créer de nouveaux :

1. Cliquer sur **Nouveau**
2. Saisir le **Nom** (ex : "Contrat d'apprentissage")
3. Sélectionner le ou les **Pays** concernés
4. Enregistrer

---

### Exercice 3 — Créer les contrats

> **Durée** : 30 minutes

Créer un contrat pour chaque employé de l'exercice 2 :

| Employé          | Type    | Date début   | Date fin     | Salaire brut |
|------------------|---------|--------------|--------------|--------------|
| Sophie Laurent   | CDI     | 01/01/2022   | *(vide)*     | 6 000 €      |
| Marc Dupont      | CDI     | 01/03/2022   | *(vide)*     | 3 800 €      |
| Julie Chen       | CDI     | 01/06/2022   | *(vide)*     | 4 200 €      |
| Paul Morin       | CDD     | 01/01/2024   | 31/12/2024   | 2 800 €      |
| Léa Bernard      | CDI     | 15/09/2023   | *(vide)*     | 4 500 €      |
| Antoine Petit    | CDD     | 01/03/2024   | 28/02/2025   | 3 200 €      |

**Pour chaque contrat** : créer, puis cliquer sur **Confirmer** pour le passer "En cours".

**Vérification** :
- Paul Morin a un CDD expiré au 31/12/2024 — son statut devrait être **Expiré**
- Antoine Petit a un CDD dont la date de fin est le 28/02/2025 — statut **Expiré** également
- Les 4 autres sont **En cours**

---

## Module 4 — Recherche, Analyse et Rapports

### 4.1 Utiliser les filtres avancés

Dans la liste des employés ou des contrats, la barre de recherche permet de filtrer précisément.

**Exemple — Trouver tous les CDD actifs** :
1. Aller dans la liste des contrats
2. Cliquer sur la barre de recherche
3. Sélectionner **Filtres > En cours**
4. Ajouter **Filtres > Date de fin est définie** (pour isoler les CDD)

**Exemple — Employés sans contrat actif** :
1. Liste des employés
2. Filtrer par **Contrat > Aucun contrat actif**

---

### 4.2 Utiliser les regroupements

**Regrouper les contrats par type** :
1. Aller dans la liste des contrats
2. Cliquer sur la loupe > **Regrouper par > Type de contrat**

**Regrouper les employés par département puis par responsable** :
1. Liste des employés
2. **Regrouper par > Département**
3. **Regrouper par > Responsable**

---

### 4.3 Vue graphique — Analyse des effectifs

1. Aller dans **Employés > Employés**
2. Cliquer sur l'icône **Graphique** (barre en haut à droite)
3. Sélectionner :
   - **Type** : Barres / Camembert / Courbe
   - **Mesure** : Nombre d'employés
   - **Regrouper par** : Département ou Poste

Cela donne une vision instantanée de la répartition des effectifs.

---

### 4.4 Exporter les données

1. Aller dans la liste souhaitée (employés, contrats…)
2. Cocher les enregistrements à exporter (ou cocher la case en-tête pour tout sélectionner)
3. Cliquer sur **Action > Exporter**
4. Choisir les colonnes à inclure
5. Choisir le format : **Excel (.xlsx)** ou **CSV**
6. Cliquer sur **Exporter**

---

### Exercice 4 — Analyse et recherche

> **Durée** : 20 minutes

1. **Lister tous les employés du département Développement** :
   Utiliser la barre de recherche > filtrer par département = Développement

2. **Afficher le nombre d'employés par département** :
   Vue Graphique > Regrouper par > Département > Type Camembert

3. **Identifier les contrats expirés** :
   Liste des contrats > Filtre > Expiré
   → Vous devez voir Paul Morin et Antoine Petit

4. **Exporter la liste des employés en Excel** avec les colonnes :
   Nom, Département, Poste, Email professionnel, Date de début du contrat

---

## Exercice de synthèse

> **Durée** : 30 minutes

### Contexte

La société **Formation SA** embauche un nouveau collaborateur :

**Camille Renard** rejoint l'équipe le 1er avril 2025 en tant que **Développeuse Full Stack** dans le département **Développement**. Son responsable est **Léa Bernard**. Elle est embauchée en CDD de 6 mois (jusqu'au 30 septembre 2025) avec un salaire brut de 3 400 €/mois. En cas de bonne performance, le CDD sera renouvelé en CDI.

### Travail à effectuer

1. Vérifier que le poste **"Développeuse Full Stack"** existe — sinon le créer dans **Configuration > Postes**
2. Créer la fiche employé de **Camille Renard** avec :
   - Tous les champs de l'onglet "Informations sur le travail"
   - Email : c.renard@formationsa.fr
   - Téléphone : 01 23 45 67 89
3. Créer son contrat CDD et le **confirmer**
4. Vérifier que Camille apparaît bien dans la liste du département Développement
5. Simuler le renouvellement en CDI :
   - Créer un **deuxième contrat CDI** à partir du 1er octobre 2025 (sans date de fin, salaire : 3 600 €)
   - Confirmer ce second contrat

**Vérification finale** : La fiche de Camille Renard doit afficher **2 contrats**.

---

## Bonnes pratiques RH dans Odoo

### À faire

- Toujours créer les **départements avant les employés**
- Renseigner le **responsable** de chaque employé pour activer la hiérarchie
- Utiliser les **types de contrats** standardisés pour les rapports
- **Archiver** les employés qui partent plutôt que de les supprimer
- Vérifier régulièrement les **contrats proches de l'expiration**

### À éviter

- Ne pas supprimer un employé qui a des données liées (pointages, notes de frais…)
- Ne pas laisser un contrat en statut "Nouveau" une fois l'employé en poste
- Ne pas dupliquer les postes avec des noms légèrement différents (créer une nomenclature)
- Ne pas créer plusieurs comptes pour le même employé

---

## Récapitulatif des chemins de navigation

| Action                         | Chemin dans Odoo 18                                         |
|--------------------------------|-------------------------------------------------------------|
| Créer un département           | Employés > Configuration > Départements > Nouveau           |
| Créer un poste                 | Employés > Configuration > Postes > Nouveau                 |
| Créer un employé               | Employés > Employés > Nouveau                               |
| Voir les contrats d'un employé | Fiche employé > bouton Contrats                             |
| Créer un contrat               | Fiche employé > Contrats > Nouveau                          |
| Archiver un employé            | Fiche employé > Action > Archiver                           |
| Voir les employés archivés     | Employés > Recherche > Filtre : Archivé                     |
| Configurer les types de contrats | Employés > Configuration > Types de contrats              |
| Exporter des données           | Liste > Sélectionner > Action > Exporter                    |

---

## Questions fréquentes

**Q : Peut-on supprimer un employé ?**
Oui, mais seulement s'il n'a aucune donnée liée (contrats, feuilles de temps, notes de frais). Dans la pratique, il vaut mieux toujours **archiver**.

**Q : Un employé peut-il avoir plusieurs contrats actifs en même temps ?**
Non. Odoo alerte si vous essayez de confirmer un second contrat alors qu'un autre est déjà actif sur la même période.

**Q : Comment modifier le salaire d'un contrat en cours ?**
Remettre le contrat en brouillon (bouton **Remettre en brouillon**), modifier le salaire, puis reconfirmer. Attention : cela peut impacter les calculs de paie déjà effectués.

**Q : Quelle est la différence entre "Poste" et "Titre du poste" ?**
- **Poste** : référence au catalogue des postes de l'entreprise (ex : Développeur)
- **Titre du poste** : intitulé libre qui apparaît sur les documents (ex : Développeur Python Senior)

**Q : Comment affecter un utilisateur Odoo à un employé ?**
Dans la fiche employé > onglet **Paramètres RH** > champ **Utilisateur lié**. Cela permet à l'employé de se connecter à Odoo et d'accéder à ses congés, notes de frais, etc.

---

*Formation Odoo 18 — Ressources Humaines | Version 1.0 — Mars 2026*
