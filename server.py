from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

GAME_FOLDER = "games"
os.makedirs(GAME_FOLDER, exist_ok=True)

@app.route("/")
def home():
    games = []

    for file in os.listdir(GAME_FOLDER):
        if file.lower().endswith(".apk"):
            games.append(file)

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>GameHub</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f2f2;
                margin: 0;
            }

            header {
                background: #202124;
                color: white;
                padding: 18px;
                font-size: 24px;
                font-weight: bold;
            }

            .container {
                padding: 20px;
            }

            .game {
                background: white;
                padding: 18px;
                margin-bottom: 15px;
                border-radius: 12px;
                box-shadow: 0 2px 8px #ccc;
            }

            .download {
                display: inline-block;
                background: #1a73e8;
                color: white;
                padding: 10px 18px;
                border-radius: 8px;
                text-decoration: none;
            }
        </style>
    </head>

    <body>

    <header>🎮 GameHub</header>

    <div class="container">

    <h2>Games</h2>
    """

    if not games:
        html += "<p>No games uploaded yet.</p>"

    for game in games:
        html += f"""
        <div class="game">
            <h3>🎮 {game[:-4]}</h3>
            <a class="download" href="/games/{game}">
                Download APK
            </a>
        </div>
        """

    html += """
    </div>
    </body>
    </html>
    """

    return html


@app.route("/games/<filename>")
def download_game(filename):
    return send_from_directory(
        GAME_FOLDER,
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
