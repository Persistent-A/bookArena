# Assignment 2 - Flask Application
    An application to CREATE, RETRIEVE and DELETE informations regarding Book - bookArena

            Name                   STUDENT-ID 
            
        Apurva Apurva             -  2030407
    Mineshkumar Dayalbhai Tandel  -  2110050



# FLASK MODULE

flask is a website application development module, based on python interpreter.</br>
It consists of FLASK class, which has it's instances</br><br>


## Installation

1. Make a folder where you can setup all your web applications setting, such as here environmentSettings;</br>
    and then perform the below code in terminal of that folder
    
    ```bash
    mkdir venv #Creates a folder for virtual environment
    python3 -m venv venv #storing virtual environment to venv folder
    ```

2. Activation of virtual environment.

    ```bash
    . venv/bin/activate
    ```

3. flask has it's dependency. When you install flask it installs other dependencies as well.</br>
   Other optionaal dependencies can be installed externally.

   such as FLASK ENVIRONMENT as a development for development purpose

    ```bash
    echo FLASK_ENV = development > .env # stores flask environment as development mode
    pip install python-dotenv # execute environment mentioned in .env file
    ```

4. After setting the environments required for flask</br>
   we can install flask

    ```bash
    pip install flask
    ```

5. Know the installed modules and their version

    pip freeze is used to store the installed modules in a perticular with with it's versions
    
    ```python
    pip freeze > requirements.txt
    ``` 
    <br>


## FLASK RUN
    
1. If we have given our flask app a name app.py and wsgi.py we can run our app by instructing the terminal as below
    
    ```bash
    flask run
    ```

2. In case if the fileName-('hello.py' here) is different the instruction to terminal will be as below

    ```bash
    export FLASK_APP=hello
    flask run
    ```
    <br>

## DATABASE CONNECTION 

    Flask does not have database linked with it, it is design decision upto the requirement of user.
    Python comes with in-built database SQLite3, we just need to create connection with our flask application to use it.<br/>
    Everytime,  when it is requirement for database, just reinstate a connection with it.
    SQLAlchemy is a database toolkit provided by SQLite3 which provides usefull defaults and extra helpers to make the work easier to accomplish.
    Below are the steps for creating connection to it</br><br>

1. SQLALCHEMY_DATABASE_URI: To create the connection with database, database URI is used. URI stands for Unified Resource Identifier which consists of URL and URN.

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_record.db' : 
    ```
2. SQLALCHEMY_TRACK_MODIFICATIONS: The default value of SQLALCHEMY_TRACK_MODIFICATIONS is None, which enables object modification tracking followed by warnings stating that it will be disabled in future. This uses extra memory, and hence, to refrain SQLALCHEMY_TRACK_MODIFICATIONS is explicitly set to False.

    ```python
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    ```
3. A callback is used to initialize the application for the use with database setup.

    ```python
    db.init_app(app)
    ```
    <br>

## CREATING THE APPLICATION

1. A route to initialize the database is setup

    ```python
    @app.route('/init')     
    def init():
        db.create_all()
        return 'DB initialized'
    ```

    create_all(): It creates all tables, here it is stored in books_record.db.<br><br>

2. Different templates are created to add functionality in the application. Here, we have created base.html which is the root and it is extended when other html are created.<br><br>

3. Creating Home page route:<br>
Endpoint: **'/'**<br>
At first when the request method is GET, it redirects to the webpage stored as base.html <br>
And then, when the request method is POST, it redirects to the webpage stored as library.html as per the search keyword that can be either title, author or genre of the book.<br><br>

4. To Add Book Information To The Database:<br>
Endpoint: **'/addBook'**<br>
In order to add Book's content to the database, at request method == 'POST', a form asking the details of the books is redirected, after filling the form, followed by submit, the new content is added to the database. 
```python
    db.session.add(book_add)
    db.session.commit()
``` 
<br>

5. To Get All The Books From The Database:<br>
Endpoint: **'/library'**
At first the builtins are stored in the variable name data, the data is feeded to the template, inside a function, which returns to redirects to the template : **library.html**. <br><br>

6. To Get The Book Details by author name <br>
Endpoint: **'/authors/<author_Name>'** <br><br><br>

## FILE STRUCTURE

File structure playes an important role in Flask Application
Flask MOdule looks for templates in templates directories and css file in Static directory.
Therefore following file structure convention is imperative to prevent conflicting behaviour of the app.


    ├── static
    │   └── css 
    │        └──style.css           --- Stores styling instructions
    ├── templates
    │   ├── addBook.html            --- Contains a form to get data about new book
    │   ├── base.html               --- Layout for the entire application, it is extended to other templates 
    │   ├── deleteBook.html         --- Contains a form to get data to delete a book
    │   ├── filterByPrice.html      --- Form which provides input fields to take minimum and maximum price to filter books as per the range
    │   ├── library.html            --- Contains a layout to display the data based on various search parameter
    │   └── macros.html             --- macros are a saparated code snippet to use it in different templates
    ├── venv                        --- It contains virtual environment to support app functionality      
    ├── .env                        --- .env contains a FLASK_APP=development variable, to support development mode of the application
    ├── app.py                      --- It conatains routes for different tasks as well as database connection instructions
    ├── model.py                    --- Database structure definition
    ├── books_record.db             --- A database file
    ├── requirements.txt            --- To know the used modules, packages and libraries along with it's version    
    └── readme.md                




# USER GUIDE

bookArena is a web based application, which facilitates a user to perform below mentioned tasks:
1. RETRIEVE BOOKS ON THE BASIS OF TITLE, AUTHOR AND GENRE 
2. RETRIEVE ALL THE BOOKS FROM THE COLLECTION
3. RETRIEVE BOOKS BY PRICE RANGE 
4. ADD INFORMATION OF A BOOK
5. DELETE A BOOK BY IT'S TITLE

## ENDPOINTS

1. RETRIEVE BOOKS ON THE BASIS OF TITLE, AUTHOR AND GENRE 

    Search through all the books in the database based on title, author and genre:<br>
    
    URL as per title: <br>
    Example: http://127.0.0.1:5000/books/Overthinking where Overthinking is the title of the book.
    
    URL as per author: <br>
    Example: http://127.0.0.1:5000/authors/Eckhart-Tolle where Eckhart Tolle is the author of the book.
    
    URL as per genre: <br>
    Example: http://127.0.0.1:5000/genres/Psychology where Psychology is the genre of the book.<br><br>

2. RETRIEVE ALL THE BOOKS FROM THE COLLECTION

    Collection of the books can be accessed through below URL<br>
    Endpoint: /library<br>
    URL : http://127.0.0.1:5000/library<br><br>

3. RETRIEVE BOOKS BY PRICE RANGE 

    Based on Price range - minimum and maximum price, the application allows a user to filter books <br>
    endpoint: **/filterByPrice**<br>
    URL : http://127.0.0.1:5000/filterByPrice<br><br>    

4. ADD INFORMATION OF A BOOK

    A user can add a book and its information to database: <br>
    Endpoint: **/addBook**<br>
    URL : http://127.0.0.1:5000/addBook<br><br>   

5. DELETE A BOOK BY IT'S TITLE

    To delete a book and it's details use below endpoint/URL <br>
    Endpoint: **/deleteBook**<br>
    URL : http://127.0.0.1:5000/deleteBook<br><br>   




