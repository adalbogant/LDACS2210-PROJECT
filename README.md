# LDACS2210-PROJECT
LDACS2210 - Information Visualisation project

## Evidemment
1. Histogramme des age at diagnostic
2. Bar chart des types PAM50
3. Kaplan-Meier curves (survival) selon le PAM50
4. Kaplan-Meier curves selon NPI
5. Survival selon Integrative Cluster (molecular subtype of the cancer)
6. Heatmap de corrélation entre attributs cliniques
7. Proportions de femmes ayant subi Masectomie ont radiotherapy / chemiotherapy / hormone therapy VS celles qui ont breast conserving
8. Histogrammes pour les différents mRNA z-score (voir si centré en 0, qui est la valeur "normale"; mettre en évidence la skewness et l'écart-type)
9. Display genes with the most mutations
10. Réduction de dimensions sur les z-scores: 
    1. Proposer le choix de l'algorithme
    2. Proposer le choix du coloring (3-gene-classifier-subtype, cohort...)


## Visualisation ideas
1. Survie (overall_survival) en fonction du pam50_+_claudin-low_subtype
2. Nottingham prognostic index VS overall survival months (voir si correspond aux prévisions)
3. Quelle combinaison de traitements donne le meilleur chance de survie
4. Clustering pr/ PAM50
    a. Variations des mutations ?
    b. Est-ce que profil clinique similaire ?
5. Gènes les + fréquemment mutés
6. Clustering par type de traitement (voir si profils cliniques similaires)
7. Lymph nodes examinés positifs selon PAM50 (box plot)
8. Top XX (20?) des gènes les + mutés (filtrable par portrait clinique)
9. Essayer réduction de dimensions seulement sur mRNA z-scores "importants" parce que sinon, gros curse of dimension quand on réduit la dimension
10. Corrélation entre mutations de certains gènes (heatmap de corrélation, binarisation des mutations)

## Ce qu'on a regardé mais qui était nul
1. "Time to die" (survival months par rapport à death from cancer or other) -> pas intéressant
2. Age at diagnosis VS survival months -> très prévisible (30 ans avant genre 65 ans et puis de moins en moins, ce qui correspond au temps pour atteindre 100 ans environ)

## Questions
- Quelle utilisation attendue des scores mRNA ? Parce que beaucoup tmtc
    - 
- Professeur Lee a dit pas de pie chart, mais pourquoi exactement ?
- Utilisation des librairies : on a pas de restriction mais on doit implémenter les algorithmes ?
    - faire attention au bruit et tout, mais en vrai, on peut réimplémenter ou utiliser

## A rechercher
- Trouver une façon de mettre en évidence les z-scores anormaux (càd pas centré en 0 ou bien très grande variance) (pas encore une définition très claire de "anormal"). Peut-être bar chart de ceux avec la + grande moyenne en valeur absolue, mais ça tient pas compte de la variance alors
- Utiliser les articles déjà publiés sur le dataset
- V de Cramèr & Test du chi² : // corrélation, mais pour variable catégorielle (mutations !!)

## A faire attention
- Les daltoniens
- Pas un temps de chargement de 10 minutes
    - Par exemple : générer des csv déjà preprocess pour ne pas le faire en live à chaque fois

## Notes
- PCA par type de données (sur les z-scores)
- Tradeoff entre clustering puis reduction dimension ou l'inverse (quand est-ce qu'on perd les données en gros)
- Faire attention au pré-processing et tout pour le computationel pas trop mal ==> !! effcacité
- Il y a une structure forte dans le dataset avec des clusters déjà séparés
- Pouvoir identifier les petites populations de gènes
- Beaucoup d'interactivité
- Clustering hiérarchique est bien pour le dataset

## Autres idées en vrac
- Pour les mutations : binariser et afficher selon muté / pas muté
- Dans l'onglet Details : mentionner aussi les méthodes pour remplir les données missing etc.
