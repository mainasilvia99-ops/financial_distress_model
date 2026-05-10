
# financial_distress_model
This script clearly demonstrates that while Fulmer (the right-most bars) stays above zero, Altman and Springate are deep in the "danger zone" below their respective lines for EAPC PLC.

<img width="818" height="451" alt="eapc_analysis" src="https://github.com/user-attachments/assets/e0b539d4-fd34-4a61-94b5-6d80485c29c0" />

# Corporate Failure Prediction: A Case Study of East African Portland Cement (EAPC) PLC

## 📌 Project Overview
This repository presents a quantitative financial distress analysis of **East African Portland Cement (EAPC) PLC Group** using audited data from FY2023 and FY2024. The study applies three classic bankruptcy prediction models to evaluate if the company’s recent "paper profit" translates to actual financial health.

## 📊 Methodology
The project implements a Python-based multi-model approach:
1. **Altman Z-Score:** Measures probability of bankruptcy using market-based solvency.
2. **Springate S-Score:** A strict test of operational efficiency and EBIT performance.
3. **Fulmer H-Score:** A 9-ratio model that weighs asset size and retained earnings.

## 🔍 Key Insights
*   **The Revaluation Paradox:** While EAPC reported a net profit of **KES 1.07B in 2024**, this was driven by a **KES 3.03B land revaluation gain**. Operationally, the core business remains in deficit.
*   **Market vs. Book Value:** A significant gap exists between the **Book Value of Equity (KES 20B)** and the **Market Value (KES 675M)**, signaling high investor risk premiums as per **MM Proposition II**.
*   **Liquidity Trap:** With a **Current Ratio of 0.52**, the Group faces a KES 6 Billion liquidity gap, confirmed by the Auditor-General's "Material Uncertainty" warning.

## Tech Stack & Methodology
*   **Language:** Python 3.x
*   **Libraries:** pandas (data structuring), matplotlib (visualization)
*   **Data Source:** Fully audited consolidated financial statements from EAPC Annual Reports and Dyer & Blair.

## How to Run the Analysis
*  1. Clone the repository:
git clone 
*  2. Install dependencies:
pip install pandas matplotlib
*  3. Run the script
 python financial_distress_model.py

## Author
Maina Silvia
## LinkedIn: https://www.linkedin.com/in/wahu-maina-a45779246/
Portfolio: soon

## Disclaimer: This analysis is for educational purposes based on publicly available audited data.
