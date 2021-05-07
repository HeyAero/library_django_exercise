# Library App using Django - Exercise /w Futureproof
Made by Aaron & Ravil

### Tasks(1):
- [x] Create a Django project with one app, 'library'
- [x] Add views and templates for a home and books show page (/ and /books/<id>)
- [x] The home page will list all the book titles
- [x] The show page will list the chosen book title and author
- [x] Show a custom 404 if book is not found
- [x] Use dummy data for now:

### Tasks(2):
- [x] Setup a 'library' database (your choice of db)
- [x] Create models for Book and Author
- [x] Authors have a name
- [x] Books have a title and a Foreign Key for author
- [x] Make and run migrations
- [x] Add your models to your admin dashboard and create some records in the GUI
- [x] Update your views to take data from the database instead of the dummy data list

### Tasks(3):
- [x] Create register, login and logout routes
- [x] Use the UserCreationForm to complete your templates
- [x] Register some new users via your registration form
- [x] Make the book show route only available to logged in users
- [x] Add a new field of 'borrower' to the Book model as a 
- [x] Foreign Key to User
- [x] In your admin dashboard, assign some books a borrower
- [x] Update your book show template to show if it is available to loan or not

### Tasks(4):
- [x] Create a new book form accessible at books/new
- [x] On success, the form redirects to the new book's show page
- [] Create a button on the book show page
- [] If the book is available, on clicking the button, the current User becomes the borrower of that book
- [] If the book is on loan by another User, current User sees disabled button
- [] If the book is on loan by the current User, on clicking the button, the book is returned