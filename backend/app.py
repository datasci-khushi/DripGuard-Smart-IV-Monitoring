from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "dripguard.db"


# =========================================================
# DATABASE
# =========================================================

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bed_id TEXT NOT NULL,
            drip_rate REAL NOT NULL,
            flow_rate REAL DEFAULT 0,
            bag_volume REAL DEFAULT 500,
            remaining_time REAL DEFAULT 0,
            status TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# =========================================================
# STATUS CALCULATION
# =========================================================

def calculate_status(drip_rate):

    if drip_rate <= 0:
        return "CRITICAL"

    elif drip_rate < 12:
        return "ATTENTION"

    else:
        return "NORMAL"


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return jsonify({
        "system": "DripGuard",
        "status": "Backend running",
        "message": "Flask server is working"
    })


# =========================================================
# RECEIVE ESP8266 READING
# =========================================================

@app.route("/api/readings", methods=["POST"])
def receive_reading():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "No JSON data received"
            }), 400

        bed_id = str(data.get("bed_id", "B01"))

        drip_rate = float(
            data.get("drip_rate", 0)
        )

        flow_rate = float(
            data.get("flow_rate", drip_rate * 0.05)
        )

        bag_volume = float(
            data.get("bag_volume", 500)
        )

        # Calculate remaining time
        if flow_rate > 0:
            remaining_time = bag_volume / flow_rate
        else:
            remaining_time = 0

        status = calculate_status(drip_rate)

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        conn = get_db()

        conn.execute("""
            INSERT INTO readings
            (
                bed_id,
                drip_rate,
                flow_rate,
                bag_volume,
                remaining_time,
                status,
                timestamp
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            bed_id,
            drip_rate,
            flow_rate,
            bag_volume,
            remaining_time,
            status,
            timestamp
        ))

        conn.commit()
        conn.close()

        return jsonify({
            "success": True,
            "bed_id": bed_id,
            "drip_rate": drip_rate,
            "flow_rate": flow_rate,
            "status": status,
            "remaining_time": remaining_time,
            "timestamp": timestamp
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# =========================================================
# GET LATEST READING FOR EACH BED
# =========================================================

@app.route("/api/latest", methods=["GET"])
def latest_readings():

    conn = get_db()

    rows = conn.execute("""
        SELECT *
        FROM readings
        WHERE id IN (
            SELECT MAX(id)
            FROM readings
            GROUP BY bed_id
        )
        ORDER BY bed_id
    """).fetchall()

    conn.close()

    readings = []

    for row in rows:

        readings.append({
            "id": row["id"],
            "bed_id": row["bed_id"],
            "drip_rate": row["drip_rate"],
            "flow_rate": row["flow_rate"],
            "bag_volume": row["bag_volume"],
            "remaining_time": row["remaining_time"],
            "status": row["status"],
            "timestamp": row["timestamp"]
        })

    return jsonify(readings)


# =========================================================
# GET HISTORY
# =========================================================

@app.route("/api/history", methods=["GET"])
def history():

    conn = get_db()

    rows = conn.execute("""
        SELECT *
        FROM readings
        ORDER BY id DESC
        LIMIT 100
    """).fetchall()

    conn.close()

    readings = []

    for row in rows:

        readings.append({
            "id": row["id"],
            "bed_id": row["bed_id"],
            "drip_rate": row["drip_rate"],
            "flow_rate": row["flow_rate"],
            "bag_volume": row["bag_volume"],
            "remaining_time": row["remaining_time"],
            "status": row["status"],
            "timestamp": row["timestamp"]
        })

    return jsonify(readings)


# =========================================================
# GET ALERTS
# =========================================================

@app.route("/api/alerts", methods=["GET"])
def alerts():

    conn = get_db()

    rows = conn.execute("""
        SELECT *
        FROM readings
        WHERE status != 'NORMAL'
        ORDER BY id DESC
        LIMIT 20
    """).fetchall()

    conn.close()

    alerts = []

    for row in rows:

        alerts.append({
            "id": row["id"],
            "bed_id": row["bed_id"],
            "drip_rate": row["drip_rate"],
            "status": row["status"],
            "timestamp": row["timestamp"]
        })

    return jsonify(alerts)


# =========================================================
# TEST DATA
# =========================================================

@app.route("/api/test", methods=["POST"])
def test_data():

    test_readings = [
        {
            "bed_id": "B01",
            "drip_rate": 20
        },
        {
            "bed_id": "B02",
            "drip_rate": 24
        },
        {
            "bed_id": "B03",
            "drip_rate": 9
        },
        {
            "bed_id": "B04",
            "drip_rate": 0
        }
    ]

    results = []

    conn = get_db()

    for item in test_readings:

        bed_id = item["bed_id"]
        drip_rate = item["drip_rate"]

        flow_rate = drip_rate * 0.05

        bag_volume = 500

        if flow_rate > 0:
            remaining_time = bag_volume / flow_rate
        else:
            remaining_time = 0

        status = calculate_status(drip_rate)

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        conn.execute("""
            INSERT INTO readings
            (
                bed_id,
                drip_rate,
                flow_rate,
                bag_volume,
                remaining_time,
                status,
                timestamp
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            bed_id,
            drip_rate,
            flow_rate,
            bag_volume,
            remaining_time,
            status,
            timestamp
        ))

        results.append({
            "bed_id": bed_id,
            "drip_rate": drip_rate,
            "flow_rate": flow_rate,
            "status": status
        })

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Test readings inserted",
        "readings": results
    })


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":

    init_database()

    print("---------------------------------------")
    print("DripGuard Flask Backend")
    print("---------------------------------------")
    print("Server: http://127.0.0.1:5000")
    print("Latest: http://127.0.0.1:5000/api/latest")
    print("History: http://127.0.0.1:5000/api/history")
    print("Alerts: http://127.0.0.1:5000/api/alerts")
    print("---------------------------------------")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
