import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import re


# Page Configuration
st.set_page_config(page_title="FurOmics", page_icon="🐾", layout="centered")

# Function to add email to Google Sheets
def add_email_to_sheet(email):
    try:
        # Set up Google Sheets API client
        scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets.google.to_dict(), scopes)
        client = gspread.authorize(creds)

        # Open the sheet and append the email
        sheet = client.open("FurOmics Waitlist").sheet1
        sheet.append_row([email])

        return True
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

# Header
st.title("FurOmics 🐈 🦮🐾")
st.subheader("The Omics solution to our furry friends!")
st.image("catanddog_300x200.jpg", caption="Healthy pets, happier lives.")

# About Section
st.header("About Us")
st.write("""
Using DeepLearning under the hood Fur Omics platform is dedicated to do comprehensive genomics analysis that aims
to provide insights into the genetic factors that contribute to the health and well-being of our pets.
Our mission is to provide personalized insights to pet owners and veterinarians.
""")

st.subheader("COMING SOON!")
# Waitlist Form
st.header("Join Our Waitlist")
email = st.text_input("Enter your email to stay updated:")
if st.button("Join Waitlist"):
    if email and re.match(r"^[a-z0-9]+@[^@]+\.[a-z]+$", email):
        success = add_email_to_sheet(email)
        if success:
            st.success("Thank you for joining the waitlist!")
    else:
        st.error("Please enter a valid email address.")


# Footer
st.markdown("---")
st.write("Follow us on [X](https://x.com/FurOmics) | [email](mailto:info@furomics.com)")
