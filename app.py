import os
from flask import Flask, send_from_directory, render_template, abort

app = Flask(__name__, static_folder='static')

# If your template is templates/web.html (as you currently have), use web.html
TEMPLATE_NAME = os.environ.get("TEMPLATE_NAME", "web.html")  # change to index.html if you rename

@app.route("/")
def home():
    try:
        return render_template(TEMPLATE_NAME)
    except Exception:
        # Helpful error if template missing
        abort(500, description=f"Template '{TEMPLATE_NAME}' not found in templates/")

# Serve the extension zip from repo root
@app.route("/Extension.zip")
def extension():
    zip_path = os.path.join(app.root_path, "Extension.zip")
    if not os.path.isfile(zip_path):
        abort(404)
    return send_from_directory(app.root_path, "Extension.zip", as_attachment=True)

# Serve the source code zip from repo root
@app.route("/source-code.zip")
def source_code():
    zip_path = os.path.join(app.root_path, "source-code.zip")
    if not os.path.isfile(zip_path):
        abort(404)
    return send_from_directory(app.root_path, "source-code.zip", as_attachment=True)

# Health check for Render / uptime monitors
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Render (and many platforms) set PORT environment variable for you.
    port = int(os.environ.get("PORT", 5010))
    host = "0.0.0.0"
    print(f"Starting Flask on http://{host}:{port} (template={TEMPLATE_NAME})")
    app.run(host=host, port=port)
