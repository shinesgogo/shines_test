from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Need to delete
import random
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# need to delete
class TextInput(BaseModel):
    text: str


@app.post("/process")
async def process_text(input: TextInput):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(input.text)
    print(scores)
    score = scores['compound']

    max_key = max(['neg', 'neu', 'pos'], key=lambda k: scores[k])
    if max_key == 'neg':
        sentiment = "negative"
    elif max_key == 'neu':
        sentiment = "neutral"
    else:
        sentiment = "positive"

    return {"score": score, "sentiment": sentiment}


@app.post("/similarity_score")
async def random_score(input: TextInput):
    score = round(random.uniform(0.4, 0.8), 3)
    return {"score": score}