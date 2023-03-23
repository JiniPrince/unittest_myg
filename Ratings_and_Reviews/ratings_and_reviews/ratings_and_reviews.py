class Rating:
    def __init__(self):
        self.reviews = []
        self.ratings = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def get_reviews(self):
        return self.reviews
