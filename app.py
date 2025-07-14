from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Webhook received:", data)

    direction = data.get("direction")
    symbol = data.get("symbol")
    lot = data.get("lot")

    if direction == "buy":
        print(f"🟢 EMA BUY → Symbol: {symbol}, Lot: {lot}")
        # ⏳ Future: send buy command to MT5 here

    elif direction == "sell":
        print(f"🔴 EMA SELL → Symbol: {symbol}, Lot: {lot}")
        # ⏳ Future: send sell command to MT5 here

    else:
        print("⚠ Unknown direction received:", direction)

    return "OK", 200

# 🟢 THIS PART IS REQUIRED FOR RENDER.COM
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
