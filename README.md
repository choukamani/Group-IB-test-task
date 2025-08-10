
# Weather Agent Project

Un agent météo intelligent basé sur un LLM local utilisant LangChain et Ollama. Il répond aux questions météo en interrogeant des APIs via un serveur proxy MCP. Le projet est modulaire : backend API, agent intelligent et interface web Streamlit.

## Table des matières

- [Présentation](#présentation)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Endpoints API](#endpoints-api)
- [Agent](#agent)
- [Interface utilisateur](#interface-utilisateur)
- [Configuration](#configuration)
- [Dépendances](#dépendances)


---

## Présentation

Ce projet propose un système de question/réponse météo propulsé par un LLM local (Ollama) et LangChain. Il récupère les données météo via des APIs externes, traite les requêtes utilisateur et affiche les résultats dans une interface web.

Nous utilisons un modèle open source sur Ollama (par exemple, `llama2`, `mistral` ...), mais il est possible d'utiliser n'importe quel autre modèle open source compatible avec Ollama. Il suffit de le télécharger et de l'activer via Ollama.

---

## Structure du projet

```
weather_agent_project/
│
├── agent/
│   ├── agent.py           # Logique principale de l'agent (LangChain, outils)
│   ├── model_loader.py    # Chargement des modèles LLM (Ollama)
│   ├── tools.py           # Outils personnalisés pour l'agent
│   
│
├── mcp_server/
│   ├── main.py            # Serveur FastAPI avec endpoints
│   ├── requirements.txt   # Dépendances serveur
│   └── weather_api.py     # Intégration API météo
│
├── ui/
│   └── app.py             # Interface Streamlit
│
├── requirements.txt       # Dépendances globales
├── README.md              # Documentation
└── .env                   # Configuration 
```

---

## Installation

1. **Cloner le dépôt :**
	 ```bash
	 git clone <repo_url>
	 cd weather_agent_project
	 ```

2. **Installer les dépendances Python :**
	 ```bash
	 pip install -r requirements.txt
	 ```

3. **Installer les dépendances du serveur MCP :**
	 ```bash
	 cd mcp_server
	 pip install -r requirements.txt
	 cd ..
	 ```

4. **Installer et lancer Ollama :**
	 - Télécharger Ollama sur [ollama.com](https://ollama.com/).
	 - Installer un modèle open source (ex : `ollama pull llama2`).
	 - Démarrer le serveur Ollama localement.
	 - Pour changer de modèle, utiliser la commande `ollama pull <nom_du_modele>` puis le sélectionner dans la config.



## Utilisation

### 1. Démarrer le serveur MCP

```bash
cd mcp_server
uvicorn main:app --reload
```

Le serveur expose les endpoints pour les coordonnées et la météo.


### 2. Lancer l'interface Streamlit

Lancez la commande suivante depuis la racine du projet :

```bash
streamlit run ui/app.py
```

Accédez à l'interface web sur `http://localhost:8501`.

### 3. Interagir avec l'agent

- Saisir une question météo dans l'UI.
- L'agent utilise LangChain et Ollama pour traiter la requête et récupérer les données via le serveur MCP.

---

## Endpoints API

Le serveur MCP propose :

- `GET /coordinates?city=<nom_ville>`  
	Retourne la latitude et la longitude pour une ville donnée.

- `GET /weather?lat=<latitude>&lon=<longitude>`  
	Retourne les données météo pour les coordonnées spécifiées.

---

## Agent

- **LangChain** : Orchestration du raisonnement LLM et des outils.
- **Ollama** : Backend LLM local pour la compréhension du langage naturel.
- **Outils personnalisés** : Intégration avec les endpoints MCP pour récupérer la météo et les coordonnées.
- **Modèles open source** : Possibilité d'utiliser différents modèles open source disponibles sur Ollama (`llama2`, `mistral`, `gemma`, etc.).

---

## Interface utilisateur

- **Streamlit** : Interface web interactive.
- **Fonctionnalités** :
	- Zone de saisie pour les questions
	- Affichage des réponses de l'agent
	- Gestion des erreurs et messages d'état



## Dépendances

- Python 3.10+
- [LangChain](https://python.langchain.com/)
- [Ollama](https://ollama.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- Autres dépendances dans `requirements.txt` et `mcp_server/requirements.txt`

---


