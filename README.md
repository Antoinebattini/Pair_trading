# Pair Trading Project

Welcome to our Pair Trading project repository! We are two students from University Paris Dauphine (Master 280) who share a passion for quantitative finance and market-neutral strategies. In this repository, we will explore various pair trading techniques and implement different types of metrics to identify and select pairs, construct portfolios, and experiment with market-neutral approaches.

## Table of Contents
1. [Overview](#overview)  
2. [Motivation](#motivation)  
3. [Approaches & Methods](#approaches--methods)  
4. [Pair Identification & Metrics](#pair-identification--metrics)  
5. [Portfolio Creation](#portfolio-creation)  
6. [Neutrality Strategies](#neutrality-strategies)  
7. [Getting Started](#getting-started)  
8. [Contributing](#contributing)  
9. [Contact](#contact)

---

## Overview

Pair trading is a market-neutral trading strategy that exploits price divergences between two correlated securities. By simultaneously going long on one security and short on another, we aim to neutralize common risk factors and profit from the relative performance between these instruments.

In this project, our goals are to:

- Implement robust techniques for identifying tradable pairs.  
- Develop and compare various metrics that help rank and select pairs.  
- Construct a portfolio from our selected pairs.  
- Experiment with different neutrality approaches to manage systematic risk.  
- Maintain a clear and reproducible research environment for future exploration.

---

## Motivation

As part of our Master 280 at University Paris Dauphine, we are eager to apply theoretical knowledge to real-world financial scenarios. Pair trading offers a rich learning environment for statistical analysis, risk management, and algorithmic trading. By sharing this project, we hope to create a reference and a learning platform for anyone interested in quantitative finance and market-neutral strategies.

---

## Approaches & Methods

To achieve our objectives, we will:

1. **Data Collection & Preprocessing**  
   - Gather historical price data from multiple sources.  
   - Adjust for corporate actions (splits, dividends, etc.) to ensure clean data.  
   - Handle missing data and standardize time series for analysis.

2. **Pair Identification & Metrics**  
   - Perform correlation and cointegration tests (Engle-Granger, Johansen).  
   - Develop custom metrics to measure pair stability and mean reversion potential.  
   - Implement ranking criteria to select the best pairs based on these metrics.

3. **Portfolio Creation & Management**  
   - Combine selected pairs into a single portfolio to diversify risk.  
   - Define position sizing rules and risk controls (stop-loss, take-profit).  
   - Deploy backtesting techniques to validate the performance of the overall portfolio.

4. **Neutrality Strategies**  
   - Explore beta-neutral, dollar-neutral, and sector-neutral tactics.  
   - Evaluate the trade-offs between different market exposures.  
   - Determine the most effective ways to preserve alpha generation.

5. **Backtesting & Validation**  
   - Simulate strategies under realistic market conditions (including slippage, fees).  
   - Perform out-of-sample tests to verify strategy robustness.  
   - Use performance metrics (Sharpe, Sortino, max drawdown) to refine our approach.

---

## Pair Identification & Metrics

Identifying which pairs to trade is a crucial step in pair trading. We will focus on:

1. **Correlation Analysis**  
   When identifying promising pairs to trade, one effective approach is to measure how “close” two assets are in terms of their historical price or return series. Below, we outline two specific distance-based methods that we apply in our workflow:
   1. ***Euclidian distance***
      The Euclidean distance method treats each asset’s price (or return) history as a point in a multi-dimensional space.
      Normalization: Before calculating distances, we typically normalize or standardize each time series to ensure differences in scale (e.g., different price ranges) do not bias the results.This straightforward metric captures absolute differences between two time series, making it a useful baseline for pair identification.
   2. ***Correlation-Based distance***
      While Euclidean distance focuses on absolute dissimilarities, correlation-based distances emphasize the direction and pattern of movement. Two popular forms include angular distance and declination distance, which transform correlations into a distance metric:Angular Distance and its declinaison.
      To enhance reliability, we apply Random Matrix Theory (RMT) denoising as discussed in the works of Marcos López de Prado. RMT helps filter out spurious correlations by removing random noise from the correlation matrix, leaving a more robust structure for measuring true asset relationships. After denoising, the correlation-based distance calculation is more stable and less prone to overfitting or short-lived market anomalies.
2. **Cointegration Tests**  
   - Apply Engle-Granger and Johansen tests to confirm the presence of a stable long-term relationship.  
   - Select pairs that exhibit mean reversion potential, a key aspect of pair trading.

3. **Custom Stability & Mean Reversion Metrics**  
   - Develop additional metrics (e.g., half-life of mean reversion, residual variance) for deeper insights.  
   - Use these metrics to rank pairs based on profitability and stability.

By combining these metrics, we aim to create a robust shortlist of potential pairs with high mean-reversion characteristics and manageable risk exposure.

---

## Portfolio Creation

Once we have identified and ranked the most promising pairs, we will construct a portfolio composed of multiple pair trades. The steps include:

1. **Pair Selection & Allocation**  
   - Pick the top-ranked pairs based on the defined metrics.  
   - Allocate capital to each pair according to a chosen weighting scheme (e.g., equal weighting, risk-adjusted weighting).

2. **Position Sizing**  
   - Determine position sizes that align with your overall risk tolerance.  
   - Employ standard risk management practices such as stop-loss orders to limit downside.

3. **Diversification & Risk Control**  
   - Ensure the selected pairs are not overly concentrated in the same sector or risk factors.  
   - Monitor correlations across pairs to maintain diversification benefits.

4. **Periodic Rebalancing**  
   - Adjust the portfolio at regular intervals or when significant deviations from targets occur.  
   - Reapply metrics and remove underperforming pairs, replacing them with new opportunities.

Through this systematic approach, we aim to build a balanced portfolio that benefits from multiple mean-reverting relationships, while minimizing idiosyncratic and systematic risks.

---

## Neutrality Strategies

Maintaining market neutrality helps isolate the alpha source (mean reversion) while hedging broader market risks. We will test:

1. **Beta Neutrality**  
   - Match the beta of long and short positions to cancel out market exposure.  
   - Minimize exposure to overall market movements.

2. **Dollar Neutrality**  
   - Allocate an equal dollar amount to long and short positions.  
   - Simple to implement and reduces net exposure to the market.

3. **Sector Neutrality**  
   - Pair stocks within similar industries to mitigate sector-related shocks.  
   - Enhance the likelihood of pure mean-reversion gains, independent of industry trends.

By comparing these approaches, we hope to identify the optimal strategy to hedge systematic risk while maximizing alpha generation.

---

## Getting Started

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/pair-trading-project.git
   ```
2. **Install Dependencies**  
   In this repository, you’ll find a `requirements.txt` file listing all necessary Python libraries (e.g., `pandas`, `numpy`, `statsmodels`, `matplotlib`, etc.):  
   ```bash
   pip install -r requirements.txt
   ```
3. **Explore the Notebooks**  
   Jupyter notebooks in the `notebooks/` directory contain step-by-step explanations and code for collecting data, identifying pairs, and building the trading strategy.

---

## Contributing

We welcome contributions! If you want to add new features, fix bugs, or suggest improvements:

1. Fork the repository.  
2. Create a new branch for your feature or bugfix.  
3. Submit a Pull Request with a clear description of your changes.

---

## Contact

For questions, suggestions, or collaboration opportunities, feel free to reach out:

- **Email**: [jules.arzel@dauphine.eu]  
- **LinkedIn**: [linkedin.com/in/jules-arzel]
- **Email**: [Antoine.battini@dauphine.eu]  
- **LinkedIn**: [linkedin.com/in/antoine-battini-b99437184]

We appreciate your interest and hope this repository is a valuable resource for anyone exploring pair trading strategies. Let’s keep learning together!

---

**Happy Pair Trading!**  
*Two students from University Paris Dauphine (Master 280)*
