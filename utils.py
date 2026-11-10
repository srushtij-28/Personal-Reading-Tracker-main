from datetime import date


def get_valid_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))

            if value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_valid_id(prompt):
    return get_valid_integer(prompt, minimum=1)


def get_reading_status(current_page, total_pages):
    if current_page >= total_pages:
        return "Completed"

    if current_page == 0:
        return "To Read"

    return "Reading"


def get_progress_percentage(current_page, total_pages):
    if total_pages <= 0:
        return 0

    return round((current_page / total_pages) * 100, 2)
