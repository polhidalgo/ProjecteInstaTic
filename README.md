# 📸 Instatic

**Instatic** és una aplicació web senzilla inspirada en Instagram, desenvolupada com a projecte escolar. La primera versió inclou funcionalitats bàsiques com el registre d'usuaris, inici de sessió i edició de perfil.

```

## ⚙️ Tecnologies utilitzades

- **Backend**: Django (Python)
- **Frontend**: HTMX + Bootstrap
- **Control de versions**: Git + GitHub

## 🏁 Instruccions per començar

### 1. Clona el repositori

```bash
git clone https://github.com/phidalgo/insta_tic.git
cd instatic/backend
```

### 2. Crea un entorn virtual i activa'l

```bash
python -m venv env
source env/bin/activate  # A Windows: env\Scripts\activate
```

### 3. Instal·la les dependències

```bash
pip install django
```

### 4. Crea el projecte de Django (si encara no s'ha creat)

```bash
django-admin startproject config .
```

### 5. Crea l'app per a la gestió d'usuaris

```bash
python manage.py startapp accounts
```

### 6. Afegeix l'app `accounts` a `INSTALLED_APPS` a `config/settings.py`

```python
# config/settings.py

INSTALLED_APPS = [
    ...
    'accounts',
]
```

### 7. Aplica les migracions inicials

```bash
python manage.py migrate
```

### 8. Crea un superusuari per accedir al panell d’administració

```bash
python manage.py createsuperuser
```

### 9. Executa el servidor de desenvolupament

```bash
python manage.py runserver
```

### 10. Accedeix al projecte al navegador

- **Backend/Admin**: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Frontend (a integrar)**: [http://localhost:8000/](http://localhost:8000/)

---

## 🚧 Funcionalitats previstes

- [x] Registre d'usuaris
- [x] Inici de sessió
- [x] Edició de perfil
- [x] Pujada d’imatges
- [ ] Línia de temps amb publicacions
- [x] Comentaris i likes

## 👤 Autors

**Rafel Dalmau, Pol Hidalgo i Enric Ulloa**  
Estudiant de Desenvolupament d'Aplicacions Web (DAW)  
📍 Barcelona

---

> Projecte creat amb finalitats educatives 💻
