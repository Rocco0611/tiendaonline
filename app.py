from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    items = [
        {"name": "Camisa Azul", "price": "$40", "image": "https://images.unsplash.com/photo-1521747116042-bb8d3f0c25e4"},
        {"name": "Vestido Bohemio", "price": "$70", "image": "https://images.unsplash.com/photo-1511341426035-dbbf6dbe3003"},
        {"name": "Chaqueta Vintage", "price": "$120", "image": "https://images.unsplash.com/photo-1594220287445-75efbb505bbb"}
    ]
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)
