# 🎓 Student Performance Prediction — End-to-End Machine Learning Project

> A complete **end-to-end Machine Learning project** that predicts student academic performance based on study habits and lifestyle factors. Built with a **modular, production-ready architecture** and served through a **Flask web application**.

---

## 📌 Project Overview

This project predicts a student's **Performance Index** (target variable) using features like hours studied, previous scores, extracurricular activities, sleep hours, and sample papers practiced.

The entire ML lifecycle is covered:
- **Data Ingestion** → Reading and splitting raw data into train/test sets
- **Data Transformation** → Feature encoding, scaling, and preprocessing pipelines
- **Model Training** → Training and evaluating 8 different regression models
- **Prediction Pipeline** → Loading the best model and making real-time predictions
- **Web Application** → A Flask-based UI where users can input data and get predictions

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Language** | Python 3.x |
| **Web Framework** | Flask |
| **ML Libraries** | Scikit-learn, XGBoost, CatBoost |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn (in notebooks) |
| **Serialization** | Dill (for saving/loading models) |
| **Architecture** | Modular pipeline-based design |

---

## 📊 ML Models Used

The project trains and compares **8 regression algorithms** and automatically selects the best one based on R² score:

| # | Model | Type |
|---|---|---|
| 1 | Linear Regression | Baseline |
| 2 | Decision Tree Regressor | Tree-based |
| 3 | Random Forest Regressor | Ensemble |
| 4 | Gradient Boosting Regressor | Boosting |
| 5 | XGBoost Regressor | Boosting |
| 6 | CatBoost Regressor | Boosting |
| 7 | AdaBoost Regressor | Boosting |
| 8 | K-Neighbors Regressor | Instance-based |

> The best model (highest R² score on test data) is automatically saved as a `.pkl` file for predictions.

---

## 📁 Folder Structure

```
ML-_PROJECT-main/
│
├── app.py                          # Flask application entry point
├── setup.py                        # Package setup configuration
├── requirements.txt                # Python dependencies
│
├── src/                            # Source code (modular pipeline)
│   ├── __init__.py
│   ├── logger.py                   # Custom logging setup
│   ├── exception.py                # Custom exception handling
│   ├── utils.py                    # Utility functions (save/load models, evaluate)
│   │
│   ├── components/                 # Core ML components
│   │   ├── data_ingestion.py       # Reads data, performs train-test split
│   │   ├── data_transformation.py  # Feature engineering & preprocessing
│   │   └── model_trainer.py        # Trains multiple models, selects the best
│   │
│   └── pipeline/                   # Pipelines
│       ├── train_pipeline.py       # Training pipeline (end-to-end training)
│       └── predict_pipeline.py     # Prediction pipeline (used by Flask app)
│
├── notebook/                       # Jupyter notebooks for EDA & experimentation
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
│       └── stud.csv                # Original dataset
│
├── datasets/                       # Generated artifacts (train/test splits, models)
│   ├── data.csv                    # Raw data copy
│   ├── train.csv                   # Training data (80%)
│   ├── test.csv                    # Testing data (20%)
│   ├── model.pkl                   # Trained best model (serialized)
│   └── preprocessor.pkl            # Fitted preprocessor (serialized)
│
└── templates/                      # HTML templates for Flask UI
    ├── index.html                  # Landing page
    └── home.html                   # Prediction form page
```

---

## 🔧 How to Set Up & Run

### Prerequisites
- Python 3.8 or above
- pip (Python package manager)

### Step 1 — Clone the Repository
```bash
git clone https://github.com/<your-username>/ML-_PROJECT.git
cd ML-_PROJECT-main
```

### Step 2 — Create a Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Train the Model (Optional — pre-trained model already included)
```bash
python src/components/data_ingestion.py
```
This will:
- Read the dataset
- Split into train/test sets
- Apply preprocessing
- Train all 8 models
- Save the best model as `datasets/model.pkl`

### Step 5 — Run the Flask Application
```bash
python app.py
```
The app will start at: **http://127.0.0.1:5000**

### Step 6 — Make a Prediction
1. Open your browser and go to `http://127.0.0.1:5000/predict_data`
2. Fill in the form:
   - **Hours Studied** — Number of hours spent studying
   - **Previous Scores** — Marks obtained in previous exams
   - **Extracurricular Activities** — Yes / No
   - **Sleep Hours** — Average hours of sleep per day
   - **Sample Question Papers Practiced** — Number of practice papers completed
3. Click **"Predict your performance index"**
4. View the predicted performance score on the page

---

## 🏗️ How the Pipeline Works

```
┌─────────────────┐
│  Raw Dataset     │  (notebook/data/stud.csv)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Data Ingestion   │  Read CSV → Train/Test Split (80/20)
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│ Data Transformation  │  Missing value imputation → Encoding → Scaling
└────────┬────────────┘
         │
         ▼
┌─────────────────┐
│ Model Training   │  Train 8 models → Evaluate R² → Pick the best
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Save Artifacts   │  model.pkl + preprocessor.pkl
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Flask Web App    │  Load model → Accept user input → Return prediction
└─────────────────┘
```

---

## 📈 Input Features

| Feature | Description | Type |
|---|---|---|
| Hours Studied | Total hours spent studying | Numeric |
| Previous Scores | Scores obtained in previous exams | Numeric |
| Extracurricular Activities | Participation in extracurricular activities | Yes / No |
| Sleep Hours | Average daily hours of sleep | Numeric |
| Sample Question Papers Practiced | Number of practice papers attempted | Numeric |

**Target Variable:** Performance Index (continuous score)

---

## 📝 What I Learned from This Project

- ✅ How to structure an ML project with **modular, reusable code**
- ✅ Building **data pipelines** (ingestion → transformation → training)
- ✅ Using **Scikit-learn Pipelines** and `ColumnTransformer` for preprocessing
- ✅ Training & comparing **multiple ML algorithms** automatically  
- ✅ Implementing **custom exception handling** and **logging** for debugging
- ✅ Saving and loading models with **serialization** (pickle/dill)
- ✅ Building a **Flask web application** to serve ML predictions
- ✅ Writing **clean, production-style Python code** with `dataclass` configs

---

## 🚀 Future Improvements

- [ ] Add **hyperparameter tuning** (GridSearchCV / RandomizedSearchCV) for better model performance
- [ ] Deploy the app on **cloud platforms** (AWS / Heroku / Render)
- [ ] Add **CI/CD pipeline** using GitHub Actions
- [ ] Build a **Docker container** for easy deployment
- [ ] Add **more visualizations** and a dashboard for model performance metrics
- [ ] Implement **input validation** on the web form

---

## 👤 Author

**Sanoj**  
📧 sanojsam123@gmail.com

---

## 📄 License

This project is open-source and available for learning purposes.

---

> ⭐ If you found this project helpful, consider giving it a star on GitHub!