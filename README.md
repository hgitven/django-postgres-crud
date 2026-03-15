# Gestión de Datos Personales con Django y PostgreSQL

Este es un proyecto web desarrollado con el framework Django que permite la gestión y administración de datos personales (CRUD: Create, Read, Update, Delete). La aplicación utiliza PostgreSQL como sistema de gestión de bases de datos y jQuery para validaciones dinámicas en el lado del cliente.

## 📋 Características

- **Registro de Personas:** Formulario para ingresar nuevos datos personales.
- **Reporte de Personas:** Visualización de todos los registros almacenados en una tabla.
- **Edición de Registros:** Modificación de los datos de una persona existente.
- **Eliminación de Registros:** Borrado de personas de la base de datos con confirmación.
- **Validación Frontend:** Uso de jQuery y Expresiones Regulares para validar en tiempo real los campos de correo electrónico y teléfono, mejorando la experiencia de usuario.

## 🛠️ Tecnologías Utilizadas

*   **Backend:** Python, Django
*   **Frontend:** HTML5, CSS, JavaScript, jQuery
*   **Base de Datos:** PostgreSQL
*   **Control de Versiones:** Git, GitHub

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en un entorno local.

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/hgitven/django-postgres-crud.git
    cd django-postgres-crud
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar la Base de Datos PostgreSQL:**
    - Asegúrate de tener PostgreSQL instalado y en ejecución.
    - Crea una base de datos llamada `pv`.
    - Actualiza las credenciales (USER, PASSWORD, HOST, PORT) en el archivo `pythonV/pythonV/settings.py` para que coincidan con tu configuración local.

5.  **Aplicar las migraciones:**
    ```bash
    python pythonV/manage.py migrate
    ```

6.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python pythonV/manage.py runserver
    ```

7.  Abre tu navegador y ve a `http://127.0.0.1:8000/`.