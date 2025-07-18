# Movie Recommender 🎬

This is a simple movie recommendation system based on genres, using Python, Flask, and basic Machine Learning techniques.

## How does it work?
The system suggests a movie to the user based on the preferences entered for each genre (Action, Horror, Drama, Sci-Fi, Thriller, Comedy, Romance). The model was trained with a simple dataset of movies and user preferences found on the internet, mainly based on genres.

## Technologies Used
- Python 3
- Flask
- Machine Learning libraries (e.g., scikit-learn, pandas, numpy)
- HTML, CSS

## Project Structure
```
movie_recommender/
├── app.py                # Main Flask file
├── model.py              # Model training and loading
├── utils.py              # Helper functions
├── dados/
│   └── movies.csv        # Movie database
├── static/
│   └── style.css         # CSS styles
├── templates/
│   └── index.html        # Main page
```

## How to run the project
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd movie_recommender
   ```
2. **Install dependencies:**
   ```bash
   pip install flask scikit-learn pandas numpy
   ```
3. **Run the Flask server:**
   ```bash
   python app.py
   ```
4. **Open in your browser:**
   Go to `http://localhost:5000`

## How to use
- For each genre, enter a value from 0 (don't like) to 1 (like a lot).
- Click "Get Recommendation" to receive a movie suggestion.

## Notes
- This system is just a didactic example, using simple data and a basic model.
- Feel free to modify, improve, or adapt it for other types of recommendations!

---

Any questions or suggestions, feel free to open an issue or contribute!

---

# Movie Recommender 🎬 (Português)

Este é um sistema simples de recomendação de filmes baseado em gêneros, utilizando Python, Flask e técnicas básicas de Machine Learning.

## Como funciona?
O sistema sugere um filme para o usuário com base nas preferências informadas para cada gênero (Ação, Terror, Drama, Sci-Fi, Thriller, Comédia, Romance). O modelo foi treinado com um conjunto de dados simples de filmes e preferências de usuários encontrados na internet, principalmente baseados em gêneros.

## Tecnologias Utilizadas
- Python 3
- Flask
- Bibliotecas de Machine Learning (ex: scikit-learn, pandas, numpy)
- HTML, CSS

## Estrutura do Projeto
```
movie_recommender/
├── app.py                # Arquivo principal Flask
├── model.py              # Treinamento e carregamento do modelo de recomendação
├── utils.py              # Funções auxiliares
├── dados/
│   └── movies.csv        # Base de dados dos filmes
├── static/
│   └── style.css         # Estilos CSS
├── templates/
│   └── index.html        # Página principal
```

## Como rodar o projeto
1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd movie_recommender
   ```
2. **Instale as dependências:**
   ```bash
   pip install flask scikit-learn pandas numpy
   ```
3. **Execute o servidor Flask:**
   ```bash
   python app.py
   ```
4. **Acesse no navegador:**
   Abra `http://localhost:5000`

## Como usar
- Para cada gênero, informe um valor de 0 (não gosta) até 1 (gosta muito).
- Clique em "Get Recommendation" para receber uma sugestão de filme.

## Observações
- O sistema é apenas um exemplo didático, usando dados simples e um modelo básico.
- Sinta-se à vontade para modificar, melhorar ou adaptar para outros tipos de recomendação!

---

Qualquer dúvida ou sugestão, fique à vontade para abrir uma issue ou contribuir! 