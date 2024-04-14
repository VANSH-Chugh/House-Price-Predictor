from flask import Flask, render_template, request
import pandas as pd

app= Flask(__name__)

@app.route("/")
def home():
    price=""
    if (request.args.get("income")) and (request.args.get("age")) and (request.args.get("rooms")) and (request.args.get("population")):
        income= eval(str(request.args.get("income")))
        age= eval(str(request.args.get("age")))
        rooms= eval(str(request.args.get("rooms")))
        population= eval(str(request.args.get("population")))
        model= pd.read_pickle("HousePricePredictor.pkl")
        df= pd.DataFrame([[income, age, rooms, population]], columns= ['Avg. Area Income','Avg. Area House Age','Avg. Area Number of Rooms','Area Population'])
        pred= model.predict(df)
        price= f"$ {round(pred[0],1)}"

    return render_template("index.html", result= price)

app.run(debug= True, port= 8000)