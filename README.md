
# 🔥 Forest Fire Prediction Web App using Machine Learning




## 🎥 Demo

🚀 Try the live app now!

🌐 Live Demo:  
https://forest-fire-app.onrender.com/

👉 This web application predicts Forest Fire Risk using Machine Learning and provides explainable insights based on environmental conditions.


## 🚀 Features

### 🔥 Fire Risk Prediction

- Predict Fire Weather Index (FWI) based on environmental conditions
- Classify fire risk levels (Low, Moderate, High, Very High)
- Uses trained Machine Learning model (Ridge Regression)

---

### 🧾 Input Options

- Manual input of environmental parameters:
  - Temperature
  - Humidity (RH)
  - Wind Speed (Ws)
  - Rain
  - FFMC, DMC, ISI
  - Region selection

---

### 📊 Result Interpretation

- Displays predicted FWI value
- Shows risk level with color indicators (Low to Very High)
- Provides explanation for risk (e.g., High Temperature, Low Humidity, Strong Wind)

---

### 🌍 Region-Based Prediction

- Supports two regions:
  - 🌲 Algerian Forest (Bejaia)
  - 🌳 Sidi Bel Abbes

---

### 🌐 Web Application

- Built using Flask
- Interactive UI for user input
- Deployed on Render for live access
  
## 📊 Dataset

The Algerian Forest Fires dataset was used. 🔗 [Dataset](https://www.kaggle.com/datasets/harshvir04/algerian-forest-fires-dataset)

The dataset contains environmental and meteorological data from two regions:

- 🌲 Bejaia (Algerian Forest Region)
- 🌳 Sidi Bel Abbes Region

Key features in the dataset include:

- Temperature (°C)
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- FFMC (Fine Fuel Moisture Code)
- DMC (Duff Moisture Code)
- ISI (Initial Spread Index)
- Classes (Fire / No Fire)
- Region (Encoded)

This dataset is used to predict the Fire Weather Index (FWI) and determine fire risk levels.

## 💻 Tech Stack


| Category            | Tools                          |
|--------------------|--------------------------------|
| Programming        | Python                         |
| Data Handling      | Pandas, NumPy                  |
| Machine Learning   | scikit-learn (Ridge Regression)|
| Visualization      | Matplotlib                     |
| Web Framework      | Flask                          |
| Deployment         | Render                         |
| Model Persistence  | Pickle                         |
| Notebook Analysis  | Jupyter Notebook               |


## 📸 Screenshots

### 🔹 Home Page
<img width="527" height="515" alt="Screenshot 2026-03-21 002633" src="https://github.com/user-attachments/assets/ee98f0c0-03ff-4769-8878-6b31460b80df" />

### 🔹 Prediction Result
<img width="556" height="522" alt="Screenshot 2026-03-21 002559" src="https://github.com/user-attachments/assets/f46bc6b0-0361-4b88-af66-0911fc7114cb" />


## ⚙️ Installation

If you want to run this project on your local machine:

```bash
git clone https://github.com/anmol7240/Forest-Fire_FWI-prediction.git
cd Forest-Fire_FWI-prediction
pip install -r requirements.txt
python application.py 
```

## 🚀 Deployment

This project is deployed using **Render**.

### Steps to Deploy:

1. Push your code to GitHub  
2. Go to Render (https://render.com/)  
3. Create a new Web Service  
4. Connect your GitHub repository  
5. Add the following settings:

- **Build Command:**  
  pip install -r requirements.txt  

- **Start Command:**  
  gunicorn application:application  

6. Click on Deploy 🚀  

Your app will be live in a few minutes!


## 🙏 Acknowledgements

- Inspired by real-world environmental datasets for forest fire prediction.
- Special thanks to [Krish Naik Sir](https://github.com/krishnaik06) for his valuable tutorials and guidance in Machine Learning and Flask development.
- Thanks to the open-source community for powerful libraries like Flask, NumPy, Pandas, and Scikit-learn.
- Gratitude to online resources and documentation that supported the development and deployment of this project.
