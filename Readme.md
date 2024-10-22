# **Despliegue de Modelos ML**

## 🚀 **¿Qué vamos a lograr?**

En este proyecto, aprenderemos a **exportar modelos de Machine Learning**, a crear **APIs** locales con Flask, y a desplegar nuestras aplicaciones en **Google Compute Engine** y **Google App Engine**.

---

## 🛠 **Parte 1: Exportar tu Modelo ML**

### 1. **Identificar los Objetos Necesarios**

Para exportar tu modelo, primero necesitas identificar los objetos y funciones necesarias para realizar una predicción. Por ejemplo:

```python
nueva_frase = "El cine español tiene películas muy interesantes."
nueva_frase_tfidf = vectorizer.transform([nueva_frase])
idioma_predicho = model.predict(nueva_frase_tfidf)
print(f"El idioma predicho es: {idioma_predicho[0]}")
```

### 2. **Exportar el Modelo y el Vectorizador**

Usamos la librería `pickle` para guardar el modelo y el vectorizador:

```python
import pickle

# Exportar el modelo
with open('model.sav', 'wb') as model_file:
    pickle.dump(model, model_file)

# Exportar el vectorizador
with open('vectorizer.sav', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)
```

---

## 🖥 **Parte 2: Ejecutar tu primera API con Flask**

### 1. **Clona el Repositorio**

Clona el repositorio `DS_MLops_Cloud` a tu computadora:

```bash
git clone https://github.com/BootcampXperience/DS_MLops_Cloud
```

### 2. **Configura el Entorno**

Accede a la carpeta `hello_world`, crea un entorno virtual e instala las dependencias:

```bash
cd hello_world
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. **Ejecuta la Aplicación Localmente**

Despliega tu aplicación en el puerto 8080:

```bash
python3 main.py
```

Accede a la aplicación en tu navegador: [http://127.0.0.1:8080](http://127.0.0.1:8080)

---

## 🌐 **Parte 3: Despliegue en Google Compute Engine**

### 1. **Configura la VM en GCloud**

1. Abre **Google Console** y crea un nuevo proyecto.
2. Habilita la API **Compute Engine API**.
3. Crea una nueva **Instancia de Máquina Virtual**:
   - Selecciona la serie `E2` y el tipo de máquina `e2-micro`.
   - Habilita el tráfico HTTP y HTTPS en la configuración de firewall.

### 2. **Conecta a la VM y configura el entorno**

- Conéctate vía SSH y actualiza las librerías:

```bash
sudo apt-get update
```

- Instala **Git** y crea una clave SSH:

```bash
sudo apt-get install git-all
ssh-keygen -t rsa -b 4096 -C "tu-email@gmail.com"
```

- Clona el repositorio en tu VM:

```bash
git clone git@github.com:BootcampXperience/DS_MLops_Cloud.git
```

- Crea un entorno virtual e instala las dependencias:

```bash
cd DS_MLops_Cloud/hello_projectML
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Ejecuta tu aplicación:

```bash
python3 main.py
```

Accede a tu aplicación en [http://tu-ip-externa:8080](http://tu-ip-externa:8080)

---

## ☁ **Parte 4: Despliegue en Google App Engine**

### 1. **Configura App Engine**

1. Abre **Google Console** y habilita la API **App Engine API**.
2. Instala **Google Cloud CLI**: [Guía de instalación](https://cloud.google.com/sdk/docs/install?hl=es-419).
3. Verifica que tu proyecto de GCloud esté configurado correctamente:

```bash
gcloud config list
```

4. Descarga el proyecto desde [GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples).

### 2. **Despliega tu aplicación en App Engine**

1. Navega a la ruta donde se encuentra el archivo `app.yaml`.
2. Ejecuta el comando para desplegar:

```bash
gcloud app deploy
```

Tu aplicación estará disponible en la URL proporcionada en el terminal.

---

### ¡Sigue estos pasos para comenzar con tu proyecto hoy!
