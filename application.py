import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)
app = application

## 1st step my web application should be interact with ridge.pkl and standard.pkl
## import ridge regressor and scaler pickel 
ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))




@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        try:

            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))


            
            if Region == 0:
                region_name = "Algerian Forest 🌲"
            else:
                region_name = "Sidi Bel Abbes (Seourane) 🌳"

            new_data_scaled = standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
            result = ridge_model.predict(new_data_scaled)


            fwi = result[0]

            if fwi < 5:
                risk = "Low"
            elif fwi < 15:
                risk = "Moderate"
            elif fwi < 30:
                risk = "High"
            else:
                risk = "Very High"
            
            # 🔥 NEW: Explanation logic
            explanation = []

            if Temperature > 35:
                explanation.append("🔥 High Temperature")

            if RH < 30:
                explanation.append("💧 Low Humidity")

            if Ws > 20:
                explanation.append("🌬️ Strong Wind")

            if Rain == 0:
                explanation.append("☀️ No Rain")
                
            if FFMC > 85:
                explanation.append("🔥 High Fuel Moisture Code (FFMC)")

            if DMC > 50:
                explanation.append("🔥 High Duff Moisture Code (DMC)")

            if ISI > 10:
                explanation.append("🔥 High Initial Spread Index (ISI)")

            return render_template('home.html',results=fwi, risk = risk,region_name=region_name, explanation=explanation)
        

        except Exception as e:
            return f"Error: {e}"

    
    return render_template('home.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
