from storage import initialize_storage

from reading_manager import (
    add_book,
    view_books,
    search_books,
    filter_books_by_status,
    update_reading_progress,
    mark_book_completed,
    delete_book,
    show_statistics
)

from utils import get_valid_integer, get_valid_id


def display_menu():
    print("\n========== PERSONAL READING TRACKER ==========")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Filter Books by Status")
    print("5. Update Reading Progress")
    print("6. Mark Book as Completed")
    print("7. Delete Book")
    print("8. Reading Statistics")
    print("9. Exit")
    print("==============================================")


def main():
    initialize_storage()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            total_pages = get_valid_integer(
                "Enter total pages: ",
                minimum=1
            )
            genre = input("Enter book genre: ").strip()

            if not title or not author:
                print("Book title and author are required.")
                continue

            add_book(title, author, total_pages, genre)

        elif choice == "2":
            view_books()

        elif choice == "3":
            keyword = input(
                "Enter book title or author name: "
            ).strip()

            search_books(keyword)

        elif choice == "4":
            print("\n1. To Read")
            print("2. Reading")
            print("3. Completed")

            status_choice = input(
                "Select reading status: "
            ).strip()

            statuses = {
                "1": "To Read",
                "2": "Reading",
                "3": "Completed"
            }

            if status_choice in statuses:
                filter_books_by_status(
                    statuses[status_choice]
                )
            else:
                print("Invalid status choice.")

        elif choice == "5":
            book_id = get_valid_id("Enter book ID: ")

            current_page = get_valid_integer(
                "Enter current page: ",
                minimum=0
            )

            update_reading_progress(
                book_id,
                current_page
            )

        elif choice == "6":
            book_id = get_valid_id(
                "Enter book ID to mark completed: "
            )

            mark_book_completed(book_id)

        elif choice == "7":
            book_id = get_valid_id(
                "Enter book ID to delete: "
            )

            delete_book(book_id)

        elif choice == "8":
            show_statistics()

        elif choice == "9":
            print("Thank you for using Personal Reading Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
