# Laboratoire : LVQ

Ce projet est le second laboratoire du cours ELE-767 : Apprentissage machine en intelligence artificielle. L'objectif est de créer,
entraîner et tester un réseau compétitif de type LVQ pour que celui-ci puisse identifier des sons produits par la voix humaines. Ces sons
sont des chiffres de 0 à 9 qui doivent être traités par le programme et identifiés selon le chiffre audible.

## Fonctionnement général

### LVQ



### Validation 


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

Pour lancer le programme, il suffit de lancer le fichier Gui.py dans le dossier ou le .zip a été extrait.Puis, de cliquer sur l'option New Network, selectionner le nombre de couches cachées, la configuration du vecteur d'entrée et le type de fonction d'activation. Une fois cela fait dans Network list selectionner Network_2.pkl, puis appuyer sur Start_learning pour commencer l'entrainement.Ensuite, attendez durant quelques heures (Notre programme est vraiment TRÈS lent) et une fois l'entrainement terminé appuyer sur le bouton Start Testing pour vérifier le performance du réseau avec les données de test.

## Auteurs

* **André-Philippe Audette**
* **Noah Ploch**
* **Aurélien Laurent**

