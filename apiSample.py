from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for testing
books = [
    {
        'id': 1,
        'book_name': 'Book 1',
        'author': 'Author 1',
        'publisher': 'Publisher 1'
    },
    {
        'id': 2,
        'book_name': 'Book 2',
        'author': 'Author 2',
        'publisher': 'Publisher 2'
    }
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        'id': len(books) + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['book_name'] = request.json.get('book_name', book['book_name'])
            book['author'] = request.json.get('author', book['author'])
            book['publisher'] = request.json.get('publisher', book['publisher'])
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run()
