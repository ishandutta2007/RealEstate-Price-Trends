import matplotlib.pyplot as plt

# DATA SOURCE: Bank for International Settlements (BIS) via FRED (St. Louis Fed)
# Series ID: QCNN628BIS (Residential Property Prices for China)
# Base Year: 2010 = 100

# Years 2016 through 2026 (Q1)
years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

# Nominal Residential Property Price Index
nominal_index = [119.20, 125.15, 134.16, 139.23, 142.45, 144.75, 139.38, 134.20, 122.70, 115.66, 113.98]

# Real (Inflation-Adjusted) Residential Property Price Index
real_index = [115.30, 104.23, 109.44, 108.75, 111.21, 111.09, 105.04, 101.48, 92.60, 86.79, 85.13]

# Initialize the plot layout
plt.figure(figsize=(12, 7))

# Plot Nominal Index
plt.plot(years, nominal_index, color='#1f77b4', marker='o', linewidth=2, label='Nominal Index')
# Plot Real Index
plt.plot(years, real_index, color='#ff7f0e', marker='s', linewidth=2, label='Real Index (Inflation-Adjusted)')

# Annotate Nominal Index points (Offset slightly upwards)
for x, y in zip(years, nominal_index):
    plt.annotate(f"{y:.2f}", 
                 (x, y), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center', 
                 fontsize=9, 
                 fontweight='bold', 
                 color='#1f77b4')

# Annotate Real Index points (Offset slightly downwards to prevent overlap)
for x, y in zip(years, real_index):
    plt.annotate(f"{y:.2f}", 
                 (x, y), 
                 textcoords="offset points", 
                 xytext=(0, -15), 
                 ha='center', 
                 fontsize=9, 
                 fontweight='bold', 
                 color='#d62728')

# Graph customization
plt.title("China Residential Property Price Index Trend (2016 - 2026)\nBase Year: 2010 = 100", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Year", fontsize=11, labelpad=10)
plt.ylabel("Index Value", fontsize=11, labelpad=10)
plt.xticks(years)  # Ensure every year is shown on the X-axis
plt.grid(True, linestyle='--', alpha=0.5)

# Add Source Note to the Bottom Right of the plot
plt.figtext(0.99, 0.01, 'Source: Bank for International Settlements (FRED Series: QCNN628BIS)', 
            horizontalalignment='right', fontsize=9, style='italic', color='gray')

# Legend layout
plt.legend(loc='upper right', frameon=True, shadow=True, facecolor='white')

# Display the finalized plot
plt.tight_layout()
plt.show()
