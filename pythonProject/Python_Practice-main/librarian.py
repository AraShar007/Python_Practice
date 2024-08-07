from prettytable import PrettyTable
class Librarian:
    def __init__(self, connection):
        self.connection = connection

    def check_librarian(self, lib_id, password):
        cursor = self.connection.cursor()
        cursor.execute("Select * from librarian where lib_id = %s and password = %s", (lib_id, password))
        row = cursor.fetchone()

        if row is None:
            print(f"Librarian with id {lib_id} does not exist or password is incorrect.")
            return False
        else:
            print(f"Librarian {row[1]} logged in:")
            return True

    def add_book(self, bid, title, author):
        try:
            cursor = self.connection.cursor()
            cursor.execute("Select * from  books where bid = %s", (bid,))
            existing_book = cursor.fetchone()

            if existing_book:
                cursor.execute("Update books set availability_count = availability_count + 1 where bid = %s", (bid,))
            else:
                cursor.execute("Insert into books (bid, title, author, status, availability_count) values (%s, %s, %s, True, 1)", (bid, title, author))

            self.connection.commit()
            print(f"Book '{title}' added successfully.")
        except Exception as e:
            print(f"Error in adding: {e}")
            return None

    # def update_book_status(self, bid, status):
    #     try:
    #         cursor = self.connection.cursor()
    #         cursor.execute("Update books set status = %s where bid = %s", (status, bid))
    #         self.connection.commit()
    #         print("Book status updated successfully.")
    #     except Exception as e:
    #         print(f"Error in updating: {e}")
    #         return None

    def remove_book(self, bid):
        try:
            cursor = self.connection.cursor()
            cursor.execute("Select availability_count from books where bid = %s", (bid,))
            availability_count = cursor.fetchone()[0]

            if availability_count > 1:
                cursor.execute("Update books set availability_count = availability_count - 1 where bid = %s", (bid,))
            else:
                cursor.execute("Delete from books where bid = %s", (bid,))

            self.connection.commit()
            print("Book removed successfully.")
        except Exception as e:
            print(f"Error in removing: {e}")
            return None

    def view_books(self):
        cursor = self.connection.cursor()
        cursor.execute("Select * from books")
        books = cursor.fetchall()
        if books:
            table = PrettyTable()
            table.field_names = ["Book ID", "Name", "Author", "Status", "Availability Count"]
            for book in books:
                status = 'Available' if book[3] else 'Not Available'
                if book[4] == 0 and book[3] != False:
                    status = 'Not Available'
                    cursor.execute("Update books set status = FALSE where bid = %s", (book[0],))
                    self.connection.commit()
                elif book[4] > 0 and book[3] != True:
                    status = 'Available'
                    cursor.execute("Update books set status = TRUE where bid = %s", (book[0],))
                    self.connection.commit()
                table.add_row([book[0], book[1], book[2], status, book[4]])
            print(table)



