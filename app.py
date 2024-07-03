from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# Konfiguracja MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'LibraryDB'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/authors')
def authors():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM Authors")
    authors = cursor.fetchall()
    return render_template('authors.html', authors=authors)

@app.route('/author/<int:author_id>')
def books_by_author(author_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("""
        SELECT Books.Title, Authors.FirstName, Authors.LastName, Books.PublishedYear
        FROM Books, Authors
        WHERE Books.AuthorID = Authors.AuthorID and Authors.AuthorID = %s
    """, (author_id,))
    data = cursor.fetchall()
    return render_template('books_by_author.html', data=data)


@app.route('/books')
def books():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("""
        SELECT CONCAT(a.FirstName, ' ', a.LastName) AS Author, b.Title, 
        g.GenreName As Genre, b.PublishedYear
        FROM Books b
        JOIN Authors a ON b.AuthorID = a.AuthorID
        JOIN BookGenres bg ON b.BookID = bg.BookID
        JOIN Genres g ON bg.GenreID = g.GenreID
        ORDER BY b.BookID;
    """)
    books = cursor.fetchall()
    return render_template('books.html', books=books)


@app.route('/members')
def members():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM Members")
    members = cursor.fetchall()
    return render_template('members.html', members=members)

@app.route('/member/<int:member_id>')
def loans_by_member(member_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("""
        SELECT Books.Title, Authors.FirstName, Authors.LastName,
        Loans.LoanDate,Loans.ReturnDate 
        FROM Members, Loans, Books, Authors
        WHERE Loans.MemberID = Members.MemberID and Books.BookID = Loans.BookID
        and Authors.AuthorID = Books.AuthorID and Loans.MemberID = %s;
    """, (member_id,))
    data = cursor.fetchall()
    return render_template('loans_by_member.html', data=data)


@app.route('/loans')
def loans():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM Loans")
    loans = cursor.fetchall()
    return render_template('loans.html', loans=loans)

@app.route('/loans_ranking')
def loand_ranking():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("""
        SELECT m.FirstName, m.LastName, COUNT(*) AS NumberOfLoans
        FROM Members m
        JOIN Loans l ON m.MemberID = l.MemberID
        GROUP BY m.FirstName, m.LastName
        ORDER BY NumberOfLoans DESC;
    """)
    loans = cursor.fetchall()
    return render_template('loans.html', loans=loans)


@app.route('/genres')
def genres():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM Genres")
    genres = cursor.fetchall()
    return render_template('genres.html', genres=genres)

if __name__ == '__main__':
    app.run(debug=True)
