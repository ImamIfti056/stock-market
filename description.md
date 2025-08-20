## Title (Tentative)
Realistic Stock Price Prediction with Walk-Forward Validation: A Machine Learning and Deep Learning Study

## Purpose
- Predicting exact future price (main purpose for now)
- Price direction (Up/Down)
- Buy/Sell signals

## Feature Engineering
- Add technical indicators (momentum, trend, volume).
- Include sentiment scores from finance news(Not neseccary for now. Will be done in future)

## Model
- Try Hybrid models → Example: CNN+LSTM

## Evaluation & Robustness
- Use Walk-forward validation (rolling windows) → simulates real-time better than train-test split.
- if not real time prediction I can use simple evaluation methods(e.g. RMSE, MSE etc.)

## Practical Contribution
- Simulate a backtest strategy (buy when model says up, sell when down).

- Show how your ML/DL-based model could actually help in trading decisions.

## Training on the Entire Dataset and Predicting Next Day
### 🔹 Idea

Use all available historical data (2015–2024 for example).

Train a model.

Predict the next unseen day (say 2025-01-02).

Keep repeating as new data arrives.

This is close to how real-time forecasting works.

### 📌 Pros

- Uses all data
- No data is "wasted" in a test split.
- The model learns from the maximum history.
- Closer to Real World
- In production, you will retrain models regularly with the most recent data.
- Financial firms do exactly this.
- Incremental Updating Possible
- You can update/retrain the model as new daily data arrives.

### 📌 Cons

- No True Evaluation ⚠️
- If you don’t hold out a test set, you cannot measure how well your model generalizes.
- You might think it’s good, but it could just be overfitting.
- Overfitting Risk
- The model could memorize patterns from the training period that don’t repeat in the future.
- Without a test set, you won’t detect this.
- False Sense of Accuracy
- The model might “look” great historically but collapse in live trading.
- This is why researchers use walk-forward validation (rolling training windows).
- Concept Drift Ignored
- Markets change. A model trained on old data (2015–2018 patterns) might not work in 2025.
- Without validation, you won’t notice performance drop.

### 📌 Best Practice

Instead of just training once on the full dataset:

- Use Walk-Forward Validation

- Train on first N years → predict next 1 month.

- Slide window forward → repeat.

This mimics “real-time” while still allowing evaluation.

Example:
- Train 2015–2020 → predict Jan 2021.
- Train 2015–2021 → predict Jan 2022.
- Train 2015–2022 → predict Jan 2023.

This way, you see how your model would have worked historically in a realistic setup.

### Final Deployment

Once you’re happy with your model (based on validation), you can train it on all available data and then start doing true live predictions for the next days.