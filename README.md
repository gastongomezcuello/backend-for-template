# Backend para Template de Criptomonedas

Este proyecto es un backend desarrollado en Django que sirve como base para un dashboard de criptomonedas. El objetivo principal fue integrar las vistas del template base con funcionalidades backend, como autenticación, manejo de usuarios y consumo de APIs externas. Fue realizado como práctica para abordar múltiples aspectos del desarrollo web.

---

## Requisitos Previos

- Python 3.8 o superior
- Entorno virtual configurado (recomendado)
- Paquetes incluidos en el archivo `requirements.txt`

---

## Estructura del Proyecto

El proyecto se organiza en las siguientes aplicaciones principales:

1. **`coins`**:

   - Modelos: `Card`, `Coin`, `Transaction`
   - Funcionalidades relacionadas con tarjetas y transacciones.

2. **`news`**:

   - Modelo: `News`
   - Gestión e integración de noticias externas.

3. **`users`**:

   - Uso del modelo de usuario de Django con extensión personalizada:
     - Modelo adicional: `UserProfile` (información adicional del usuario).

4. **`admin_settings`**:
   - Modelos: `Country`, `Language`
   - Configuraciones globales relacionadas con localización.

Además, cuenta con:

- Conexión y configuración de archivos estáticos y de media.
- Modificación del middleware predeterminado de Django para proteger las vistas con autenticación.

---

## Instalación y Configuración

1. Clonar el repositorio:

   ```bash
   git clone <URL-del-repositorio>
   cd backend-for-template
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate # En Windows: venv\Scripts\activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno:
   Crear un archivo `.env` en la raíz del proyecto con las siguientes claves:

   ```env
   DEBUG=True
   SECRET_KEY=<tu_secret_key>
   NEWS_API_KEY=<tu_news_api_key>
   ```

5. Realizar las migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---

## Características Implementadas

- **Autenticación de usuarios:**

  - Registro, inicio de sesión y logout.
  - Panel de administración para gestionar usuarios: activar/bloquear cuentas.

- **Integración con API externa de noticias:**

  - Obtención y visualización de noticias relacionadas con criptomonedas.

- **Gestión de wallets:**

  - Formularios conectados para crear tarjetas y transacciones.

- **Vistas protegidas:**

  - Middleware ajustado para garantizar que solo usuarios autenticados accedan a las vistas.

- **Organización de archivos:**
  - Archivos estáticos y de media organizados en carpetas específicas.

---

## Limitaciones o Puntos Pendientes

- Vistas sin conectar:

  - **Portfolio:** Implementación pendiente.
  - **Detalle de monedas:** Sin lógica avanzada, pendiente de conectar.

- Archivos HTML sin usar en la raíz:
  - `404.html`, `500.html`, `forgotpassword.html`

---

## Dependencias

Listado completo de dependencias incluidas en `requirements.txt`:

```txt
asgiref==3.8.1
certifi==2024.12.14
charset-normalizer==3.4.0
Django==5.1.4
django-environ==0.11.2
idna==3.10
pillow==11.0.0
requests==2.32.3
sqlparse==0.5.3
tzdata==2024.2
urllib3==2.2.3
```

---

## Cierre

Este proyecto es un ejercicio práctico que aborda múltiples aspectos del desarrollo web con Django. Si tienes preguntas o deseas colaborar, no dudes en contactarme.
