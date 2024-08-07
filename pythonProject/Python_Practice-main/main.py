from database_connection import create_connection
from librarian import Librarian
from student import Student

def lib_main():
    connection = create_connection()
    if connection is None:
        return

    while True:
        print("--------------------------Welcome To My Library--------------------------")
        print("Main Menu:")
        print("\n1. Librarian\n2. Student\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            librarian = Librarian(connection)
            lib_id = input("Enter librarian ID: ")
            password = input("Enter password: ")

            if not librarian.check_librarian(lib_id, password):
                print("Returning back to main menu\n\n")
                continue

            while True:
                print("------------------------------------------------------------------------------------")
                print("Please Choose One")
                print("1. Add Book\n2. Remove Book\n3. View All Books\n4. Back to Main Menu")
                librarian_choice = input("Enter your choice: ")
                if librarian_choice == '1':
                    bid = input("Enter Book ID: ")
                    title = input("Enter book title: ")
                    author = input("Enter author: ")
                    librarian.add_book(bid, title, author)
                elif librarian_choice == '2':
                    bid = int(input("Enter book ID: "))
                    librarian.remove_book(bid)
                elif librarian_choice == '3':
                    librarian.view_books()
                elif librarian_choice == '4':
                    break
                else:
                    print("Invalid choice.")

        elif choice == '2':
            student = Student(connection)
            sid = input("Enter your student ID: ")
            password = input("Enter password: ")

            if not student.student_exists(sid, password):
                print("Returning to main menu \n\n")
                continue

            while True:
                print("\n1. Borrow Book\n2. Return Book\n3. Check Borrow History\n4. View All Books\n5. Back to Main Menu")
                student_choice = input("Select an option: ")
                if student_choice == '1':
                    bid = int(input("Enter book ID: "))
                    student.borrow_book(sid, bid)
                elif student_choice == '2':
                    bid = int(input("Enter book ID: "))
                    student.return_book(sid, bid)
                elif student_choice == '3':
                    student.view_borrow_history(sid)
                elif student_choice == '4':
                    student.view_books()
                elif student_choice == '5':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == '3':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

lib_main()
