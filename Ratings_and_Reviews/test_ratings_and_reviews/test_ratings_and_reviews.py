import pytest
from  Ratings_and_Reviews.ratings_and_reviews.ratings_and_reviews import Rating
@pytest.fixture
def rating():
    return Rating()

def test_add_review(rating):
    rating.add_review('Great product!')
    assert rating.get_reviews() == ['Great product!']

def test_add_rating(rating):
    rating.add_rating(5)
    assert rating.get_average_rating() == 5

def test_get_average_rating_empty(rating):
    assert rating.get_average_rating() == 0

def test_get_reviews_empty(rating):
    assert rating.get_reviews() == []
