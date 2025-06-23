# Sistema_Docker_FastAPI
# 🐳 Sistema de Recomendação com FastAPI e Docker

## 📋 Índice

- [Descrição](#descrição)
- [Tecnologias](#tecnologias)
- [Funcionalidades](#funcionalidades)
- [Instalação e execução](#instalação-e-execução)
  - [Pré-requisitos](#pré-requisitos)
  - [Passos com Docker Compose](#passos-com-docker-compose)
- [Modelo de recomendação](#modelo-de-recomendação)
  - [Dados de entrada](#dados-de-entrada)
  - [Descrição do algoritmo](#descrição-do-algoritmo)
  - [Decisões de design](#decisões-de-design)
- [Arquitetura da aplicação](#arquitetura-da-aplicação)
- [Uso](#uso)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## 🎯 Descrição

Este projeto fornece uma API de sistema de recomendação utilizando FastAPI, com suporte completo a Docker. O objetivo é criar um sistema modular, fácil de escalar e pronto para deploy.

---

## 🧰 Tecnologias

- Python 3.10+
- FastAPI
- Pydantic
- Docker e Docker Compose
- Scikit-learn / Implicit / Surprise (dependendo da versão do modelo)
- Uvicorn

---

## 🚀 Funcionalidades

- API RESTful para recomendações personalizadas
- Documentação interativa com Swagger UI (`/docs`)
- Healthcheck (`/healthz`)
- Containerização com Docker

---

## ⚙️ Instalação e execução

### Pré-requisitos

- Docker instalado (versão 20+)
- Docker Compose instalado
- Git instalado

### Passos com Docker Compose

Clone o repositório:

```bash
git clone https://github.com/Gabriel-Prediger/Sistema_Docker_FastAPI.git
cd Sistema_Docker_FastAPI
```
---
