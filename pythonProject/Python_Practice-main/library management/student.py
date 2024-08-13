from datetime import datetime
from prettytable import PrettyTable
from user import User
class Student(User):
    def user_exists(self):
        cursor = self.connection.cursor()
        cursor.execute("Select * from user where user_id = %s AND password = %s AND user_role = 'student'", (self.user_id, self.password))
        row = cursor.fetchone()

        if row is None:
            print(f"Student with ID {self.user_id} does not exist or password is incorrect.")
            return False
        else:
            print(f"Student {row[1]} logged in.\n")
            return True

    def display_menu(self):
        print("\nStudent Menu:")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View Borrow History")
        print("4. View Books")
        print("5. Back to Login")
        print("6. Exit")

    def borrow_book(self):
        sid = self.user_id
        self.view_books()
        bid = int(input("Enter book ID to borrow: "))

        try:
            cursor = self.connection.cursor()
            cursor.execute("Select * from borrow_history where sid = %s AND bid = %s AND is_returned = False", (sid, bid))
            existing_borrow_record = cursor.fetchone()

            if existing_borrow_record:
                print(f"Student ID {sid} already has this book borrowed.")
                return

            cursor.execute("Select status, availability_count from books where bid = %s", (bid,))
            book = cursor.fetchone()

            if book and book[0] and book[1] > 0:
                cursor.execute("INSERT INTO borrow_history (sid, bid, borrow_date, return_date, is_returned) VALUES (%s, %s, NOW(), DATE_ADD(NOW(), INTERVAL 15 DAY), False)", (sid, bid))
                cursor.execute("Update books set availability_count = availability_count - 1 where bid = %s", (bid,))
                if book[1] - 1 == 0:
                    cursor.execute("Update books set status = FALSE where bid = %s", (bid,))
                self.connection.commit()
                print("Book borrowed successfully.")
            else:
                print("Book is not available.")
        except Exception as e:
            print(f"Error in borrowing: {e}")

    def return_book(self):
        sid = self.user_id
        self.view_borrow_history()
        bid = int(input("Enter book ID to return: "))
        try:
            cursor = self.connection.cursor()
            cursor.execute("Select hid from borrow_history where sid = %s AND bid = %s AND is_returned = False", (sid, bid))
            borrow_record = cursor.fetchone()

            if not borrow_record:
                print(f"No active borrow record found for student ID {sid} and book ID {bid}.")
                return

            cursor.execute("Update borrow_history set return_date = NOW(), is_returned = True where hid = %s", (borrow_record[0],))
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

    def view_borrow_history(self):
        sid = self.user_id
        cursor = self.connection.cursor()
        cursor.execute("Select * from borrow_history where sid = %s ORDER BY is_returned", (sid,))
        history = cursor.fetchall()
        if not history:
            print("No borrow history found for this student.")
        else:
            for record in history:
                borrow_date = record[3].strftime('%d-%m-%Y') if record[3] else 'N/A'
                return_date = record[4].strftime('%d-%m-%Y') if record[4] else 'N/A'
                returned = 'Yes' if record[5] else 'No'
                print(f"History_ID: {record[0]}, Student_ID: {record[1]}, Book ID: {record[2]}, Borrow Date: {borrow_date}, Due Date: {return_date}, Returned: {returned}")

    def view_books(self):
        cursor = self.connection.cursor()
        cursor.execute("Select bid, title, author, status from books")
        books = cursor.fetchall()
        if books:
            table = PrettyTable()
            table.field_names = ["Book ID", "Title", "Author", "Status"]
            for book in books:
                status = 'Available' if book[3] else 'Not Available'
                table.add_row([book[0], book[1], book[2], status])
            print(table)
        else:
            print("No books found.")
