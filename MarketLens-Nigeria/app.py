
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MarketLens Nigeria",
    page_icon="📊",
    layout="wide"
)


from pathlib import Path

@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parent

    data_path = (
        base_dir
        / "marketlens_outputs"
        / "marketlens_adaption_input.csv"
    )

    df = pd.read_csv(data_path)
    df["date"] = pd.to_datetime(df["date"])
    return df


df = load_data()

st.title("📊 MarketLens Nigeria")
st.markdown(
    "Making historical food-price data accessible "
    "across underserved Nigerian communities."
)

st.info(
    "This platform presents historical food-price "
    "observations, not live market prices."
)

# Overview
c1, c2, c3, c4 = st.columns(4)

c1.metric("Price records", f"{len(df):,}")
c2.metric("States", df["state"].nunique())
c3.metric("Markets", df["market_id"].nunique())
c4.metric("Food commodities", df["commodity"].nunique())

st.caption(
    f"Latest observation: {df['date'].max():%d %B %Y}"
)

# Filters
st.sidebar.header("Explore food prices")

commodity = st.sidebar.selectbox(
    "Select food",
    sorted(df["commodity"].unique())
)

states = st.sidebar.multiselect(
    "Select states",
    sorted(df["state"].unique()),
    default=sorted(df["state"].unique())
)

filtered = df[
    (df["commodity"] == commodity) &
    (df["state"].isin(states))
]

if filtered.empty:
    st.warning("Select at least one state.")
    st.stop()

unit = filtered["price_unit"].iloc[0]

tab1, tab2, tab3, tab4 = st.tabs([
    "Market comparison",
    "Historical trends",
    "Market map",
    "Explore data"
])

# Market comparison
with tab1:
    st.subheader("Compare historical market prices")

    months = sorted(
        filtered["observation_month"].unique(),
        reverse=True
    )

    month = st.selectbox("Observation month", months)

    monthly = filtered[
        filtered["observation_month"] == month
    ]

    comparison = monthly.groupby(
        ["state", "market", "market_id"],
        as_index=False
    )["price_per_unit_ngn"].median()

    comparison = comparison.sort_values(
        "price_per_unit_ngn"
    )

    comparison["location"] = (
        comparison["market"] + ", " +
        comparison["state"]
    )

    st.metric(
        "Markets with observations",
        len(comparison)
    )

    if len(comparison) < 2:
        st.warning(
            "Insufficient market coverage for "
            "a meaningful comparison."
        )

    fig = px.bar(
        comparison,
        x="price_per_unit_ngn",
        y="location",
        color="state",
        orientation="h",
        labels={
            "price_per_unit_ngn": unit,
            "location": "Market"
        },
        title=f"{commodity} — {month}"
    )

    fig.update_layout(
        yaxis={"autorange": "reversed"}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Only markets with observations in the selected "
        "month are included. Missing markets do not "
        "indicate unavailable food."
    )

# Historical trends
with tab2:
    st.subheader("How food prices changed over time")

    trend = filtered.groupby(
        ["observation_month", "state"],
        as_index=False
    )["price_per_unit_ngn"].median()

    trend = trend.sort_values("observation_month")

    fig = px.line(
        trend,
        x="observation_month",
        y="price_per_unit_ngn",
        color="state",
        markers=True,
        labels={
            "observation_month": "Month",
            "price_per_unit_ngn": unit
        },
        title=f"Historical median price of {commodity}"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Changes may reflect both price movements "
        "and differences in market coverage."
    )

# Market map
with tab3:
    st.subheader("Geographical market coverage")

    locations = filtered.dropna(
        subset=["latitude", "longitude"]
    ).drop_duplicates(subset=["market_id"])

    st.map(
        locations,
        latitude="latitude",
        longitude="longitude"
    )

    st.caption(
        "Locations represent markets covered by "
        "the historical dataset."
    )

# Raw data explorer
with tab4:
    st.subheader("Explore historical observations")

    search = st.text_input("Search for a market")

    results = filtered[
        filtered["market"].str.contains(
            search,
            case=False,
            na=False,
            regex=False
        )
    ]

    st.dataframe(
        results[[
            "date",
            "state",
            "lga",
            "market",
            "commodity",
            "original_price_ngn",
            "unit",
            "price_per_unit_ngn",
            "price_unit",
            "record_class"
        ]],
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        "Download filtered data",
        results.to_csv(index=False),
        file_name="marketlens_filtered.csv",
        mime="text/csv"
    )

st.divider()

st.subheader("About the data")

st.write(
    "MarketLens uses historical WFP Nigeria food-price "
    "observations to improve access to market information "
    "in Borno and Yobe."
)

st.write(
    "Prices have been normalized to Nigerian naira "
    "per kilogram or litre using the source unit labels."
)

st.write(
    "The dataset contains reported and aggregated "
    "observations. Coverage varies across markets and dates."
)

st.markdown(
    "[View original dataset]"
    "(https://huggingface.co/datasets/"
    "electricsheepafrica/wfp-nigeria-food-prices)"
)

st.caption("MarketLens Nigeria | Build54 Unmapped")
