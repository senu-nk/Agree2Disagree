from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

counts = {'agree': 0, 'disagree': 0}

INDEX_HTML = """
<!doctype html>
<title>Agree2Disagree</title>
<h1>{{ statement }}</h1>
<form method="post" action="{{ url_for('vote') }}">
    <button name="choice" value="agree">Agree</button>
    <button name="choice" value="disagree">Disagree</button>
</form>
<p><a href="{{ url_for('results') }}">View results</a></p>
"""

RESULTS_HTML = """
<!doctype html>
<title>Results</title>
<h1>Results</h1>
<p>Agree: {{ agree }}</p>
<p>Disagree: {{ disagree }}</p>
<p><a href="{{ url_for('index') }}">Back</a></p>
"""

STATEMENT = "Pineapple belongs on pizza."

@app.route('/')
def index():
    return render_template_string(INDEX_HTML, statement=STATEMENT)

@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form.get('choice')
    if choice in counts:
        counts[choice] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template_string(RESULTS_HTML, agree=counts['agree'], disagree=counts['disagree'])

if __name__ == '__main__':
    app.run(debug=True)

