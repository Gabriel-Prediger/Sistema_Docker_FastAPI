from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from recommender import HybridRecommender
import pandas as pd
import os

app = FastAPI(title="Sistema de Recomendação")

# Dados globais (em memória)
ratings = pd.read_csv("data/ratings.csv")
movies = pd.read_csv("data/movies.csv")
recommender = HybridRecommender(ratings, movies)

DATA_DIR = "data"
RATINGS_FILE = os.path.join(DATA_DIR, "ratings.csv")
MOVIES_FILE = os.path.join(DATA_DIR, "movies.csv")


# === MODELS PARA ENTRADA ===

class UserRating(BaseModel):
    userId: int
    movieId: int
    rating: float

class MovieItem(BaseModel):
    movieId: int
    title: str
    genres: str

# === ENDPOINTS ===

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int, top_k: int = 5):
    try:
        recs = recommender.recommend(user_id, top_k)
        return {"user_id": user_id, "recommendations": recs}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/users/")
def add_user_rating(rating: UserRating):
    global ratings, recommender

    new_row = pd.DataFrame([rating.dict()])
    ratings = pd.concat([ratings, new_row], ignore_index=True)

    # Salva em CSV
    ratings.to_csv(RATINGS_FILE, index=False)

    # Atualiza modelo
    recommender = HybridRecommender(ratings, movies)
    return {"message": "Interação do usuário adicionada com sucesso."}


@app.post("/items/")
def add_item(movie: MovieItem):
    global movies, recommender

    if movie.movieId in movies.movieId.values:
        raise HTTPException(status_code=400, detail="movieId já existe.")

    new_movie = pd.DataFrame([movie.dict()])
    movies = pd.concat([movies, new_movie], ignore_index=True)

    # Salva em CSV
    movies.to_csv(MOVIES_FILE, index=False)

    # Atualiza modelo
    recommender = HybridRecommender(ratings, movies)
    return {"message": "Item adicionado com sucesso."}
