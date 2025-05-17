# 🎬 Movie Recommender App

This is a simple content-based movie recommendation system built using Python, Streamlit, and Scikit-learn. It uses TF-IDF and cosine similarity to recommend movies based on plot descriptions.

---

## 🚀 Features

- Recommend similar movies based on descriptions
- Fuzzy title matching for minor typos
- Streamlit UI for live interaction
- Ready to deploy on Streamlit Cloud

---

## 🧪 Tech Stack

- Python
- Streamlit
- pandas
- scikit-learn

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deploy on Streamlit

1. Push this folder to a public GitHub repo.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud).
3. Click "New app", select your repo, and deploy!

---

## 📁 Dataset

Include a `movies.csv` file with at least these columns:
- `title`: movie name
- `overview`: description/summary of the movie

---

## 📷 Output Example

```
Input: Avatar
Output:
- John Carter
- Interstellar
- The Matrix
...
```
