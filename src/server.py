from flask import Flask, jsonify, render_template, request
from datetime import datetime
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


@app.post("/print-report")
def print_report():
    unit_name = request.json["unit_name"]
    now = datetime.now()
    file_content = f"""-----------------------------
UNIT: {unit_name}
DATE: {now.strftime("%m/%d/%Y")}
TIME: {now.strftime("%H:%M:%S")}
-----------------------------
"""

    with open("/tmp/report.txt", "w") as file1:
        file1.write(file_content)

    conn = cups.Connection()
    job_id = conn.printFile(
        "hp-casa",
        "/tmp/report.txt",
        "Report",
        options={}
    )
    return {
            "job_id": job_id
    }


@app.route("/")
def render_index():
    return render_template("index.html")
