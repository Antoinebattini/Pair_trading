# Pair_trading
# Pair Trading Project

Welcome to our Pair Trading project repository! We are two students from University Paris Dauphine (Master 280) who share a passion for quantitative finance and market-neutral strategies. In this repository, we will explore various pair trading techniques, implement different types of performance metrics, and delve into multiple neutrality approaches.

## Table of Contents
1. [Overview](#overview)  
2. [Motivation](#motivation)  
3. [Approaches & Methods](#approaches--methods)  
4. [Metrics](#metrics)  
5. [Neutrality Strategies](#neutrality-strategies)  
6. [Getting Started](#getting-started)  
7. [Contributing](#contributing)  
8. [Contact](#contact)

---

## Overview

Pair trading is a market-neutral trading strategy that aims to exploit price divergences between two correlated securities. By simultaneously going long on one security and short on another, we seek to neutralize common risk factors and profit from the relative performance between the two instruments.

In this project, our goals are to:
- Implement robust techniques for identifying tradable pairs.
- Compare various metrics to evaluate pair stability and profitability.
- Experiment with different neutrality strategies to mitigate systematic risks.
- Provide a clear and reproducible research environment for further exploration.

---

## Motivation

As part of our Master 280 at University Paris Dauphine, we are enthusiastic about applying theoretical knowledge to real-world financial markets. Pair trading, a classic quantitative strategy, provides an excellent framework to learn about statistical analysis, risk management, and algorithmic trading. We hope this project can serve both as a learning platform and a reference for future quantitative finance endeavors.

---

## Approaches & Methods

To achieve our objectives, we plan to:

1. **Data Collection & Preprocessing**:  
   - Import historical price data from various sources.  
   - Clean and adjust data for corporate actions (splits, dividends, etc.).  
   - Handle missing values and standardize time series for analysis.

2. **Pair Identification & Selection**:  
   - Explore correlation-based methods (Pearson, Spearman).  
   - Use cointegration tests (Engle-Granger, Johansen) to find mean-reverting pairs.  
   - Employ machine learning techniques for discovering new pair relationships.

3. **Trade Execution & Simulation**:  
   - Set up backtesting environment with realistic constraints (commissions, slippage).  
   - Implement position sizing rules and risk controls (stop-loss, take-profit).  
   - Evaluate out-of-sample performance.

---

## Metrics

We will evaluate our pair trading strategies using a variety of performance metrics, including:

- **Profit & Loss (P&L) Curves**: Tracks overall strategy returns.  
- **Sharpe Ratio**: Measures excess return relative to volatility.  
- **Sortino Ratio**: Focuses on downside risk.  
- **Maximum Drawdown**: Gauges the largest peak-to-trough loss.  
- **Beta and Correlation**: Assesses the strategy’s systematic exposure.

These metrics will guide us in refining our strategy and selecting optimal pairs.

---

## Neutrality Strategies

Maintaining a market-neutral stance is crucial for a pair trading approach. We will consider:

1. **Beta Neutrality**: Matches the beta of long and short positions to reduce market exposure.  
2. **Dollar Neutrality**: Allocates an equal amount of capital to long and short positions.  
3. **Sector Neutrality**: Ensures that pairs are chosen within or across similar sectors to limit exposure to industry-specific factors.  

By experimenting with these neutrality approaches, we aim to identify the most effective way to hedge systematic risks while preserving alpha generation.

---

## Getting Started

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/pair-trading-project.git
   ```
2. **Install Dependencies**  
   We will provide a `requirements.txt` file with all the necessary Python libraries (e.g., `pandas`, `numpy`, `statsmodels`, `matplotlib`, etc.).  
   ```bash
   pip install -r requirements.txt
   ```
3. **Explore the Notebooks**  
   You can find Jupyter notebooks inside the `notebooks/` directory, which contain detailed explanations and step-by-step instructions for replicating our pair trading experiments.

---

## Contributing

We welcome contributions! If you want to add new features, fix bugs, or suggest improvements:
1. Fork the repository.  
2. Create a new branch for your feature/bugfix.  
3. Submit a Pull Request explaining your changes.

---

## Contact

For any questions, suggestions, or collaboration ideas, feel free to reach us through:

- **Email**: `[Your Email Address Here]`
- **LinkedIn**: `[Optional LinkedIn Profiles]`

We appreciate your interest and hope this repository serves as a helpful resource for anyone exploring pair trading strategies. Let’s keep learning together!

---

**Happy Pair Trading!**  
*Two students from University Paris Dauphine (Master 280)*
