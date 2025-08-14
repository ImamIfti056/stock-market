# 📊 Thesis: Stock Market Prediction

This repository contains the code and resources for my **Thesis** on stock market prediction.  
It includes data preprocessing, model training, evaluation, and visualization.

---

## 🚀 Getting Started

Follow the steps below to clone the repository and set up the development environment.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ImamIfti056/stock-market
cd stock-market
```

### 2️⃣ Create a Virtual Environment
It’s recommended to use a virtual environment to keep dependencies isolated.

```bash
python -m venv venv
```

Activate the environment:

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
All dependencies are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

## 📂 Project Structure
```
├── data/               # Datasets (ignored in .gitignore if large)
├── notebooks/          # Jupyter notebooks
├── scripts/            # Source code
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## 🛠 Development Notes
- Do **not** commit your `venv/` folder.  
- Keep large datasets out of the repo — store them in `/data` and add to `.gitignore`.
- Update `requirements.txt` when new dependencies are added:
```bash
pip freeze > requirements.txt
```

---

## 📜 License
This project is licensed under the MIT License.
