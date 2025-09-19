from flask import Flask, render_template, request
from transformers import pipeline
import os

app = Flask(__name__)

local_model_path = r"C:/Users/Nandhini Pushpa/Downloads/emotion_model_1-20250916T080312Z-1-001/emotion_model_1"
if not os.path.exists(local_model_path):
    raise FileNotFoundError(f"Model folder not found: {local_model_path}")

classifier = pipeline("text-classification", model=local_model_path, framework="pt")

languages = ['english', 'tamil']

curated_recommendations = {
    "joy": {
        "english": {
            "playlists": {
                "kids": ["https://open.spotify.com/playlist/6rqtaHBjxTu6DytqrbLXuh"],
                "adults": ["https://open.spotify.com/playlist/1kZifnfzpb0YSMOCtq5mIx"],
                "seniors": ["https://open.spotify.com/playlist/0jrlHA5UmxRxJjoykf7qRY"]
            },
            "quotes": [
                "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama",
                "The purpose of our lives is to be happy. – Dalai Lama"
            ],
            "poems": [
                "“A Light Exists in Spring” by Emily Dickinson",
                "“Ode to Joy” by Friedrich Schiller"
            ]
        },
        "tamil": {
            "playlists": {
                "kids": ["https://open.spotify.com/playlist/2pYdhZjsFiI8ru1jaNrO8R"],
                "adults": ["https://open.spotify.com/playlist/5vWq8ktlFZiFpGfJbFkc5D"],
                "seniors": ["https://open.spotify.com/playlist/5kwvEJyTgKyugqdH4LIhFr"]
            },
            "quotes": [
                "மகிழ்ச்சி என்பது தயார் செய்யப்படும் ஒன்று அல்ல. இது உங்கள் சொந்த செயல்களில் இருந்து வருகிறது. – தாலை லாமா",
                "எங்கள் வாழ்க்கையின் நோக்கம் மகிழ்ச்சியாக வாழ்வதே. – தாலை லாமா"
            ],
            "poems": [
                "“வசந்த காலத்தில் ஒளி ஏதோ இருக்கும்” - எமிலி டிக்கின்சன்",
                "“சந்தோஷம்” - ஃப்ரீட்ரிக் ஷில்லர்"
            ]
        }
    },
    "sadness": {
        "english": {
            "playlists": {
                "kids": ["https://open.spotify.com/album/0CkSCUTfUOE0Wp7QqZKVzX"],
                "adults": ["https://open.spotify.com/playlist/25ZzkJkOuYir9kHr2CqwPQ"],
                "seniors": ["https://open.spotify.com/playlist/4JnrC17yxHUtHFjrpHDxKi"]
            },
            "quotes": [
                "Tears come from the heart and not from the brain. – Leonardo da Vinci",
                "Every human walks around with a certain kind of sadness. – Brad Pitt"
            ],
            "poems": [
                "“Funeral Blues” by W.H. Auden",
                "“I measure every grief I meet” by Emily Dickinson"
            ]
        },
        "tamil": {
            "playlists": {
                "kids": ["https://open.spotify.com/album/45zqFu6lQVGBdNYtumUPEf"],
                "adults": ["https://open.spotify.com/playlist/4c4spdFwXBKiFTqug4i0FK"],
                "seniors": ["https://open.spotify.com/playlist/5XwEIM7WcrDUGRJEYCG3E9"]
            },
            "quotes": [
                "அழுகைகள் இதயத்திலிருந்து வரும், மூளையில் இருந்து அல்ல. – லியோனார்டோ டா வின்சி",
                "ஒவ்வொரு மனிதனும் ஒரு வகை சோகத்துடன் நடக்கிறார். – பிராட் பிட்ட்"
            ],
            "poems": [
                "“மரண கவிதைகள்” - டபிள்யூ.எச். ஆடன்",
                "“நான் சந்திக்கும் ஒவ்வொரு கவலையையும் அளவிடுகிறேன்” - எமிலி டிக்கின்சன்"
            ]
        }
    },
    "anger": {
        "english": {
            "playlists": {
                "kids": ["https://open.spotify.com/album/2r6bg0wQuP7PN1bU2fgznn"],
                "adults": ["https://open.spotify.com/playlist/67STztGl7srSMNn6hVYPFR"],
                "seniors": ["https://open.spotify.com/album/4O5bEQ6WNgp7JByxT9yGBp"]
            },
            "quotes": [
                "For every minute you remain angry, you give up sixty seconds of peace. – Ralph Waldo Emerson"
            ],
            "poems": [
                "“The Lake Isle of Innisfree” by William Butler Yeats",
                "“Do not go gentle into that good night” by Dylan Thomas"
            ]
        },
        "tamil": {
            "playlists": {
                "kids": ["https://open.spotify.com/playlist/4x6xi0pI8Yaiwp3iNBEh74"],
                "adults": ["https://open.spotify.com/playlist/3p8ejB7BscAVmEdyK7AtXx"],
                "seniors": ["https://open.spotify.com/playlist/5zoLP7dcKS14PgSj8K5aXx"]
            },
            "quotes": [
                "நீங்கள் கோபமாக இருக்கும் ஒவ்வொரு நிமிடத்தையும், நிமிடம் அமைதியை விட்டுவிடுகிறீர்கள். – ரால்ஃப் வால்டோ எமர்சன்"
            ],
            "poems": [
                "“இன்னிஸ்பிரி ஏரியின் தீவின் கவி” - வில்லியம் பட்டு யேட்ஸ்",
                "“அந்த நல்ல இரவு மெதுவாக செல்ல வேண்டாம்” - டிலன் தோமஸ்"
            ]
        }
    },
    "fear": {
        "english": {
            "playlists": {
                "kids": ["https://open.spotify.com/playlist/3gLGJ55iXUdLf9y8dgd7pq"],
                "adults": ["https://open.spotify.com/playlist/7L4qbPDXElR0sw75vLJobW"],
                "seniors": ["https://open.spotify.com/playlist/4eBaqVbGzUyAiXv149myH2"]
            },
            "quotes": [
                "Do one thing every day that scares you. – Eleanor Roosevelt"
            ],
            "poems": [
                "“The Raven” by Edgar Allan Poe",
                "“Stopping by Woods on a Snowy Evening” by Robert Frost"
            ]
        },
        "tamil": {
            "playlists": {
                "kids": ["https://open.spotify.com/playlist/2pYdhZjsFiI8ru1jaNrO8R"],
                "adults": ["https://open.spotify.com/playlist/4Ky4vveGq77DAgV3Z2Lk4e"],
                "seniors": ["https://open.spotify.com/playlist/2f8Jr34CAALmHJ6LY22GoJ"]
            },
            "quotes": [
                "ஒவ்வொரு நாளும் உங்களை பயப்பட வைக்கும் ஒரு காரியம் செய்யுங்கள். – எலியானார் ரூஸ்வேல்ட்"
            ],
            "poems": [
                "“காகம்” - எட்கர் அலன் போ",
                "“மழை இரவில் காடுகளுக்கு அருகில் நிற்கிறது” - ராபெர்ட் ஃப்ராஸ்ட்"
            ]
        }
    },
    
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/detect')
def detect():
    return render_template('detect.html', languages=languages)

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    language = request.form.get('language', 'english').lower()
    age = int(request.form.get('age', 25))

    result = classifier(text)[0]
    emotion = result['label'].lower()
    score = round(result['score'], 3)

    if age < 18:
        age_group = 'kids'
    elif age >= 51:
        age_group = 'seniors'
    else:
        age_group = 'adults'

    recommendations = curated_recommendations.get(emotion, curated_recommendations['joy'])
    language_data = recommendations.get(language, recommendations['english'])

    playlist_links = language_data['playlists'].get(age_group, [])
    quotes = language_data['quotes']
    poems = language_data['poems']

    combined_quotes = quotes + poems

    return render_template(
        'result.html',
        emotion=emotion,
        score=score,
        playlists=playlist_links,
        quotes=combined_quotes,
        language=language,
        languages=languages,
        text=text
    )

if __name__ == "__main__":
    app.run(debug=True)
