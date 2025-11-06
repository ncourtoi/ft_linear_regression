
# ft_linear_regression
An Introduction to Machine Learning
## 📘 Summary
This project is our first step into the world of Machine Learning.
We will implement a simple linear regression algorithm that predicts the price of a car based on its mileage using gradient descent.
## 🚀 Objective
The goal is to understand the basic principles behind machine learning by implementing everything from scratch.
Our program will:

- Train a linear model on a dataset (data.csv) containing car mileages and prices.
- Predict a car price for a given mileage using the trained parameters.
## ⚙️ Project Structure
We will create two main programs:

### 1️⃣ Training Program (train.py)

This script will:

Read the dataset.

- Perform linear regression using gradient descent.

- Save the resulting parameters (theta0 and theta1) in a file (e.g., thetas.csv).

**Mathematical model**:

    estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
**Gradient Descent Update Formulas**:

    θ0​:=θ0​−α×m1​i=0∑m−1​(estimatePrice(xi​)−yi​)
    θ1​:=θ1​−α×m1​i=0∑m−1​(estimatePrice(xi​)−yi​)×xi​
Where:


- α is the learning rate


- m is the number of samples

### 2️⃣ Prediction Program (predict.py)

This script will:

- Load the trained parameters from
    thetas.csv

- Ask the user for a mileage value.

- Output the estimated price based on the learned model.

### 📊 Bonus Features

Once we did the mandatory part perfectly can add:

- 📈 Plotting data points and the regression line using Matplotlib.

- 📉 Visualization of the learning curve (cost function evolution).

### 🧠 Notes

- We can use any programming language, but Python is recommended.

- Avoid libraries that perform the entire regression for you (e.g., numpy.polyfit).

- Data visualization is encouraged to debug and understand our model better.

## 🧪 Example Usage
**Training the model:**
```bash
python training.py
```
**Training the model and display the visualization:**
```bash
python training.py -b
```
**Predicting a price:**
```bash
python prediction.py
Enter a mileage: 100000
Estimated price: 8500 €
```

## ✅ Evaluation Criteria

During peer-evaluation, your project will be checked for:

- ❌ No use of pre-built regression libraries.

- 🧩 Correct implementation of the linear hypothesis.

- ⚖️ Correct gradient descent update rule.

- 💾 Proper saving/loading of model parameters.

- 🧮 Bonus: Data visualization or precision computation.

## 💡 Author

### 👨‍💻 ncourtoi
