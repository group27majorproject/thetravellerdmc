import random
import pandas as pd
import streamlit as st

# Load data (assuming local file for now)
df_responses = pd.read_excel("Sample Data.xlsx", sheet_name="Responses")

# Predefined activity pools
activity_pools = {
    "Team-building & corporate wellness": {
        "Morning": [
            "Beachside yoga session", "Wellness seminar", "Motivational keynote",
            "Mindfulness workshop", "Team trust-building games"
        ],
        "Afternoon": [
            "Sentosa Beach Olympics", "Siloso Beach BBQ & sports", "Group painting class",
            "Cooking class at Palate Sensations", "Team escape room challenge"
        ],
        "Evening": [
            "Sunset cruise with dinner", "Night Safari bonding walk",
            "Outdoor movie night at the hotel", "Team karaoke & dinner"
        ],
        "Accommodation": [
            "Sofitel Singapore Sentosa Resort & Spa", "Siloso Beach Resort - Sentosa"
        ]
    },
    "Business meetings & networking": {
        "Morning": [
            "Strategy workshop", "Business breakfast & seminar", "Keynote by industry expert"
        ],
        "Afternoon": [
            "Networking lunch", "Panel discussions", "Corporate innovation workshop"
        ],
        "Evening": [
            "Cocktail reception at Altro Zafferano", "Networking dinner with city view",
            "Singapore Sidecars evening city tour"
        ],
        "Accommodation": [
            "Carlton Hotel Singapore", "Concorde Hotel Singapore",
            "PARKROYAL COLLECTION Marina Bay"
        ]
    },
    "Executive retreats & incentive trips": {
        "Morning": [
            "Leadership roundtable", "Changi Jewel Forest tour", "Luxury breakfast cruise"
        ],
        "Afternoon": [
            "Private art gallery visit", "Golfing session at Sentosa",
            "Spa & relaxation at Capella"
        ],
        "Evening": [
            "Gourmet dining at Candlenut", "Royal Albatross yacht dinner",
            "Cultural immersion experience"
        ],
        "Accommodation": [
            "The Capitol Kempinski Hotel", "The Singapore EDITION",
            "The Fullerton Bay Hotel Singapore"
        ]
    }
}

# Generate itinerary

def generate_itinerary(tourism_type, duration):
    pool = activity_pools.get(tourism_type, activity_pools["Business meetings & networking"])
    accommodation = random.choice(pool["Accommodation"])
    itinerary = []

    for day in range(1, duration + 1):
        itinerary.append({
            "Day": day,
            "Morning": random.choice(pool["Morning"]),
            "Afternoon": random.choice(pool["Afternoon"]),
            "Evening": random.choice(pool["Evening"]),
            "Accommodation": accommodation
        })

    return pd.DataFrame(itinerary)

# Streamlit app
st.title("Singapore Itinerary Generator")

# User Inputs
tourism_type = st.selectbox(
    "Select Type of Tourism",
    list(activity_pools.keys())
)
duration = st.slider("Select Duration (Days)", 1, 7, 3)

if st.button("Generate Itinerary"):
    result = generate_itinerary(tourism_type, duration)
    st.subheader(f"{duration}-Day Itinerary for {tourism_type}")
    st.dataframe(result)
    st.download_button("Download Itinerary as Excel", data=result.to_csv(index=False), file_name="itinerary.csv")
