import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Set up the Audited Data (Values in KES '000)
data = {
    'Metric': ['Total Assets', 'Total Liabilities', 'Total Equity', 'Current Assets',
               'Current Liabilities', 'Revenue', 'EBIT', 'Net Income', 'Retained Earnings', 'Market Cap'],
    'FY2023': [32780931, 13566668, 19214263, 1731893, 13556384, 2953573, -1926027, -1356467, 17760370, 742500],
    'FY2024': [35186150, 14785418, 20400732, 6743038, 12833923, 3279053, -1961489, 1067075, 18827445, 675000]
}

df = pd.DataFrame(data).set_index('Metric')


def calculate_models(year):
    # Base Variables
    ta = df.loc['Total Assets', year]
    tl = df.loc['Total Liabilities', year]
    ca = df.loc['Current Assets', year]
    cl = df.loc['Current Liabilities', year]
    rev = df.loc['Revenue', year]
    ebit = df.loc['EBIT', year]
    re = df.loc['Retained Earnings', year]
    mkt_cap = df.loc['Market Cap', year]
    ni = df.loc['Net Income', year]
    wc = ca - cl

    # --- ALTMAN Z-SCORE ---
    z = (1.2 * (wc / ta)) + (1.4 * (re / ta)) + (3.3 * (ebit / ta)) + (0.6 * (mkt_cap / tl)) + (1.0 * (rev / ta))

    # --- SPRINGATE S-SCORE ---
    s = (1.03 * (wc / ta)) + (3.07 * (ebit / ta)) + (0.66 * (ni / cl)) + (0.4 * (rev / ta))

    # --- FULMER H-SCORE ---
    v1, v2 = re / ta, rev / ta
    v3 = ni / df.loc['Total Equity', year]
    v4 = (ni + 500000) / tl  # Estimated Cash Flow (NI + Approx Depreciation)
    v5, v6 = tl / ta, cl / ta
    v7 = np.log10(ta)
    v8 = wc / tl
    v9 = 0  # EBIT is negative, so Log(EBIT/Int) is penalized to 0

    h = (5.528 * v1) + (0.212 * v2) + (0.073 * v3) + (1.270 * v4) - (0.120 * v5) + (2.335 * v6) + (0.575 * v7) + (
                1.083 * v8) + (0.894 * v9) - 6.075

    return round(z, 4), round(s, 4), round(h, 4)


# Execute for both years
z23, s23, h23 = calculate_models('FY2023')
z24, s24, h24 = calculate_models('FY2024')

# 2. Visualization
models = ['Altman Z', 'Springate S', 'Fulmer H']
fy23 = [z23, s23, h23]
fy24 = [z24, s24, h24]
thresholds = [1.81, 0.862, 0]  # Thresholds for Safe vs Distress

x = np.arange(len(models))
plt.figure(figsize=(12, 7))
plt.bar(x - 0.2, fy23, width=0.4, label='FY2023', color='#a8dadc')
plt.bar(x + 0.2, fy24, width=0.4, label='FY2024', color='#457b9d')

# Custom Threshold Markers
plt.axhline(y=1.81, color='red', linestyle='--', alpha=0.6, label='Altman Safe (>1.81)')
plt.axhline(y=0.86, color='orange', linestyle='--', alpha=0.6, label='Springate Safe (>0.86)')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1, label='Fulmer Safe (>0)')

plt.xticks(x, models)
plt.ylabel('Model Score')
plt.title('EAPC Financial Distress Analysis: Multi-Model Comparison')
plt.legend()
plt.style.use('ggplot')
plt.show()

print(f"Results Compiled:\nFY2023: Z={z23}, S={s23}, H={h23}\nFY2024: Z={z24}, S={s24}, H={h24}")
