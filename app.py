from flask import Flask, render_template, request

app = app

properties = [
    {
        "id": 1,
        "title": "3 beds • 2 baths",
        "price": 142900,
        "location": "Ibadan",
        "image": "house1.jpg",
        "type": "House"
    },
    {
        "id": 2,
        "title": "4 beds • 3 baths",
        "price": 149000,
        "location": "Lagos",
        "image": "house2.jpg",
        "type": "Land"
    },
    {
        "id": 3,
        "title": "2 beds • 1 bath",
        "price": 128700,
        "location": "Ibadan",
        "image": "house3.jpg",
        "type": "House"
    }
]

@app.route("/")
def home():
    query = request.args.get("q", "").lower()
    max_price = request.args.get("price")

    filtered = properties

    if query:
        filtered = [p for p in filtered if query in p["location"].lower()]

    if max_price:
        filtered = [p for p in filtered if p["price"] <= int(max_price)]

    return render_template("index.html", properties=filtered)
