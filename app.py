from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/poll')
def poll():
    location = request.args.get('location')
    question = request.args.get('question')
    return render_template('poll.html', location=location, question=question)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
