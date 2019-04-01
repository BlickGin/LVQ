# Laboratoire : LVQ

Ce projet est le second laboratoire du cours ELE-767 : Apprentissage machine en intelligence artificielle. L'objectif est de créer,
entraîner et tester un réseau compétitif de type LVQ pour que celui-ci puisse identifier des sons produits par la voix humaines. Ces sons
sont des chiffres de 0 à 9 qui doivent être traités par le programme et identifiés selon le chiffre audible.

## Fonctionnement général

### LVQ

La LVQ utilise un réseau du type compétitif qui compare des points dans un espace multidimensionnel. La méthode de comparaison mesure la distance entre les deux en calculant la norme du vecteur qui lie les deux points. Le réseau est di compétitif, car seulement une partie des vecteurs de poids (Points) seront utilisé lors de la detection des sons. Les autres seront ce seront trop éloigné de la cible pour être jugé correct. La LVQ utilise donc la séquence suivante pour faire son apprentissage : 

    1. On initialise les K vecteur de poids pour les M classe à déterminer.
    2. On trouve le vecteur de poids le plus près d'une donnée tirée au hasard.
    3. Si le vecteur est dans la même classe que la donnée alors on approche le vecteur de la donnée.
    4. Dans le cas contraire on éloigne le vecteur de la donnée.
    5. On répète le processus (2) à (4) jusqu'à la condition d'arrêt de l'apprentissage



### Validation 

Pour valider le fonctionnement de l'algorithme on utilise des données de test représentative des sons. Ces données sont différentes de celle de l'entrainement. Si l'algorithme a convergé on va remarqué une convergence sur les données de test.

## Obtention du programme


### Prérequis

Note : Un script d'installation est fournie dans le .zip (windows only) sous le nom de Install_Package.bat les détails sont dans la section installation plus bas.


  * [Python 3.7](https://www.python.org/downloads/release/python-370/)


  
  * [PIP](https://pypi.org/project/pip/)



  * [Numpy](https://pypi.org/project/numpy/)



  * [Pickle](https://pypi.org/project/pickle5/)



  * [Tkinter](https://pypi.org/project/tkinter3000/)
  


  * [Pygubu](https://pypi.org/project/pygubu/)
  
  
  
  * [Matplotlib](https://matplotlib.org/)


### Installation

Le script Install_Package.bat utilise l'invite de commande windows pour installer divers modules python à l'aide de l'utilitaire PIP. Il est à noté qu'à partir de la version 3.4 de Python PIP est installé par défaut lors de l'installation de Python. Donc le seul prérequis à l'installation sur windows est alors Python 3.7. L'installation se déroule donc comme suit : 

        1. Télécharger le fichier .zip contenant le code. 
        2. Télécharger Python3.7.
        3. Extraire le .zip dans un dossier quelconque.
        4. Lancer le fichier Install_Package.bat
        5. Normalement l'installation devrait être complète.

## Déploiment

Pour lancer le programme, il suffit de lancer le fichier Main.py. Puis d'appuyer le boutton de création d'un noveau réseau dans la GUI.

## Auteurs

* **André-Philippe Audette**
* **Noah Ploch**
* **Aurélien Laurent**

