
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

## Financial Variable	FY 2022-2023 (KES '000)	FY 2023-2024 (KES '000)
*  **Total Assets** 	32,780,931	35,186,150
*  **Total Liabilities**	13,566,668	14,785,418
*  **Total Equity**	19,214,263	20,400,732
*  **Revenue (Sales)**	2,953,573	3,279,053
*  **Working Capital (CA - CL)** 	(11,824,491)	(6,090,885)
*  **Retained Earnings**	17,760,370	18,827,445
*  **EBIT (Operating Profit/Loss)**	(1,926,027)	(1,961,489)
* **Current Assets**	1,731,893	6,743,038
*  **Current Liabilities**	13,556,384	12,833,923
*  **Net Income (PAT)**	(1,356,467)	1,067,075



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
