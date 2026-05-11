from flask import Flask, render_template 
from flask_socketio import SocketIO, emit 

app = Flask(__name__) 
socketio = SocketIO(app, cors_allowed_origins="*") 

@app.route("/") 
def index(): 
    return render_template("index.html")
@socketio.on("attack_event") 
def handle_attack(data): 
    emit("update_dashboard", data, broadcast=True) 
if __name__ == "__main__": 
    socketio.run(app, host="0.0.0.0", port=5000)
