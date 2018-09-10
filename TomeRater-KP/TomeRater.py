class User(object):
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email chabged to " + self.email)

    def __repr__(self):
        return "User " + self.name + ', email: ' + self.email + ", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        return (self.name == other_user.name) and (self.email == other_user.email)

    def read_book(self, book, rating = None):
        self.books.update({book: rating})

    def get_average_rating(self):
        rating = 0
        for value in self.books.values():
            if value != None:
                rating += value
        return rating / len(self.books)

class Book(object):

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN has been changed")

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __repr__(self):
        return self.title

    def get_average_rating(self):
        rating_sum = 0
        for item in self.ratings:
            rating_sum += item
        return rating_sum / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    
    def __init__(self, title, isbn, author):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)


class Non_Fiction(Book):
    
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level   = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater(object):
    
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        if self.uniq_isbn(isbn):
            book = Book(title, isbn)
            return book

    def create_novel(self, title, author, isbn):
        if self.uniq_isbn(isbn):
            novel = Fiction(title, isbn, author)
            return novel

    def create_non_fiction(self, title, subject, level, isbn):
        if self.uniq_isbn(isbn):
            non_fiction = Non_Fiction(title, subject, level, isbn)
            return non_fiction

    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email {}".format(email))

def add_user(self, name, email, user_books = None):
        if '@' in email and ('.com' in email or '.org' in email or '.edu' in email or '.gov' in email):
            new_user = User(name, email)
            if email not in self.users.keys():
                self.users[email] = new_user
            else:
                print("Email aready exists.")
            if user_books:
                for item in user_books:
                    self.add_book_to_user(item, email)
        else:
            print("Invalid email")
            
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
            
    def print_users(self):
        for user in self.users.values():
            print(user)
            
    def get_most_read_book(self):
        reads_num = 0
        book_num = None
        for book in self.books:
            reads = self.books[book]
            if reads >= reads_num:
                reads_num = reads
                book_num = book
        return book_num
    
    def highest_rated_book(self):
        rating_num = 0
        book_num = None
        for book in self.books:
            avg = book.get_average_rating()
            if avg >= rating_num:
                rating_num = avg
                book_num = book
        return book_num

    def get_most_positive_user(self):
        rating_num = 0
        user_num = None
        for book in self.users:
            avg = self.users[book].get_average_rating()
            if avg >= rating_num:
                rating_num = avg
                user_num = self.users[book]
        return user_num
