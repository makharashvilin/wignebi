from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": 1880},
    {"id": 2, "title": "The Metamorphosis", "author": "Franz Kafka", "year": 1915},
    {"id": 3, "title": "No Longer Human", "author": "Osamu Dazai", "year": 1948}
]


@app.route('/')
def home():
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>')
def book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    return render_template('book.html', book=book)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            'id': len(books) + 1,
            'title': request.form['title'],
            'author': request.form['author'],
            'year': request.form['year']
        }
        books.append(new_book)
        return render_template('index.html', books=books)
    return render_template('add_book.html')







if __name__ == '__main__':
    app.run(debug=True)