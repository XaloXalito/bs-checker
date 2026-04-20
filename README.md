# BCV Scraper

Este es un scraper automatizado desarrollado en Python para capturar la tasa del dólar del Banco Central de Venezuela (BCV) y almacenarla en una base de datos PostgreSQL para su posterior consulta y análisis.

## 🛠️ Tecnologías utilizadas

* **Python 3.11+**
* **PostgreSQL** (Base de datos principal)
* **HTTPX** (Cliente HTTP para la extracción de datos)
* **Selectolax** (Parser de HTML de alto rendimiento)
* **SQLAlchemy** (ORM para la gestión de la base de datos)
* **Logging** (Sistema de logs rotativos por fecha)

## 📋 Estructura del Proyecto

```text
.
├── log/                # Logs diarios del sistema
├── logger_config.py    # Configuración del sistema de logs
├── database.py         # Modelos de SQLAlchemy y conexión a Postgres
├── scraper.py          # Lógica principal de scrap
├── requirements.txt    # Dependencias del proyecto
└── .env                # Variables de entorno
