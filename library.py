# library.py
# A simple command-line library tracker.

books = {}  # title -> {"author": str, "available": bool}

def show_menu():
    print("\n=== Library Tracker ===")
    print("0. Exit")
    print("1. Add book")

def add_book():
    title = input("Title: ")
    author = input("Author: ")

    if title in books:
        print(f'"{title}" is already in the library.')
    else:
        books[title] = {
            "author": author,
            "available": True
        }
        print(f'Added "{title}".')
        
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()