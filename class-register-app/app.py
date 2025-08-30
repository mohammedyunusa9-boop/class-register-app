
import streamlit as st
import pandas as pd

# Load Excel file
@st.cache_data
def load_data():
    df = pd.read_excel("CLASS REGISTER.xlsx")
    return df

st.set_page_config(page_title="Class Register", layout="wide")

st.title("📘 Class Register")

df = load_data()

# Search/Filter
search = st.text_input("🔍 Search by Name or ID")
if search:
    df = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]

# Show table
st.dataframe(df, use_container_width=True)

# Download updated Excel
st.download_button(
    label="📥 Download Register",
    data=df.to_csv(index=False),
    file_name="updated_register.csv",
    mime="text/csv"
)
