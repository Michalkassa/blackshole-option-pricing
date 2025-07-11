from flask import Flask, redirect, url_for, request, render_template
import BlackSholes
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        stock_price = float(request.form["asset_price"])
        time_to_maturity= float(request.form["time_to_maturity"])
        strike=float(request.form["strike_price"])
        volatility=float(request.form["volatility"])
        interest_rate=float(request.form["interest_rate"])

        temp_model = BlackSholes.BlackScholes(
            time_to_maturity=time_to_maturity,
            strike=strike,
            stock_price=stock_price,
            volatility=volatility,
            interest_rate=interest_rate
        )
        temp_model.calculate()


        return render_template("index.html",asset_price=stock_price ,time_to_maturity=time_to_maturity ,strike_price=strike,volatility=volatility ,interest_rate=interest_rate, call=temp_model.call, put=temp_model.put)
    else:
        return render_template("index.html",asset_price=100 ,time_to_maturity=1 ,strike_price=100,volatility=0.2 ,interest_rate=0.02, call=8.92, put=6.94)

if __name__ == '__main__':
    app.run(debug = True)