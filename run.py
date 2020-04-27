from recommendation import create_app
from recommendation.models import Question
from starter import starter

app = create_app()

if __name__ == "__main__":
    try:
        counter = len(Question.query.all()) 
    except Exception:
        starter()
    app.run(debug = True, port = 8082)