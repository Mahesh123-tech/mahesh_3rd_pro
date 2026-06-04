# 📊 GenZ Budget Allocation & Career Benchmark Tracker

An interactive Streamlit web application designed for Generation Z individuals to track their personal monthly finances, calculate income distribution percentages, and instantly benchmark their spending/saving behaviors against peers and global survey dataset standards.

---

## 🚀 Live Demo
*(Once deployed, you can paste your Streamlit Community Cloud link here!)*
👉 [Live Dashboard Link](https://share.streamlit.io/)

---

## ✨ Features
- **📌 High-Level Success Headers:** Displays core academic and career benchmarks (Total Students Tracked, Avg Starting Salary, Avg Job Offers, and Career Satisfaction) based on the target survey data.
- **🌍 Global Sidebar Breakdowns:** Shows the precise global dataset percentage weight distribution across all categories sorted from highest to lowest.
- **📋 Interactive User Form:** Allows users to input their name, age, income, and individual monthly dollar allocations.
- **🚦 Dynamic Budget Warning System:** Alerts users with a clean warning banner if their targeted allocations exceed 100% of their actual monthly income.
- **📊 Tri-Group Visual Charting:** Renders an interactive Plotly grouped bar chart comparing User Inputs directly against a filtered peer age baseline and the broad global database.
- **💡 Contextual Insights:** Automatically analyzes the user's highest spending areas and dynamically generates strategic advice.

---

## 📂 Repository Structure
```text
├── app.py                      # Main Streamlit web application script
├── requirements.txt            # Python package dependencies
├── genz_money_spends.csv       # Underlying survey tracking dataset
└── README.md                   # Repository documentation and guide
