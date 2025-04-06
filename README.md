# 🥚 Golden_Egg - ERP Lite para Empresas Avícolas

*Golden_Egg* es un sistema ERP Lite desarrollado para digitalizar y optimizar los procesos clave de una empresa avícola dedicada a la comercialización y distribución de huevos. Está construido con una arquitectura de microservicios utilizando FastAPI en el backend y Angular en el frontend, con despliegue en contenedores Docker y CI/CD a través de GitHub Actions.

---

## 🚀 Objetivo General

Desarrollar un sistema ERP Lite con arquitectura de microservicios en Python (FastAPI) que permita gestionar de forma integral procesos de negocio como: clientes, inventario, facturación, usuarios y reportes financieros.

---

## 🎯 Objetivos Específicos

- Gestionar usuarios con autenticación y control de roles (admin, empleado).
- Controlar inventario de huevos por proveedor, entrada y salida.
- Administrar pedidos, facturación y pagos.
- Generar reportes financieros automáticos.
- Proveer una interfaz web moderna y responsiva usando Angular.

---

## ⚙️ Tecnologías Utilizadas

| Tecnología       | Descripción                                |
|------------------|---------------------------------------------|
| FastAPI          | Backend RESTful                            |
| Angular          | Frontend moderno                           |
| MySQL            | Base de datos relacional                   |
| Docker           | Contenedores y orquestación                |
| GitHub Actions   | Integración y despliegue continuo (CI/CD) |
| JWT              | Autenticación segura                       |

---

## 🧱 Arquitectura del Sistema

El sistema está dividido en los siguientes microservicios:

- *Servicio de Autenticación*
- *Servicio de Clientes y Pedidos*
- *Servicio de Productos e Inventario*
- *Servicio de Pagos y Facturación*
- *Servicio de Reportes*
- *Frontend Angular* (Desplegado de forma independiente)

## 🧪 Pruebas

- Pruebas realizadas con *Postman*.
- Colecciones organizadas por microservicio.
- Validación de endpoints: login, crear orden, consultar stock, etc.

---

## 🔐 Seguridad

- Autenticación mediante *JWT*.
- Control de acceso basado en roles (admin, empleado) tanto en backend como frontend.

---

## 📦 Despliegue

- Orquestación con *Docker Compose*.
- CI/CD con *GitHub Actions*.
- Backend y frontend desplegados como servicios independientes.

---

## 📈 Metodología de Desarrollo

Se utilizó *SCRUM* como metodología ágil:

- Sprints semanales
- Reuniones diarias (dailies), de planificación, revisión y retrospectiva
- Gestión de tareas con *Trello*
- Historias de usuario priorizadas en backlog del producto

---

## 🧑‍💻 Equipo de Desarrollo

| Rol              | Nombre Completo           |
|------------------|----------------------------|
| Backend          | Joan Sebastián Sosa Bedoya |
| DevOps           | Jilmar Said Veloza         |
| DBA              | Pablo Garcés               |
| QA               | Juan Diego Rojas           |
| Frontend         | Esteban Pineda             |
| Analista         | Felipe López               |

---

## 📂 Diagramas del Sistema

Incluye los siguientes diagramas en la carpeta /docs:

- Diagrama de Clases UML
- Diagrama de Casos de Uso Principal
- Casos de uso individuales: Login, Registrar, Crear Orden, Generar Reporte, Pagar
