from flask import Flask, render_template, request
from utils import load_and_prepare_data
from model import train_model
import torch

app = Flask(__name__)
X, y, label_encoder = load_and_prepare_data("dados/movies.csv")
model = train_model(X, y)

@app.route("/", methods=["GET", "POST"])
def index():
    recommended = None
    if request.method == "POST":
        inputs = []
        for f in ["Action", "Horror", "Drama", "Sci-Fi", "Thriller", "Comedy", "Romance"]:
            val = float(request.form.get(f))
            if val >= 0.5:
                val = 1
            else:
                val = 0
            inputs.append(val)
        input_tensor = torch.tensor([inputs], dtype=torch.float32)
        model.eval()
        with torch.no_grad():
            output = model(input_tensor)
            prediction = torch.argmax(output, dim=1)
            recommended = label_encoder.inverse_transform(prediction)[0]
    return render_template("index.html", recommended=recommended)

if __name__ == "__main__":
    app.run(debug=True)
