# 🪙 Coin Toss Simulation: The Law of Large Numbers

This project is an interactive web application built with **Streamlit** that simulates coin toss experiments to demonstrate the **Law of Large Numbers**. It visualizes in real-time how the cumulative mean of outcomes converges to the theoretical probability of 0.5 as the number of trials increases.

## 🚀 Features
* **Real-time Visualization:** Uses `st.empty` and `line_chart` to animate the convergence of the mean during the simulation.
* **Dynamic Simulation:** Adjustable number of trials (1 to 1,000) using an interactive slider.
* **Persistent Results:** Utilizes `st.session_state` to store and display the results of multiple experiments in a historical table.
* **Statistical Rigor:** Powered by `scipy.stats.bernoulli` for accurate random variable generation.

---

## 🛠️ Tech Stack
* **Python 3.x**
* **Streamlit** (UI and Dashboarding)
* **Pandas** (Data management)
* **SciPy** (Statistical distributions)

---

## 📈 The Concept
The simulation follows the **Bernoulli Distribution** where:
* **Outcome 1 (Heads):** Probability $p = 0.5$
* **Outcome 0 (Tails):** Probability $q = 1 - p = 0.5$

As the number of trials ($n$) grows, the average of the results ($\bar{X}_n$) is guaranteed to approach the expected value ($\mu = 0.5$).

---

## 💻 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/JManuelCR/coin-toss-simulation.git](https://github.com/JManuelCR/coin-toss-simulation.git)
cd coin-toss-simulation