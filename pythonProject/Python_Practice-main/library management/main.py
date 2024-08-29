from database_connection import create_connection
from librarian import Librarian
from student import Student


def lib_main():
    while True:
        connection = create_connection()
        if connection is None:
            return

        try:
            print("\n-------------Welcome to My Library---------------\n")
            user_id = input("Enter User ID: ")

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM user WHERE user_id = %s", (user_id,))
            user_exists = cursor.fetchone()[0]

            if not user_exists:
                print("User does not exist.\n")
                continue

            password = input("Enter Password: ")
            print()


            cursor.execute("SELECT user_role FROM user WHERE user_id = %s AND password = %s", (user_id, password))
            result = cursor.fetchone()

            if result:
                user_role = result[0]
                if user_role == 'librarian':
                    user = Librarian(connection, user_id, password)
                elif user_role == 'student':
                    user = Student(connection, user_id, password)
                else:
                    print("Invalid user type. Enter (librarian/student)\n")
                    continue

                if not user.user_exists():
                    print("User does not exist.\n")
                    continue

                while True:
                    user.display_menu()
                    choice = input("\nEnter your choice: ")

                    if user_role == 'librarian':
                        if choice == '1':
                            user.add_book()
                        elif choice == '2':
                            user.update_book()
                        elif choice == '3':
                            user.remove_book()
                        elif choice == '4':
                            user.view_books()
                        elif choice == '5':
                            user.issue_book()
                        elif choice == '6':
                            user.return_book()
                        elif choice == '7':
                            break
                        elif choice == '8':
                            print("Exiting the Library System...")
                            connection.close()
                            return
                        else:
                            print("Invalid choice. Please try again.\n")

                    if user_role == 'student':
                        if choice == '1':
                            user.borrow_book()
                        elif choice == '2':
                            user.return_book()
                        elif choice == '3':
                            user.view_borrow_history()
                        elif choice == '4':
                            user.view_books()
                        elif choice == '5':
                            break
                        elif choice == '6':
                            print("Exiting the Library System...")
                            connection.close()
                            return
                        else:
                            print("Invalid choice. Input should be in range (1-6)\n")
            else:
                print("Invalid credentials. Enter again\n")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

lib_main()


