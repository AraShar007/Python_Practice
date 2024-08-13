from prettytable import PrettyTable
from student import Student
from user import User
class Librarian(User):
    def user_exists(self):
        cursor = self.connection.cursor()
        cursor.execute("Select * from user where user_id = %s and password = %s and user_role = 'librarian'", (self.user_id, self.password))
        row = cursor.fetchone()

        if row is None:
            print(f"Librarian with ID {self.user_id} does not exist or password is incorrect.")
            return False
        else:
            print(f"Librarian {row[1]} logged in.\n")
            return True

    def display_menu(self):
        print("Librarian Menu:")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. View Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Back to Login")
        print("8. Exit")

    def get_valid_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than 0. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        availability_count = self.get_valid_quantity()
        status = availability_count > 0

        cursor = self.connection.cursor()
        try:
            cursor.execute("Insert into books (title, author, status, availability_count) values (%s, %s, %s, %s)",
                (title, author, status, availability_count))
            self.connection.commit()
            print("Book added successfully.")
        except Exception as e:
            print(f"Error adding book: {e}")



    def update_book(self):
        bid = int(input("Enter book ID to update: "))
        availability_count = self.get_valid_quantity()
        cursor = self.connection.cursor()
        try:
            cursor.execute("Select availability_count FROM books WHERE bid = %s", (bid,))
            current_availability = cursor.fetchone()

            if current_availability is None:
                print("Book not found. Try adding it first")
                self.add_book()
                return

            new_availability_count = current_availability[0] + availability_count
            status = new_availability_count > 0

            cursor.execute("UPDATE books SET status = %s, availability_count = %s WHERE bid = %s",( status, new_availability_count, bid))
            self.connection.commit()
            print("Book updated successfully.")
        except Exception as e:
            print(f"Error updating book: {e}")

    def remove_book(self):
        bid = int(input("Enter book ID to remove: "))

        cursor = self.connection.cursor()
        try:
                cursor.execute("Delete from books where bid = %s", (bid,))
                cursor.execute("Delete from borrow_history where bid = %s", (bid,))
                self.connection.commit()
                print("Book removed successfully.")
        except Exception as e:
            print(f"Error removing book: {e}")

    def view_books(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        if books:
            table = PrettyTable()
            table.field_names = ["Book ID", "Title", "Author", "Status", "Availability Count"]
            for book in books:
                status = 'Available' if book[3] else 'Not Available'
                table.add_row([book[0], book[1], book[2], status, book[4]])
            print(table)
        else:
            print("No books found.")

    def issue_book(self):
        sid = input("Enter Student ID to issue book to: ")
        student = Student(self.connection, sid, None)
        student.view_borrow_history()

        self.view_books()
        bid = int(input("Enter Book ID to issue: "))

        try:
            cursor = self.connection.cursor()
            cursor.execute("Select * from borrow_history where sid = %s AND bid = %s AND is_returned = False",
                           (sid, bid))
            existing_borrow_record = cursor.fetchone()

            if existing_borrow_record:
                print(f"Student ID {sid} already borrowed this book {bid}.")
                return

            cursor.execute("Select status, availability_count from books where bid = %s", (bid,))
            book = cursor.fetchone()

            if book and book[0] and book[1] > 0:
                cursor.execute(
                    "INSERT INTO borrow_history (sid, bid, borrow_date, return_date, is_returned) VALUES (%s, %s, NOW(), DATE_ADD(NOW(), INTERVAL 15 DAY), False)",
                    (sid, bid))
                cursor.execute("Update books set availability_count = availability_count - 1 where bid = %s", (bid,))
                if book[1] - 1 == 0:
                    cursor.execute("Update books set status = FALSE where bid = %s", (bid,))
                self.connection.commit()
                print("Book issued successfully.")
            else:
                print("Book is not available.")
        except Exception as e:
            print(f"Error in issuing book: {e}")

    def return_book(self):
        sid = input("Enter Student ID to return book: ")
        student = Student(self.connection, sid, None)
        student.view_borrow_history()
        bid = int(input("Enter Book ID to return: "))
        try:
            cursor = self.connection.cursor()
            cursor.execute("Select hid from borrow_history where sid = %s AND bid = %s AND is_returned = False",
                           (sid, bid))
            borrow_record = cursor.fetchone()

            if not borrow_record:
                print(f"No active borrow record found for student ID {sid} and book ID {bid}.")
                return

            cursor.execute("Update borrow_history set return_date = NOW(), is_returned = True where hid = %s",
                           (borrow_record[0],))
            self.connection.commit()

            cursor.execute("Update books set availability_count = availability_count + 1 where bid = %s", (bid,))
            self.connection.commit()

            cursor.execute("Select availability_count from books where bid = %s", (bid,))
            availability_count = cursor.fetchone()[0]

            if availability_count > 0:
                cursor.execute("Update books set status = TRUE where bid = %s", (bid,))
                self.connection.commit()

            print(f"Book ID {bid} returned successfully by student ID {sid}.")
        except Exception as e:
            print(f"Error in returning book: {e}")




