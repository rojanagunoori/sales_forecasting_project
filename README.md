# 📊 Sales Forecasting System (End-to-End Time Series ML + FastAPI)

## 🏷️ Title, Introduction & Links

**📌 Project Name**

State-wise Sales Forecasting System using Machine Learning & FastAPI

## 📖 Short Description

An end-to-end machine learning system that predicts next 8 weeks of sales for each state using multiple time-series models (XGBoost, ARIMA, Prophet). The system automatically selects the best-performing model and serves predictions via a FastAPI REST API.

## 🔗 Important Links

📂 GitHub Repository: https://github.com/your-username/sales-forecasting

📊 API Docs (Swagger): http://127.0.0.1:8000/docs

🚀 Local API: http://127.0.0.1:8000

---

## 📌 Project Overview

This project simulates a real-world production ML forecasting system.

It is designed to:

- Analyze historical sales data state-wise
- Handle missing values and time-series structure
- Train multiple forecasting models
- Select the best model automatically
- Serve predictions through a REST API

### 🎯 Purpose

To build a production-like ML pipeline that demonstrates:

- Data preprocessing
- Feature engineering
- Model training & evaluation
- Model selection
- API deployment

---

### 💡 Why this project exists

This project demonstrates how machine learning models are deployed in real businesses for:

- Demand forecasting
- Inventory planning
- Sales prediction systems

---

## 🚀 Features

This project is a complete end-to-end time series forecasting system designed like a production-ready data science backend service. It includes data preprocessing, feature engineering, multiple model training, automatic model selection, and API deployment.

---

### 📊 Multi-Model Forecasting System

The system trains and evaluates multiple forecasting algorithms:

- **XGBoost (Machine Learning approach)** using engineered lag and rolling features
- **ARIMA (Statistical time series model)** for capturing trend and autocorrelation
- **Facebook Prophet** for seasonality and trend decomposition

Each model is independently trained for every state, ensuring state-wise forecasting accuracy.

---

### 🧠 Automatic Best Model Selection

After training all models, the system:

- Evaluates each model using RMSE (Root Mean Squared Error)
- Compares performance across models
- Automatically selects the best performing model per state
- Saves only the best model for future predictions

This ensures optimized accuracy without manual intervention.

---

📅 Time-Series Feature Engineering

To improve predictive performance, multiple time-based features are created:

- **Lag features:** lag_1, lag_7, lag_30 (past values of sales)
- Rolling statistics:
  - Rolling mean (7-day window)
  - Rolling standard deviation (7-day window)
- Temporal features:
  - Day of week
  - Month

These features help models capture:

- Short-term trends
- Weekly seasonality
- Monthly patterns

---

### 🔄 Missing Data Handling

The pipeline is designed to handle real-world messy datasets:

- Missing dates are filled using daily frequency resampling
- Missing sales values are handled using forward fill (ffill)
- Ensures continuity in time-series structure

This prevents model breakdown due to irregular data.

---

### ⚡ FastAPI REST API

A production-style API is built using FastAPI:

- Endpoint: GET /forecast/{state}
- Returns 8-week sales forecast per state
- Loads the best saved model dynamically
- Supports multiple states independently

**Example response:**

```bash
{
  "state": "California",
  "model_used": "xgb",
  "forecast_8_weeks": [1200, 1300, 1250, ...]
}

```

---

### 📦 Model Persistence (Per State)

Each state has its own trained model stored as:

```bash
models/{state}_model.pkl
```

This allows:

- Independent state-level forecasting
- Faster API inference
- Easy model management

---

### 📈 8-Week Forecasting System

The system generates:

- Future 56-day (8 weeks) predictions
- Recursive forecasting for XGBoost
- Built-in forecasting for ARIMA and Prophet

This meets the assignment requirement of multi-week forecasting.

---

### 🧹 Clean Modular Pipeline

The project is structured into clean modules:

- preprocessing (data cleaning)
- feature engineering
- model training
- forecasting logic
- API service

This makes the system:

- Scalable
- Maintainable
- Production-like

---

## 📁 Folder / Project Structure

```bash
sales_forecasting_project/
│
├── api/
│ └── app.py # FastAPI backend service
│
├── data/
│ └── sales.xlsx # Dataset
│
├── models/ # Saved trained models per state
│
├── src/
│ ├── preprocessing.py # Data cleaning & formatting
│ ├── feature_engineering.py# Feature creation (lags, rolling stats)
│ ├── train.py # Model training & selection
│ ├── forecast.py # Forecast generation logic
│
├── main.py # Training pipeline entry point
├── README.md # Documentation

```

---

## ⚙️ Tech Stack / Environment

### 🧠 Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Statsmodels (ARIMA)
- Prophet (Facebook Prophet)

### 🌐 Backend

- FastAPI
- Uvicorn

### 📊 Data Handling

- Pandas
- OpenPyXL (Excel reading)

### 🧰 Tools

- Pickle (model saving)
- Virtual Environment (venv)

---

## 🛠 Installation / Setup

1. Clone Repository

```bash
   git clone https://github.com/your-username/sales-forecasting.git
   cd sales-forecasting_project
```

2. Create Virtual Environment

```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
```

3. Install Dependencies

```
   pip install -r requirements.txt
```

4. Train Models

```bash
   python main.py
```

This will:

- Train models for each state
- Save best model into /models

5. Run API Server

```bash
uvicorn api.app:app --reload
```

6. Open API Docs

```bash
http://127.0.0.1:8000/docs
```

---

## 🔐 Environment Variables

Currently, this project does not require external .env variables.

But in production, you can add:

```bash
DATA_PATH=data/sales.xlsx
MODEL_PATH=models/
API_HOST=127.0.0.1
API_PORT=8000
```

