from flask import Flask, request

app = Flask(_name_)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Webhook received:", data)

    direction = data.get("direction")
    symbol = data.get("symbol")
    lot = data.get("lot")

    if direction == "buy":
        print(f"🟢 EMA BUY → Symbol: {symbol}, Lot: {lot}")
        # 🧩 Future: MT5 Buy logic here

    elif direction == "sell":
        print(f"🔴 EMA SELL → Symbol: {symbol}, Lot: {lot}")
        # 🧩 Future: MT5 Sell logic here

    else:
        print("⚠ Unknown direction:", direction)

    return"OK",200
