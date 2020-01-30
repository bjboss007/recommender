from  recommendation.user.question import questions
from  recommendation.models import * 
from  recommendation import create_app
import os
app = create_app()
app.test_request_context().push()
 
 
rating_1 = Rating(rating = 1)
rating_2 = Rating(rating = 2)
rating_3 = Rating(rating = 3)
rating_4 = Rating(rating = 4)
rating_5 = Rating(rating = 5)
 
moderate = Remedy.query.filter_by(title = "moderate_1").first()
moderate_1 = Remedy.query.filter_by(title = "moderate_2").first()
 
moderate_1.remedy_ratings = [rating_1, rating_2, rating_5, rating_3]
moderate.remedy_ratings = [rating_1, rating_4, rating_5, rating_3]
 
db.session.commit()
 