## 📡 API Usage

### 🏠 Home Endpoint

```bash
GET /
```

#### Response

```bash
{
"message": "Forecast API running successfully 🚀"
}
```

---

### 📈 Forecast Endpoint

```bash
GET /forecast/{state}
```

#### Example:

```bash
/forecast/California
```

#### Response:

```bash
{
"state": "California",
"model_used": "xgb",
"forecast_8_weeks": [12345, 12500, 12800, ...]
}
```

---

## 🧠 Key Components

1. Preprocessing
   - Missing date handling
   - Sorting by state and date
   - Filling missing values
2. Feature Engineering
   - Lag features: lag_1, lag_7, lag_30
   - Rolling mean and std
   - Time features: day, month
3. Model Training
   - XGBoost for ML-based forecasting
   - ARIMA for statistical forecasting
   - Prophet for trend-based forecasting
4. Model Selection
   - Based on RMSE
   - Best model saved per state
5. API Layer
   - Loads model dynamically
   - Returns 8-week forecast

## 🔒 Security

- Local API (no authentication required)
- Safe pickle loading (internal models only)
- Input validation via FastAPI

---

## ⚠️ Challenges Faced (Explained Clearly)

---

### 1. Handling missing time-series data

#### Problem:

Real sales data does not always have continuous dates (some days missing).

**What went wrong:**

- Model expects daily continuous data
- Missing dates caused gaps in trends

**Solution:**

- Used asfreq('D') to force daily frequency
- Filled missing values using forward fill (`ffill()`)

---

### 2. Fixing NaN errors in evaluation

Problem:
During RMSE calculation, some values were NaN.

**Why it happened:**

- ARIMA predictions and real values were not aligned
- Rolling features created empty rows

**Solution:**

- Removed NaN values before evaluation
- Aligned predictions and actual values properly
- Used:

```bash
df_compare = df.dropna()
```

---

### 3. Aligning ARIMA predictions with dataset

**Problem:**
ARIMA output length did not match dataset index.

**Why:**

- ARIMA returns forecast without proper indexing

**Solution:**

- Manually aligned predictions with dataset index
- Used proper slicing before RMSE calculation

---

### 4. Recursive forecasting for XGBoost

**Problem:**
XGBoost needs future features, but future values are unknown.

**Challenge:**

- Lag features depend on previous predictions

**Solution:**

- Used recursive forecasting loop:
  - Predict 1 step
  - Update lag features
  - Repeat for next step

This simulates real-world forecasting.

---

### 5. FastAPI JSON serialization issues

**Problem:**
API crashed with error like:

```bash
numpy.float32 is not JSON serializable
```

**Why:**

- Model output was NumPy type, not Python type

**Solution:**

- Converted all outputs to Python floats:

```bash
float(pred)
```

- Ensured response is JSON safe

---

### 6. Feature leakage prevention

**Problem:**
Model could accidentally “see future data” during training.

**Why this is bad:**

- Gives fake high accuracy
- Not real-world correct

**Solution:**

- Used time-based split (not random split)
- Created lag features only from past data
- Ensured no future information leaks into training

---

## 🚀 Future Improvements (Explained Clearly)

1. Add LSTM deep learning model
   - Current system uses ML + statistical models
   - LSTM can capture long-term patterns better
   - Useful for complex seasonality

   ***

2. Implement SARIMA instead of ARIMA
   - ARIMA does not handle seasonality strongly
   - SARIMA adds seasonal component
   - Improves real forecasting accuracy

   ***

3. Add holiday feature engineering
   - Sales change during holidays (Diwali, Christmas, etc.)
   - Adding holiday flags improves model accuracy

**Example:**

```bash
is_holiday = 1 if date is holiday else 0
```

---

### 4. Deploy on AWS / Render

- Current project runs locally
- Production deployment means:
  - Public API URL
  - Real usage access
- Can deploy using:
  - AWS EC2
  - Render
  - Railway

---

### 5. Store predictions in database

- Currently predictions are temporary
- Storing in DB helps:
  - Analytics
  - History tracking
  - Dashboard creation

**Example DB:**

- PostgreSQL
- MongoDB

---

6. Add authentication to API
   Right now API is open (no security)

- In real systems we add:
  - API keys
  - JWT tokens

This prevents unauthorized access.

---

## 🤝 Contributing

If anyone wants to contribute:

- Fork repository
- Create new branch
- Commit changes
- Submit Pull Request

---

## 🙏 Acknowledgments

- Scikit-learn documentation
- Facebook Prophet library
- XGBoost team
- FastAPI framework
- Statsmodels library

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♀️ Author / Contact

**Nagunoori Roja**

- 📧 Email: [nagunooriroja@gmail.com](mailto:nagunooriroja@gmail.com)
- 🌐 GitHub: [https://github.com/rojanagunoori](https://github.com/rojanagunoori)
- 🌐 LinkedIn: [https://www.linkedin.com/in/nagunoori-roja-51b936267/](https://www.linkedin.com/in/nagunoori-roja-51b936267/)
- 🌐 Personal Portfolio: [portfolio-roja.netlify.app](https://portfolio-roja.netlify.app/)
- 🌐 LeetCode: [https://leetcode.com/u/dSdsi6XkI8/](https://leetcode.com/u/dSdsi6XkI8/)
- 🌐 Kaggle: [https://www.kaggle.com/nagunooriroja](https://www.kaggle.com/nagunooriroja)

---

## 🎯 Final Note

Your project is now:

- ✔ Complete
- ✔ Functional
- ✔ API working
- ✔ Industry-style structure
- ✔ Ready for submission + video + viva

---
