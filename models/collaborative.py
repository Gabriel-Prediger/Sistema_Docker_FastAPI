import pandas as pd

class CollaborativeRecommender:
    def __init__(self, ratings_df):
        self.ratings = ratings_df.copy()
        self.global_mean = self.ratings['rating'].mean()

    def score(self, user_id):
        user_data = self.ratings[self.ratings.userId == user_id]
        if user_data.empty:
            return pd.Series()

        movie_means = self.ratings.groupby("movieId")["rating"].mean()
        already_seen = user_data["movieId"].unique()
        movie_means = movie_means.drop(index=already_seen, errors="ignore")
        return movie_means.sort_values(ascending=False)
