
# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)
books = {}

html = '''
<h2>Library Management System</h2>
<form method="post">
Book ID: <input name="id"><br>
Name: <input name="name"><br>
Author: <input name="author"><br>
Qty: <input name="qty"><br>
<button>Add Book</button>
</form>
<h3>Books</h3>
{{books}}
'''

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        books[request.form["id"]] = {
            "name": request.form["name"],
            "author": request.form["author"],
            "qty": request.form["qty"]
        }
    return render_template_string(html, books=books)

if __name__ == "__main__":
    app.run(debug=True)
