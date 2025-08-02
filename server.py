"""Módulo principal do servidor Flask para detecção de emoções."""


from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Renderiza a página inicial da aplicação web."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """ Recebe texto via POST, executa análise emocional e retorna os resultados.
        Retorna mensagem de erro se o texto for inválido.
    """
    try:
        input_text = request.json.get("text")
        if not input_text:
            return jsonify({"emotion_response": "Invalid text! Please try again"}), 200

        result = emotion_detector(input_text)

        if result["dominant_emotion"] is None:
            return jsonify({"emotion_response": "Invalid text! Please try again"}), 200

        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return jsonify({"emotion_response": response_text})

    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    