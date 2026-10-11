<p align="center">
  <img src="assets/banner.svg" alt="Residential Property Price Trends: China vs India" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007/RealEstate-Price-Trends/stargazers"><img src="https://img.shields.io/github/stars/ishandutta2007/RealEstate-Price-Trends?style=flat-square&logo=github" alt="GitHub_Stars" /></a>
  <a href="https://github.com/ishandutta2007/RealEstate-Price-Trends/network/members"><img src="https://img.shields.io/github/forks/ishandutta2007/RealEstate-Price-Trends?style=flat-square&logo=github" alt="GitHub forks" /></a>
  <a href="https://github.com/ishandutta2007/RealEstate-Price-Trends/issues"><img src="https://img.shields.io/github/issues/ishandutta2007/RealEstate-Price-Trends?style=flat-square" alt="GitHub issues" /></a>
  <a href="https://github.com/ishandutta2007/RealEstate-Price-Trends/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License: MIT" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square&logo=python&logoColor=white" alt="Python 3.8+" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</p>

# 🏘️ Residential Property Price Trends (2016 – 2026): China vs. India 📈

A comprehensive comparative analysis of residential property price indices across **China** 🇨🇳 and **India** 🇮🇳 using authoritative quarterly economic data from the **Bank for International Settlements (BIS)** via the **Federal Reserve Bank of St. Louis (FRED)** database.

---

## 📊 Overview & Comparative Plot 🖼️

![China vs India Residential Property Price Trends](real_estate_trends_china_india.png)

---

## 🔍 Key Insights & Dynamics 💡

| Metric / Country | **China** (🇨🇳) | **India** (🇮🇳) |
| :--- | :--- | :--- |
| 🏷️ **Nominal Trend** | Rose steadily to peak at **144.75** (2021) before dropping to **113.98** (2026). | Surged strongly and consistently from **253.13** (2016) to **366.84** (2026). |
| 📉 **Real Trend (Inflation-Adjusted)** | Hovered around 104–115 until 2021; fell below 2010 baseline to **85.13** in 2026. | Remained largely resilient in the 156–175 range, finishing at **161.94** in 2026. |
| 🏗️ **Market Driver** | Regulatory de-leveraging ("Three Red Lines"), developer liquidity contractions, and demographic headwinds. | Strong domestic urban housing demand, economic expansion, and post-pandemic premium residential uptake. |

---

## 🗃️ Data Source Details 📚

All series are indexed with **2010 = 100** and published by the **Bank for International Settlements (BIS)** 🏛️:

| Country | Metric | FRED Series ID | Frequency |
| :--- | :--- | :--- | :--- |
| 🇨🇳 **China** | Residential Property Prices (Nominal) | [`QCNN628BIS`](https://fred.stlouisfed.org/series/QCNN628BIS) | 📅 Quarterly |
| 🇨🇳 **China** | Real Residential Property Prices (Inflation-Adjusted) | [`QCNR628BIS`](https://fred.stlouisfed.org/series/QCNR628BIS) | 📅 Quarterly |
| 🇮🇳 **India** | Residential Property Prices (Nominal) | [`QINN628BIS`](https://fred.stlouisfed.org/series/QINN628BIS) | 📅 Quarterly |
| 🇮🇳 **India** | Real Residential Property Prices (Inflation-Adjusted) | [`QINR628BIS`](https://fred.stlouisfed.org/series/QINR628BIS) | 📅 Quarterly |

---

## 🚀 How to Run the Script 💻

### 🛠️ Prerequisites
Make sure you have Python 3 and `matplotlib` installed:

```bash
pip install matplotlib
```

### ⚡ Execution
Run the visualization script:

```bash
python real_estate_trends.py
```

The script will render the side-by-side comparative chart and export an updated high-resolution figure at [`real_estate_trends_china_india.png`](real_estate_trends_china_india.png) 🎨.

---

## 📈 Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=ishandutta2007/RealEstate-Price-Trends&type=date&legend=top-left)](https://star-history.dera.page/#ishandutta2007/RealEstate-Price-Trends&type=date&legend=top-left)

---

## 💖 Support & Sponsoring ☕

Thank you for checking out this project! If you found this analysis helpful, insightful, or interesting, please consider:
- ⭐ **Starring** this repository to show your appreciation
- 🍴 **Forking** the repo to contribute or extend the research
- 📢 **Sharing** with fellow researchers, analysts, and developers

If you'd like to support my open-source work and buy me a coffee, you can sponsor me on GitHub:

<p align="left">
  <a href="https://github.com/sponsors/ishandutta2007">
    <img src="https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?style=for-the-badge&logo=github-sponsors" alt="Sponsor on GitHub" />
  </a>
  <a href="https://github.com/sponsors/ishandutta2007">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee" />
  </a>
</p>

Your generous support is greatly appreciated! 🙌
