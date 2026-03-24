from flask import Flask, request, render_template, jsonify, redirect, url_for
import os
import json

app = Flask(__name__)

# Data file used by the Flask UI
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, 'reading_list.json')

def load_list():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as fh:
        try:
            return json.load(fh)
        except Exception:
            return []

def save_list(lst):
    with open(DATA_FILE, 'w', encoding='utf-8') as fh:
        json.dump(lst, fh, ensure_ascii=False, indent=2)


@app.route('/')
def index():
    return render_template('reading_list.html')


@app.route('/api/list', methods=['GET'])
def api_list():
    return jsonify(load_list())


@app.route('/add-book', methods=['POST'])
def add_book():
    title = request.form.get('title', '').strip()
    author = request.form.get('author', '').strip()
    notes = request.form.get('notes', '').strip()
    status = request.form.get('status', 'n')

    # don't add empty titles
    if not title:
        return redirect(url_for('index'))

    lst = load_list()
    title_key = title.strip().lower()
    # check for duplicate title (case-insensitive)
    for item in lst:
        if not item:
            continue
        existing_title = item[0] if len(item) > 0 else ''
        if existing_title.strip().lower() == title_key:
            # duplicate found; skip adding
            return redirect(url_for('index'))

    lst.append([title, author, notes, status])
    save_list(lst)

    return redirect(url_for('index'))


@app.route('/update-book', methods=['POST'])
def update_book():
    idx = request.form.get('index')
    status = request.form.get('status', 'n')
    if idx is None or idx == '':
        return redirect(url_for('index'))
    try:
        i = int(idx)
    except ValueError:
        return redirect(url_for('index'))

    lst = load_list()
    if 0 <= i < len(lst):
        item = lst[i]
        while len(item) < 4:
            item.append('')
        item[3] = status
        lst[i] = item
        save_list(lst)

    return redirect(url_for('index'))


@app.route('/delete-book', methods=['POST'])
def delete_book():
    idx = request.form.get('index')
    if idx is None or idx == '':
        return redirect(url_for('index'))
    try:
        i = int(idx)
    except ValueError:
        return redirect(url_for('index'))

    lst = load_list()
    if 0 <= i < len(lst):
        lst.pop(i)
        save_list(lst)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
