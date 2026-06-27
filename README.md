# Rendering de uma cena

Este é o projeto é referente ao trabalho 2 de Computação Gráfica

## Integrantes

- Ignacio Sander
- Leonardo Amorim
- Lucas Victorino

## Pré-requisitos

- Python 3.10 ou superior (recomendado)

### 1. Instalar o Python

Caso ainda não possua o Python instalado:

- **Windows:** https://www.python.org/downloads/
  - Durante a instalação, marque a opção **"Add Python to PATH"**.

- **Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verifique a instalação:

```bash
python3 --version
```

ou

```bash
python --version
```

---

## Instalar as dependências

Instale as bibliotecas necessárias:

```bash
pip install pygame numpy
```

Caso utilize Linux e tenha mais de uma versão do Python instalada:

```bash
pip3 install pygame numpy
```

---

## Executando o projeto

Execute a aplicação através da **main.py**:

### Windows

```bash
python main.py
```

### Linux/macOS

```bash
python3 main.py
```

---

## Controles

| Tecla | Função |
|-------|--------|
| ← | Rotaciona o modelo para a esquerda |
| → | Rotaciona o modelo para a direita |
| **W** | Alterna o modo Wireframe |
| **Q** | Exibe/oculta os vértices |
| **T** | Ativa/desativa o contorno (Toon) |
| **C** | Gera novas cores aleatórias para os objetos |

---

## Dependências

- Python 3
- Pygame
- NumPy

Instalação rápida:

```bash
pip install pygame numpy
```