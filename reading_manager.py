from datetime import date

from storage import load_books, save_books
from utils import get_reading_status, get_progress_percentage


def add_book(title, author, total_pages, genre):
    books = load_books()

    book_id = max(
        [book["id"] for book in books],
        default=0
    ) + 1

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "total_pages": total_pages,
        "current_page": 0,
        "genre": genre,
        "status": "To Read",
        "date_added": date.today().isoformat(),
        "date_completed": ""
    }

    books.append(book)
    save_books(books)

    print("\nBook added successfully!")


def view_books():
    books = load_books()

    if not books:
        print("\nNo books found.")
        return

    print("\n" + "-" * 100)
    print(
        f"{'ID':<5} {'Title':<25} {'Author':<20} "
        f"{'Pages':<12} {'Progress':<12} {'Status':<15}"
    )
    print("-" * 100)

    for book in books:
        progress = get_progress_percentage(
            book["current_page"],
            book["total_pages"]
        )

        page_text = (
            f"{book['current_page']}/{book['total_pages']}"
        )

        print(
            f"{book['id']:<5} "
            f"{book['title'][:24]:<25} "
            f"{book['author'][:19]:<20} "
            f"{page_text:<12} "
            f"{str(progress) + '%':<12} "
            f"{book['status']:<15}"
        )

    print("-" * 100)


def search_books(keyword):
    books = load_books()
    keyword = keyword.lower()

    results = [
        book for book in books
        if keyword in book["title"].lower()
        or keyword in book["author"].lower()
    ]

    display_books(results)


def filter_books_by_status(status):
    books = load_books()

    results = [
        book for book in books
        if book["status"] == status
    ]

    display_books(results)


def display_books(books):
    if not books:
        print("\nNo matching books found.")
        return

    print("\nMatching Books:")

    for book in books:
        progress = get_progress_percentage(
            book["current_page"],
            book["total_pages"]
        )

        print(
            f"\nID: {book['id']}"
            f"\nTitle: {book['title']}"
            f"\nAuthor: {book['author']}"
            f"\nGenre: {book['genre']}"
            f"\nPages: {book['current_page']}/{book['total_pages']}"
            f"\nProgress: {progress}%"
            f"\nStatus: {book['status']}"
            f"\nDate Added: {book['date_added']}"
            f"\nDate Completed: {book['date_completed'] or 'Not completed'}"
        )


def update_reading_progress(book_id, current_page):
    books = load_books()

    for book in books:
        if book["id"] == book_id:
            if current_page > book["total_pages"]:
                print(
                    f"Current page cannot exceed "
                    f"{book['total_pages']}."
                )
                return

            book["current_page"] = current_page
            book["status"] = get_reading_status(
                current_page,
                book["total_pages"]
            )

            if book["status"] == "Completed":
                book["date_completed"] = date.today().isoformat()
            else:
                book["date_completed"] = ""

            save_books(books)
            print("\nReading progress updated successfully!")
            return

    print("\nBook ID not found.")


def mark_book_completed(book_id):
    books = load_books()

    for book in books:
        if book["id"] == book_id:
            book["current_page"] = book["total_pages"]
            book["status"] = "Completed"
            book["date_completed"] = date.today().isoformat()

            save_books(books)
            print("\nBook marked as completed!")
            return

    print("\nBook ID not found.")


def delete_book(book_id):
    books = load_books()

    updated_books = [
        book for book in books
        if book["id"] != book_id
    ]

    if len(updated_books) == len(books):
        print("\nBook ID not found.")
        return

    save_books(updated_books)
    print("\nBook deleted successfully.")


def show_statistics():
    books = load_books()

    if not books:
        print("\nNo books available for statistics.")
        return

    total_books = len(books)

    completed_books = sum(
        1 for book in books
        if book["status"] == "Completed"
    )

    reading_books = sum(
        1 for book in books
        if book["status"] == "Reading"
    )

    to_read_books = sum(
        1 for book in books
        if book["status"] == "To Read"
    )

    total_pages_read = sum(
        book["current_page"] for book in books
    )

    average_progress = sum(
        get_progress_percentage(
            book["current_page"],
            book["total_pages"]
        )
        for book in books
    ) / total_books

    print("\n========== READING STATISTICS ==========")
    print(f"Total Books: {total_books}")
    print(f"Completed Books: {completed_books}")
    print(f"Currently Reading: {reading_books}")
    print(f"To Read: {to_read_books}")
    print(f"Total Pages Read: {total_pages_read}")
    print(f"Average Progress: {average_progress:.2f}%")
    print("========================================")
