from flask import Flask, request, redirect, render_template
import random
import string
from models import (
    init_db,
    insert_url,
    get_url,
    get_all_urls,
    increment_visit_count,
    delete_url_by_code
)

app = Flask(__name__)
init_db()

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']

        while True:
            short_code = generate_short_code()
            try:
                insert_url(original_url, short_code)
                break
            except Exception as e:
                if "UNIQUE constraint failed" in str(e):
                    continue
                else:
                    raise e

        return redirect('/')
    
    all_urls = get_all_urls()
    return render_template('index.html', all_urls=all_urls)


@app.route('/<short_code>')
def redirect_to_original(short_code):
    data = get_url(short_code)
    if data:
        original_url = data[1]
        increment_visit_count(short_code)
        return redirect(original_url)
    else:
        return "Invalid short code", 404

@app.route('/delete/<short_code>', methods=['POST'])
def delete(short_code):
    delete_url_by_code(short_code)
    return redirect('/')

if __name__ == '__main__':
    app.run(
        debug=True,
        host= '0.0.0.0',
        port=8000
    )

