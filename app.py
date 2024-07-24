from flask import Flask, render_template
import requests

app = Flask(__name__)

planet_images = {
    'Mercury': 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg',
    'Venus': 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg',
    'Earth': 'https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg',
    'Mars': 'https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg',
    'Jupiter': 'https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg',
    'Saturn': 'https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg',
    'Uranus': 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg',
    'Neptune': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg'
}

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    data = response.json()
    planetas = [corpo for corpo in data['bodies'] if corpo['isPlanet']]

    return planetas 

@app.route('/')
def index():
    planetas = fetch_planet_data()

    for planeta in planetas:
        nome = planeta['englishName']
        planeta['image'] = planet_images.get(nome, '')
        
    return render_template('index.html', planetas=planetas)

if __name__ == '__main__':
    app.run(debug=True)