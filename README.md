
# MarketLens Nigeria

> Turning overlooked data into meaningful insights.

MarketLens Nigeria is a data-driven platform that makes historical food-price information across Borno and Yobe states accessible through interactive visualizations, market comparisons and AI-generated explanations.

Built for the **Build54 Unmapped Hackathon** using the Adaption API.

## Live Demo

- [Live Application](https://marketlens-nigeria.streamlit.app/)
- [Adapted Dataset on Hugging Face](https://huggingface.co/datasets/DominionofWeb3/marketlens-nigeria-food-prices)

## The Problem

Historical food-price information in northeastern Nigeria is often buried in technical datasets, making it difficult for researchers, communities and humanitarian organizations to understand regional price disparities and historical food affordability.

MarketLens Nigeria bridges this accessibility gap by transforming complex datasets into interactive and understandable information.

## Features

- **Market Comparison:** Compare historical food prices across markets within the same month.
- **Historical Price Trends:** Explore changes in food prices over time.
- **Interactive Market Map:** Visualize geographical market locations.
- **Data Exploration:** Search, filter and download historical food-price records.
- **AI Market Insights:** Access manually validated AI-generated explanations powered by the Adaption API.
- **Data Transparency:** Understand data freshness, measurement units and coverage limitations.

## Dataset Overview

The platform uses historical food-price data sourced from the World Food Programme (WFP).

| Attribute | Details |
|---|---|
| Historical records | 6,623 |
| Geographical coverage | Borno and Yobe |
| Commodities | 5 |
| Currency | Nigerian Naira (NGN) |
| Price type | Retail |
| Latest observation | November 15, 2025 |
| Validated AI explanations | 10 |

### Supported Commodities

- Local rice
- Red beans
- Millet
- Yam
- Palm oil

[Original Dataset](https://huggingface.co/datasets/electricsheepafrica/wfp-nigeria-food-prices)

## Data Preparation

The original dataset was processed through the following steps:

1. Filtered observations to Borno and Yobe states.
2. Selected five essential food commodities.
3. Retained valid retail price observations.
4. Checked for missing values and duplicate records.
5. Standardized prices into NGN per kilogram or litre.
6. Preserved source price flags and historical context.

## Adaption API Integration

The Adaption API was used to transform structured food-price observations into natural-language explanations.

### Initial Experiment

- Successfully processed 100 historical observations.
- Manual inspection identified inaccuracies in some generated explanations, particularly normalized prices and market names.

### Improved Experiment

- Restructured input data into clearly labelled context.
- Refined the prompt to prevent unnecessary price conversions and unsupported claims.
- Generated 10 additional explanations.
- All 10 explanations passed manual validation against their supplied context.

The validated explanations were published on Hugging Face and integrated into the live application.

## Key Findings

Using Adaption Visualize, the following historical insights were identified:

- Local rice prices increased significantly after 2022, reaching their highest annual median in 2024.
- Borno recorded higher median prices than Yobe across four compared staple foods in 2024.

| Commodity | Borno (NGN/kg) | Yobe (NGN/kg) | Difference |
|---|---:|---:|---:|
| Red beans | 1,913 | 1,360 | 40.7% |
| Millet | 769 | 600 | 28.2% |
| Local rice | 1,578 | 1,296 | 21.8% |
| Yam | 1,200 | 1,015 | 18.2% |

Percentage differences are relative to Yobe and calculated from rounded chart values.

Uneven market reporting also highlights the need for more consistent data collection across both states.

## Technology Stack

- Python
- Pandas
- Streamlit
- Plotly
- Adaption API
- Adaption Visualize
- Hugging Face
- Google Colab
- GitHub

## Project Structure

```text
marketlens-nigeria/
├── README.md
└── MarketLens-Nigeria/
    ├── app.py
    ├── requirements.txt
    └── marketlens_outputs/
        ├── marketlens_adaption_input.csv
        └── marketlens_adapted_validated.csv
```

## Running Locally

Clone the repository:

```bash
git clone https://github.com/dominion1000/marketlens-nigeria.git
cd marketlens-nigeria/MarketLens-Nigeria
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

## Intended Users

- Agricultural researchers
- Humanitarian organizations
- Food-security analysts
- Community organizations
- Policymakers
- Students and data enthusiasts

## Limitations

- The platform provides historical observations, not real-time market prices.
- Market reporting varies across locations, commodities and time periods.
- Historical prices alone cannot fully measure household food affordability.
- The validated AI dataset contains only 10 observations and is not representative of the entire dataset.
- The latest available observation is from November 2025.

## Future Improvements

- Integration of more recent food-price datasets.
- Expansion to additional Nigerian states.
- Improved mobile accessibility.
- Larger-scale AI adaptation and validation.
- Independent usability testing with affected communities and food-security experts.

## Acknowledgements

- Build54 Africa
- Adaption AI
- World Food Programme
- Electric Sheep Africa
- Hugging Face

---

**MarketLens Nigeria — Turning overlooked data into meaningful insights.**
