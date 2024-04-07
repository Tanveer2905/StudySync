from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def lobby():
    return render_template('lobby.html')

@app.route('/room.html')
def room():
    # This function should handle room creation and joining logic
    return render_template('room.html')

if __name__ == '__main__':
    app.run(debug=True)
