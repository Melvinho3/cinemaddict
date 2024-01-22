from flask import Flask, render_template, request, jsonify
import pickle
import random
import os
import fonctions

app = Flask(__name__)

# Vos données de jeu (à remplacer par votre logique de jeu)
# ...
# Initialiser une liste vide
Titles = []
Years=[]
Director=[]
Genres=[]
Acteurs=[]
Acteurs_=[]
Titles_=[]

# Vérifier si le fichier existe
if os.path.exists('Titles.pkl'):
    # Importer la liste depuis le fichier
    with open('Titles.pkl', 'rb') as fichier:
        Titles = pickle.load(fichier)

if os.path.exists('Years.pkl'):
    # Importer la liste depuis le fichier
    with open('Years.pkl', 'rb') as fichier2:
        Years = pickle.load(fichier2)

if os.path.exists('Director.pkl'):
    # Importer la liste depuis le fichier
    with open('Director.pkl', 'rb') as fichier3:
        Director = pickle.load(fichier3)

if os.path.exists('Genres.pkl'):
    # Importer la liste depuis le fichier
    with open('Genres.pkl', 'rb') as fichier4:
        Genres = pickle.load(fichier4)

if os.path.exists('Acteurs.pkl'):
    # Importer la liste depuis le fichier
    with open('Acteurs.pkl', 'rb') as fichier5:
        Acteurs = pickle.load(fichier5)

if os.path.exists('Acteurs_.pkl'):
    # Importer la liste depuis le fichier
    with open('Acteurs_.pkl', 'rb') as fichier6:
        Acteurs_ = pickle.load(fichier6)

if os.path.exists('Titles_.pkl'):
    # Importer la liste depuis le fichier
    with open('Titles_.pkl', 'rb') as fichier7:
        Titles_ = pickle.load(fichier7)


#enlever un film qui fausse la liste
Years.remove(Years[3383])
Titles.remove(Titles[3383])
Genres.remove(Genres[3383])
Director.remove(Director[3383])
Acteurs.remove(Acteurs[3383])


for liste_de_titres in Titles_:
    position_ = Titles_.index(liste_de_titres)
    for title in liste_de_titres:
        if title not in Titles:
            Titles.append(title)
            Years.append(2000)
            Genres.append('Inconnu')
            Director.append('Inconnu')
            Acteurs.append([Acteurs_[position_]])
        else:
            position_2 = Titles.index(title)
            if Acteurs_[position_] not in Acteurs[position_2]:
                Acteurs[position_2].append(Acteurs_[position_])


nombre_de_films_des_acteurs_=[]
for ttitles in Titles_:
    nombre_de_films_des_acteurs_.append(len(ttitles))
for i in range(0,len(nombre_de_films_des_acteurs_)):
            nombre_de_films_des_acteurs_[i] = nombre_de_films_des_acteurs_[i]**(2.3)


#remplir un dico avec les listes
films=[]
cles = ['Title','Year','Actors','Director','Genres']
for i in range(0,len(Titles)):
    valeurs = [Titles[i],Years[i],Acteurs[i],Director[i],Genres[i]]
    mydict = dict()
    for cle,valeur in zip(cles,valeurs):
        mydict[cle] = valeur
    films.append(mydict)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home.html')
def home2():
    return render_template('home.html')

# Nouvelle route pour choisir la difficulté
@app.route('/choix_difficulte/<int:choix_jeu>')
def choix_difficulte(choix_jeu):
    if choix_jeu == 1:
        return render_template('choix_difficulte.html', choix_jeu=choix_jeu)
    else:
        return "Le jeu n'est pas encore prêt."

# Ajoutez la route pour le jeu avec le choix de difficulté
@app.route('/jeu.html')
def jeu():
    acteur1=request.args.get('nomActeur')
    acteur2=request.args.get('acteur2')
    points=request.args.get('points')
    # Ajoutez ici votre logique spécifique pour la difficulté (passez 'difficulte' à votre template)
    return render_template('jeu.html', films=films,acteur1=acteur1,acteur2=acteur2,points=points)


# Nouvelle route pour la difficulté 1
@app.route('/difficulte1')
def difficulte1():
    # Ajoutez ici la logique spécifique pour la difficulté 1
    difficulte = 1
    return render_template('difficulte.html',difficulte=difficulte,films=films,Acteurs_=Acteurs_,nombre_de_films_des_acteurs_=nombre_de_films_des_acteurs_)

# Nouvelle route pour la difficulté 2
@app.route('/difficulte2')
def difficulte2():
    # Ajoutez ici la logique spécifique pour la difficulté 2
    return "Cette difficulté n'est pas prête"
    return render_template('difficulte.html', acteur1=acteur1, acteur2=acteur2)

# Nouvelle route pour la difficulté 3
@app.route('/difficulte3')
def difficulte3():
    # Ajoutez ici la logique spécifique pour la difficulté 3
    return "Cette difficulté n'est pas prête"
    return render_template('difficulte.html', acteur1=acteur1, acteur2=acteur2)



if __name__ == '__main__':
    app.run(debug=True)