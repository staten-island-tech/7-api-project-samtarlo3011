
import tkinter as tk
import requests

def book_info():
    book = tk.Tk()
    book.title("Book Info")
    book.geometry("4000x3000")
    entry = tk.Entry(book, width=30)
    entry.pack(pady=10)
    "creates gui with a title and input box"
    def getinfo():
        title = entry.get()
        response = requests.get(f"https://gutendex.com/books?search={title}")
        data = response.json()
        return data
        "gets all book titles with the search term"
    def select_book():
        data = getinfo()
        select = tk.Toplevel()
        select.title("Select Book")
        select.geometry("400x300")
        instruct = tk.Label(select, text="Multiple books found. Please select one:")
        instruct.pack(pady=5)
        "creates new gui to select book if multiple books are found"
        def selectB():
            for i in data["results"]:
                button = tk.Button(select, text=i["title"], command=lambda b=i: labels(b))
                button.pack(pady=5)
        selectB()
    title_label = tk.Label(book, text=f"Title: ")
    title_label.pack(pady=5)
    author_label = tk.Label(book, text=f"Author: ")
    author_label.pack(pady=5)
    summary_label = tk.Label(book, text=f"Summary: ", wraplength=350)
    summary_label.pack(pady=5)
    def labels(book_data):
        info = getinfo()
        if info:
            title_label.config(text=f"Title: {book_data['title']}")
            author_label.config(text=f"Author: {book_data['authors'][0]['name']}")
            summary_label.config(text=f"Summary: {book_data['summaries'][0] if book_data['summaries'] else 'No summary available.'}")
        else:
            print("Book not found.")
    search = tk.Button(book, text="Search", command=select_book)
    search.pack(pady=10)
    book.mainloop()
book_info()
