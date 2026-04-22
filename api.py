from logging import info
import tkinter as tk
import requests

def book_info():
    book = tk.Tk()
    book.title("Book Info")
    book.geometry("4000x3000")
    entry = tk.Entry(book, width=30)
    entry.pack(pady=10)
    def getbook():
        title = entry.get()
        response = requests.get(f"https://gutendex.com/books?search={title}")
        data = response.json()
        if int(data["count"]) > 1:
            select = tk.Tk()
            select.title("Select Book")
            select.geometry("400x300")
            instruct = tk.Label(select, text="Multiple books found. Please select one:")
            instruct.pack(pady=5)
            def select():
                for i in data["results"]:
                    id = i["id"]
                    return id
            for i in data["results"]:
                button = tk.Button(select, text=i["title"], command=)
                button.pack(pady=5)
    title_label = tk.Label(book, text=f"Title: ")
    title_label.pack(pady=5)
    author_label = tk.Label(book, text=f"Author: ")
    author_label.pack(pady=5)
    summary_label = tk.Label(book, text=f"Summary: ", wraplength=350)
    summary_label.pack(pady=5)
    def labels():
        info = getbook()
        if info:
            title_label.config(text=f"Title: {info['results'][id]['title']}")
            author_label.config(text=f"Author: {info['results'][id]['authors'][0]['name']}")
            summary_label.config(text=f"Summary: {info['results'][id]['summaries']}")
        else:
            print("Book not found.")
    search = tk.Button(book, text="Search", command=labels)
    search.pack(pady=10)
    book.mainloop()
book_info()
