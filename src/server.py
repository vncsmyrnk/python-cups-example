from flask import Flask, jsonify
import cups


app = Flask(__name__)


@app.get("/printers-info")
def display_app_data():
    conn = cups.Connection()
    printers = conn.getPrinters()
    return jsonify(printers)


@app.route("/print-file")
def print_file():
    conn = cups.Connection()
    job_id = conn.printFile(
        "hp-casa",
        "/var/app/sample.pdf",
        "Default print",
        options={}
    )
    return {
            "job_id": job_id
    }
