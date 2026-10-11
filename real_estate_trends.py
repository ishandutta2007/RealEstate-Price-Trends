import matplotlib.pyplot as plt

# ==============================================================================
# DATA SOURCE: Bank for International Settlements (BIS) via FRED (St. Louis Fed)
# Base Year: 2010 = 100
#
# Series IDs:
#   - China Nominal: QCNN628BIS
#   - China Real (Inflation-Adjusted): QC mathvariant / QCNR628BIS
#   - India Nominal: QINN628BIS
#   - India Real (Inflation-Adjusted): QINR628BIS
# ==============================================================================

# Timeline: 2016 through 2026 (Q4 values for annual markers, Q1 for 2026)
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

# --- China Data ---
china_nominal = [119.20, 125.15, 134.16, 139.23, 142.45, 144.75, 139.38, 134.20, 122.70, 115.66, 113.98]
china_real = [115.30, 104.23, 109.44, 108.75, 111.21, 111.09, 105.04, 101.48, 92.60, 86.79, 85.13]

# --- India Data ---
india_nominal = [253.13, 270.10, 279.90, 290.87, 298.60, 303.96, 321.14, 330.63, 353.37, 366.00, 366.84]
india_real = [170.00, 173.42, 175.40, 170.83, 167.22, 160.07, 159.71, 156.08, 157.88, 162.61, 161.94]

# Create subplots for comparison (2 side-by-side or stacked)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), sharex=True)

# Consistent color palette across both plots
COLOR_NOMINAL = '#1f77b4'  # Blue for Nominal
COLOR_REAL = '#e6550d'     # Orange for Real (Inflation-Adjusted)

# ----------------- China Subplot -----------------
ax1.plot(years, china_nominal, color=COLOR_NOMINAL, marker='o', linewidth=2.2, label='Nominal Index')
ax1.plot(years, china_real, color=COLOR_REAL, marker='s', linewidth=2.2, label='Real Index (Inflation-Adjusted)')

for x, y in zip(years, china_nominal):
    ax1.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 8),
                 ha='center', fontsize=8.5, fontweight='bold', color=COLOR_NOMINAL)

for x, y in zip(years, china_real):
    ax1.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, -14),
                 ha='center', fontsize=8.5, fontweight='bold', color=COLOR_REAL)

ax1.set_ylim(80, 155)
ax1.set_title("China: Residential Property Price Index\n(FRED: QCNN628BIS / QCNR628BIS)", fontsize=12, fontweight='bold', pad=12)
ax1.set_xlabel("Year", fontsize=11, labelpad=8)
ax1.set_ylabel("Index Value (2010 = 100)", fontsize=11, labelpad=8)
ax1.set_xticks(years)
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right', frameon=True, facecolor='white', shadow=True)

# ----------------- India Subplot -----------------
ax2.plot(years, india_nominal, color=COLOR_NOMINAL, marker='o', linewidth=2.2, label='Nominal Index')
ax2.plot(years, india_real, color=COLOR_REAL, marker='s', linewidth=2.2, label='Real Index (Inflation-Adjusted)')

for x, y in zip(years, india_nominal):
    ax2.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, 8),
                 ha='center', fontsize=8.5, fontweight='bold', color=COLOR_NOMINAL)

for x, y in zip(years, india_real):
    ax2.annotate(f"{y:.1f}", (x, y), textcoords="offset points", xytext=(0, -15),
                 ha='center', fontsize=8.5, fontweight='bold', color=COLOR_REAL)

ax2.set_ylim(140, 390)

ax2.set_title("India: Residential Property Price Index\n(FRED: QINN628BIS / QINR628BIS)", fontsize=12, fontweight='bold', pad=12)
ax2.set_xlabel("Year", fontsize=11, labelpad=8)
ax2.set_ylabel("Index Value (2010 = 100)", fontsize=11, labelpad=8)
ax2.set_xticks(years)
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='center right', frameon=True, facecolor='white', shadow=True)

# Overall Title and Footnote
fig.suptitle("Residential Property Price Trends (2016 - 2026): China vs India\nBase Year: 2010 = 100", 
             fontsize=14, fontweight='bold', y=0.98)
fig.text(0.99, 0.01, 'Source: Bank for International Settlements (BIS) via FRED', 
         horizontalalignment='right', fontsize=9, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.03, 1, 0.94])

# Save the figure for README embedding
output_image = "real_estate_trends_china_india.png"
plt.savefig(output_image, dpi=300, bbox_inches='tight')
print(f"Chart saved as {output_image}")

# Display the plot
plt.show()
