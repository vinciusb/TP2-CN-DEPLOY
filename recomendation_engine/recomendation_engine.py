from flask import Flask, request, jsonify
import pickle
from itertools import accumulate
import operator

app = Flask(__name__)
app.model = pickle.load(open("./data/model.pkl", "rb"))


@app.route("/api/recommend", methods=["POST"])
def hello_world():
    # Ensure the request contains JSON data
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": "Invalid JSON data", "message": str(e)}), 400

    # Validate input data
    if not data or "songs" not in data or not isinstance(data["songs"], list):
        return (
            jsonify(
                {"error": "Request must contain a 'songs' field with a list of songs."}
            ),
            400,
        )

    user_songs = data["songs"]

    # Ensure the model is loaded
    if not app.model:
        return jsonify({"error": "Recommendation model is not available."}), 500

    # Use the model to generate recommendations (mock implementation here)
    recommended_songs = recomend_musics(user_songs)

    # Build response
    response = {
        "songs": recommended_songs,
        "version": 1,
        "model_date": 2,
    }

    return jsonify(response)


def recomend_musics(musics: list[str]) -> list[str]:
    musics_key = tuple(musics)
    inferencias = app.model["inferencias"]

    if musics_key in inferencias:
        return inferencias[musics_key][0]

    def recomend_music(music: str) -> str:
        key = tuple([music])
        if key in inferencias:
            return set(inferencias[key][0])
        return set([app.model["musica_mais_frequente"]])

    recomendations = list(map(recomend_music, musics))
    return list(list(accumulate(recomendations, operator.or_))[-1])


if __name__ == "__main__":
    app.run(debug=True)
