from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Khởi tạo ứng dụng Flask
app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app2)

# Mô hình Book trong database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

# Tạo database nếu chưa có
with app2.app_context():
    db.create_all()

# GET: Lấy danh sách sách
@app2.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = [{"id": b.id, "title": b.title, "author": b.author} for b in books]
    return jsonify(result)

# POST: Thêm sách mới
@app2.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added", "book_id": new_book.id}), 201

# PUT: Cập nhật sách
@app2.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    book.title = data['title']
    book.author = data['author']
    db.session.commit()
    return jsonify({"message": "Book updated"})

# DELETE: Xóa sách
@app2.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})

# Chạy app
if __name__ == '__main__':
    app2.run(debug=True)
