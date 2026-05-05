from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Preloaded 50 books
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Moby Dick", "author": "Herman Melville", "year": 1851},
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
]

# Add more books automatically to reach 50
for i in range(6, 51):
    books.append({
        "title": f"Sample Book {i}",
        "author": f"Author {i}",
        "year": 2000 + (i % 20)
    })


@app.route("/")
def home():
    return redirect(url_for("user_panel"))


# USER PANEL
@app.route("/user", methods=["GET"])
def user_panel():
    query = request.args.get("search", "")
    filtered_books = books

    if query:
        filtered_books = [
            book for book in books
            if query.lower() in book["title"].lower()
            or query.lower() in book["author"].lower()
        ]

    return render_template("user.html", books=filtered_books, query=query)


# ADMIN PANEL
@app.route("/admin", methods=["GET", "POST"])
def admin_panel():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]

        books.append({
            "title": title,
            "author": author,
            "year": int(year)
        })

        return redirect(url_for("admin_panel"))

    return render_template("admin.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)