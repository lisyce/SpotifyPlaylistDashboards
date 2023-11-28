import os, requests, random, string
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")

app = FastAPI()


@app.get("/authorize")
def read_root():
    state = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + "0123456789", k=16))

    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': 'playlist-read-private',
        'redirect_uri': REDIRECT_URI,
        'state': state
    }

    return requests.get('https://accounts.spotify.com/authorize', params=params)