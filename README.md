# Wallet App – Gestión segura de métodos de pago

Aplicación tipo **wallet** para registro de usuarios, autenticación y administración segura de métodos de pago.

El proyecto fue desarrollado aplicando una **arquitectura limpia básica (Clean Architecture)** con separación por capas para mejorar mantenibilidad, escalabilidad y claridad del código.

---

# Funcionalidades implementadas

##  Autenticación

- Registro de usuario
- Inicio de sesión con JWT
- Cierre de sesión
- Consulta de perfil autenticado

---

## Métodos de pago

- Alta de método de pago
- Listado de métodos de pago del usuario autenticado
- Consulta de detalle de un método de pago
- Eliminación lógica (soft delete)
- Prevención de registros duplicados

---

## Seguridad y trazabilidad

- Hash seguro de contraseñas (`bcrypt`)
- Hash de identificadores sensibles de métodos de pago
- Respuesta con identificadores enmascarados (`****1234`)
- Protección de endpoints mediante JWT
- Registro automático de auditoría (audit logs)

---

# Arquitectura del proyecto

Se implementó una **arquitectura limpia básica**, separando responsabilidades en distintas capas:

```bash
wallet-backend/
├── src/
│
├── config/            # configuración general, DI, seguridad
├── domain/            # entidades de dominio
├── helpers/           # utilidades (JWT, seguridad)
├── infrastructure/    # modelos DB, repositorios, middleware
├── presentation/      # rutas y schemas
├── services/          # lógica de negocio
│
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── schema.sql
├── .env.example

# Cómo levantar el proyecto

## 1. Clonar repositorio

```bash
git clone <url-del-repositorio>
cd wallet-backend
```

---

## 2. Levantar contenedores

```bash
docker compose up --build
```

Copyright (c) 2026 David Arias

All rights reserved.

No permission is granted to use, copy, modify or distribute
this software without explicit written consent from the author.