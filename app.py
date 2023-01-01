#imported FLask class from flask module, and instance of this class will be WSGI application
from flask import Flask, redirect, render_template, request, url_for 
from model import Books, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_record.db' #The database URI that should be used for connection.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To prevent object modification warnings as wwell as excess memory usage for that.
db.init_app(app) # To initialize the application for use with this database setup.


# Route to initialize database before using the app
@app.route('/init')     
def init():
    db.create_all()
    return 'DB initialized'

# Home page route
@app.route("/", methods=['GET', 'POST'])
def home():
    # When requesting the response from the route, it will render webpage stored as base.html
    if request.method == 'GET': 
        return render_template('base.html', title='Books Arena')

    else:
        """
        As base.html contains a form, on submiting it triggers post action method.
        on request.method == 'POST', the input field data will be stored and compared 
        to the database builtins, matched information will be then fetched and used to display it 
        through resultBySearch.html template
        """
        search_keyword = request.form['search_keyword']
        search_keyword_title =  Books.query.filter(Books.title.like(f"%{search_keyword}%")).all()
        search_keyword_author =  Books.query.filter(Books.author.like(f"%{search_keyword}%")).all()
        search_keyword_genre =  Books.query.filter(Books.genre.like(f"%{search_keyword}%")).all()

        if search_keyword_title:
            return render_template('library.html', books=search_keyword_title)
    
        elif search_keyword_author:
            return render_template('library.html', books=search_keyword_author)
        
        else:
            return render_template('library.html', books=search_keyword_genre)


# ROUTE TO ADD BOOK INFORMATION to database
@app.route('/addBook', methods=('POST', 'GET'))
def addBook():
    if request.method == 'GET':
        return render_template('addBook.html', title='This is about Page')
    else:
        book_title = request.form['title']
        book_author = request.form['author']
        book_genre = request.form['genre']
        book_descriptiion = request.form['description']
        book_price = request.form['price']
        # Creating an object(builtin) based on the information given by user in abbBook.html webpage.
        book_add = Books(title=book_title, author=book_author, genre=book_genre, description=book_descriptiion, price=book_price)
        # Insertion of the object to batabase
        db.session.add(book_add)
        # Storing the changes
        db.session.commit()
        return redirect(url_for('library'))

# ROUTE TO GET ALL THE BOOKS from database
@app.route('/library', methods=['GET', 'POST'])
def library():
    data = Books.query.all() # Stores all the builtins to data
    return render_template('library.html', title='LIBRARY', books=data)


# TO GET BOOKS BY AUTHOR directly using URL
@app.route('/authors/<author_Name>')
def getBookByAuthor(author_Name):
    author_Name = author_Name.replace('-', ' ')
    data = Books.query.filter(Books.author == author_Name).all()
    return render_template('library.html', books=data)


# TO GET BOOKS BY NAME directly using URL
@app.route('/books/<book_Name>') #Enter book name with '-' instead of ' ' (space)
def getBookByName(book_Name):
    # To avoid url's limitation - URL does not takes space 
    book_Name = book_Name.replace('-', ' ') 
    # Only storing the builtins matching the book name given
    data = Books.query.filter(Books.title == book_Name).all()
    # books=data used to parse the builtins stored in data to the template
    return render_template('library.html', title='BOOKS BY NAME', books=data) 


# TO GET BOOKS BY GENRE directly using URL
@app.route('/genres/<book_Genre>')
def getBooksByGenre(book_Genre):
    book_Genre = book_Genre.replace('-', ' ')
    #  Data corresponding genre given
    data = Books.query.filter(Books.genre == book_Genre).all()
    return render_template('library.html', title='BOOKS BY Genre', books=data)


# ROUTE TO FILTER BOOKS BY PRICE
@app.route('/filterByPrice', methods=['GET', 'POST'])
def filterByPrice():
    if request.method == 'GET':
        return render_template('filterByPrice.html') 

    else:
        min_entered_price = request.form['priceMin']
        max_entered_price = request.form['priceMax']

        # To get builtins based on more than one parameter, Use filter method with arguments saparated by ',' (comma)
        data = Books.query.filter(Books.price <= max_entered_price, Books.price >= min_entered_price).all()
        return render_template('library.html', books=data)


# ROUTE TO DELETE A BOOK from database
@app.route('/deleteBook', methods=['GET', 'POST'])
def deleteBook():
    if request.method == 'GET':
        # Renders form to fetch information from user 
        return render_template('deleteBook.html')
    else:
        book_title = request.form['delete']
        data = Books.query.filter(Books.title == book_title).first()
        # Instruction to delete A book object retrieved based on it's title
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('library'))