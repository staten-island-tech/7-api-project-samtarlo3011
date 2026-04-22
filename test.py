from logging import info
import tkinter as tk
import requests

response = requests.get(f"https://gutendex.com/books?search=frankenstein")
data = response.json()
print(data)