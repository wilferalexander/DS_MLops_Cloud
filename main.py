from flask import Flask, request, render_template_string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Cargar el modelo
with open('models/model.sav', 'rb') as model_file:
    modelo = pickle.load(model_file)

# Cargar el vectorizador
with open('models/vectorizer.sav', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

app = Flask(__name__)

# Ruta principal con formulario y resultado
@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = ""
    
    if request.method == 'POST':
        frase = request.form['frase']
        if frase:
            idiomas_map = {"port": "Portugués","esp": "Español","ing": "Inglés"}
            nueva_frase_tfidf = vectorizer.transform([frase])
            idioma_predicho = modelo.predict(nueva_frase_tfidf)
            resultado = f"El idioma predicho es: {idiomas_map[idioma_predicho[0]]}"
        else:
            resultado = "No se proporcionó ninguna frase."

    # Usamos render_template_string para mostrar el formulario y el resultado en la misma página
    html = '''
    <h1>API de Detección de Idioma</h1>
    <form method="POST">
        <textarea name="frase" rows="4" cols="50" placeholder="Ingrese una frase en Portugues, Español o Inglés..."></textarea><br><br>
        <input type="submit" value="Detectar Idioma">
    </form>
    <p>{{ resultado|safe }}</p>
    '''
    
    return render_template_string(html, resultado=resultado)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run(host="0.0.0.0", port=8080, debug=True)
# [END gae_flex_quickstart]
