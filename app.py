from flask import Flask, render_template, request, jsonify
from game.state import new_game_state
from game.weather import get_weather
from game.levels import handle_level
from game.rewards import sell_fruits

app = Flask(__name__)

# 暂时只用一个全局游戏状态（以后接 login 再改）
game_state = new_game_state()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/action", methods=["POST"])
def action():
    global game_state
    weather = get_weather()
    game_state = handle_level(game_state, weather)
    return jsonify({
        "state": game_state,
        "weather": weather
    })

@app.route("/sell", methods=["POST"])
def sell():
    global game_state
    game_state = sell_fruits(game_state)
    return jsonify(game_state)

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)