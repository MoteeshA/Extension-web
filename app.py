from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

# Home page (your full HTML file)
@app.route("/")
def home():
    return render_template("index.html")

# Serve extension file
@app.route("/Extension.zip")
def download_extension():
    return send_from_directory(".", "Extension.zip", as_attachment=True)

# Serve source code zip
@app.route("/source-code.zip")
def download_source():
    return send_from_directory(".", "source-code.zip", as_attachment=True)

# Health check (Render uses this sometimes)
@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
