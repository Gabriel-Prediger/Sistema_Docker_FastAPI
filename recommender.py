from models.content_based import ContentBasedRecommender
from models.collaborative import CollaborativeRecommender


class HybridRecommender:
    def __init__(self, ratings_df, movies_df):
        self.content_model = ContentBasedRecommender(movies_df)
        self.collab_model = CollaborativeRecommender(ratings_df)
        self.movies = movies_df
        self.ratings = ratings_df

    def recommend(self, user_id, top_k=5):
        cb_scores = self.content_model.score(user_id, self.ratings)
        collab_scores = self.collab_model.score(user_id)

        # Junta os dois com peso igual
        combined = cb_scores.add(collab_scores, fill_value=0) / 2.0
        top_items = combined.sort_values(ascending=False).head(top_k)
        return [
            {"movieId": int(mid), "title": self.movies.loc[self.movies.movieId == mid, "title"].values[0]}
            for mid in top_items.index
        ]
