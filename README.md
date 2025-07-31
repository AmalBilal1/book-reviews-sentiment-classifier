# 📚 Book Review Sentiment Classifier

This project implements a **neural network** to classify book reviews as **positive** or **negative** using natural language processing techniques. Leverages a TF-IDF vectorizer to transform review text into numerical features. The model is trained, validated, and tested to evaluate its performance and improve generalization.

---

## 🚀 Project Overview

The goal of this project is to apply the **machine learning lifecycle** to a real-world sentiment analysis task. Using a dataset of book reviews, the model predicts whether a review expresses a positive or negative sentiment.

**Key Objectives:**
- Load and preprocess the book reviews dataset  
- Perform exploratory data analysis  
- Define the ML problem: **binary classification**  
- Transform text data using **TF-IDF vectorization**  
- Build and train a **feedforward neural network**  
- Evaluate performance on training, validation, and test sets  
- Experiment with techniques to improve accuracy and generalization  

---

## 📂 Project Structure
├── data/

│ └── bookReviewsData.csv # Book review dataset

├── DefineAndSolveMLProblem.ipynb # Jupyter Notebook with full implementation

├── README.md # Project documentation

└── requirements.txt # Python dependencies

---

## 🛠️ Technologies Used

- **Python**  
- **Pandas** and **NumPy** (data manipulation)  
- **Matplotlib** and **Seaborn** (data visualization)  
- **Scikit-learn** (TF-IDF vectorization and preprocessing)  
- **TensorFlow** and **Keras** (neural network implementation)  

---

## ⚙️ Installation

Clone the repository and install the dependencies:

git clone https://github.com/abilal24/book-review-sentiment-classifier.git

cd book-review-sentiment-classifier

pip install -r requirements.txt

---

## ▶️ Usage:

Run the Jupyter notebook to train and evaluate the model: jupyter notebook DefineAndSolveMLProblem.ipynb

The notebook includes step-by-step code for:

Data loading & preprocessing

TF-IDF vectorization

Model construction & training

Performance evaluation

---

## 📊 Results

Achieved effective classification (81% accuracy) of book reviews into positive or negative categories.

Model performance was evaluated on training, validation, and test sets, with experiments conducted to improve generalization.

---

## 🔮 Future Improvements

Experiment with word embeddings.

Implement regularization to prevent overfitting.

Improve the confusion matrix and analytics report.

---

## 👩‍💻 Author

Developed by Amal Bilal for the final project in Break Through Tech's Machine Learning Foundations Course.

GitHub: amalbilal1

LinkedIn: www.linkedin.com/in/amal-bilal
