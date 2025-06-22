import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self, movies_df):
        self.movies = movies_df.copy()
        self.vectorizer = TfidfVectorizer(token_pattern=r'[^|]+')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.movies['genres'].fillna(''))

    def score(self, user_id, ratings_df):
        user_ratings = ratings_df[ratings_df['userId'] == user_id]
        if user_ratings.empty:
            return pd.Series()

        # Pega os filmes avaliados e suas similaridades
        indices = self.movies[self.movies.movieId.isin(user_ratings.movieId)].index
        sim_matrix = cosine_similarity(self.tfidf_matrix[indices], self.tfidf_matrix)

        # Média ponderada de similaridade
        sim_scores = sim_matrix.T @ user_ratings['rating'].values
        sim_scores_series = pd.Series(sim_scores, index=self.movies.movieId)

        # Remove os já assistidos
        return sim_scores_series.drop(labels=user_ratings.movieId.values, errors='ignore').sort_values(ascending=False)
