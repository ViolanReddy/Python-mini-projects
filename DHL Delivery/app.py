from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    dashboard_stats = {
        "total_parcels": 128,
        "pending_deliveries": 24,
        "completed_deliveries": 89,
        "vehicles_available": 6
    }

    #Sample shipments
    recent_shipments = [
        {
            "waybill": "DHL10001",
            "customer": "John Smith",
            "destination": "Cape Town",
            "weight": 12,
            "status": "In Transit"
        },
        {
            "waybill": "DHL10002",
            "customer": "Sarah Johnson",
            "destination": "Johannesburg",
            "weight": 8,
            "status": "Delivered"
        },
        {
            "waybill": "DHL10003",
            "customer": "Michael Brown",
            "destination": "Pretoria",
            "weight": 25,
            "status": "Pending"
        },
        {
            "waybill": "DHL10004",
            "customer": "Emily Davis",
            "destination": "Gqeberha",
            "weight": 15,
            "status": "In Transit"
        }
    ]
    
    return render_template(
        "index.html",
        stats=dashboard_stats,
        shipments=recent_shipments
    )


if __name__ == "__main__":
    app.run(debug=True)