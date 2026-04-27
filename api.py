
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
        select.geometry("4000x3000")
        instruct = tk.Label(select, text="Multiple books found. Please select one:")
        instruct.grid(row=0, column=0, padx=5, pady=5)
        "creates new gui to select book if multiple books are found"
        def next_page():
            nonlocal data 
            response = requests.get(data["next"])
            data = response.json()
            for widget in select.winfo_children():
                widget.destroy()
            selectB()
        def selectB():
            r = 1
            c = 1
            for i in data["results"]:
                button = tk.Button(select, text=i["title"],wraplength=300, command=lambda b=i: [labels(b), select.destroy()])
                button.grid(row=r, column=c, padx=5, pady=5)
                r += 1
                if r > 20:
                    r = 1
                    c += 1
            if data.get("next"):
                next_button = tk.Button(select, text="Next", command=next_page )
                next_button.grid(row=r, column=c, padx=5, pady=5)
        selectB()
    title_label = tk.Label(book, text=f"Title: ", wraplength=300)
    title_label.pack(pady=5)
    author_label = tk.Label(book, text=f"Author: ", wraplength=300)
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
