# 📷 Instatic - Red Social Juvenil con Django + HTMX

**Instatic** es una red social desarrollada con **Django**, que permite a los usuarios registrarse, subir fotos, dar likes, comentar, seguir a otros usuarios y recibir notificaciones. Además, utiliza **HTMX** para mejorar la experiencia de usuario.

---

## 🔧 Requisitos

- Python 3.10
- Docker y Docker Compose (opcional, pero recomendado)
- Git

---

## ⚙️ Instrucciones para desarrollo local

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/instatic.git
cd instatic
```

---

### 2. Crea un entorno virtual e instala dependencias

Asegúrate de usar **Python 3.10** y tener `requirements.txt` en la raíz del proyecto:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

---

### 3. Configura la base de datos y realiza migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4. Crea un superusuario

```bash
python manage.py createsuperuser
```

---

### 5. Ejecuta el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐳 Docker (opcional pero recomendado)

Este proyecto incluye configuración para levantar todo con Docker + PostgreSQL:

```bash
docker-compose up --build
```

Esto levantará el backend de Django y la base de datos automáticamente.

---

## 📁 Estructura del proyecto

```
instatic/
│
├── accounts/          # App principal (registro, login, feed, perfil, etc.)
├── templates/         # Templates HTML (login, feed, perfil, etc.)
├── static/            # Archivos CSS, JS, imágenes estáticas
├── media/             # Archivos subidos por los usuarios
├── requirements.txt   # Dependencias del proyecto
├── manage.py
└── docker-compose.yml # Configuración para entorno Docker
```

---

## 📌 Funcionalidades

- Registro e inicio de sesión personalizados
- Subida y eliminación de imágenes
- Feed con publicaciones de usuarios seguidos
- Likes y comentarios con interacción en tiempo real (HTMX o AJAX)
- Perfil público y privado
- Buscador de usuarios
- Sistema de notificaciones
- Edición de perfil con foto y biografía

---

## ✅ Notas

- Puedes usar Django Admin en `/admin` con el superusuario que hayas creado.
- Las imágenes subidas se almacenan en la carpeta `/media`.
- Si usas Docker, asegúrate de que los puertos no estén ocupados.

---

## 🧑‍💻 Autor

Proyecto desarrollado por [Tu Nombre / Usuario GitHub].
