from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Load journal entries
JOURNAL_FILE = 'data/journal_entries.json'

def load_entries():
    if not os.path.exists(JOURNAL_FILE):
        return []
    with open(JOURNAL_FILE, 'r') as f:
        return json.load(f)

def save_entry(entry):
    entries = load_entries()
    entries.append(entry)
    with open(JOURNAL_FILE, 'w') as f:
        json.dump(entries, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/relax')
def relax():
    return render_template('relax.html')

@app.route('/mood')
def mood():
    return render_template('mood.html')

@app.route('/journal', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        content = request.form['entry']
        save_entry({'content': content})
        return redirect(url_for('journal'))
    entries = load_entries()
    return render_template('journal.html', entries=entries)

@app.route('/connect')
def connect():
    return render_template('connect.html')

if __name__ == '__main__':
    app.run(debug=True)
