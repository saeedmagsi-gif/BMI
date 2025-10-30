import streamlit as st

# 🧮 Title and Description
st.set_page_config(page_title="BMI Calculator", page_icon="🧮", layout="centered")

st.title("🧮 BMI Calculator")
st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

# 🧍 Inputs
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.5)
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.5)

# 🧠 BMI Calculation
if st.button("Calculate BMI 🚀"):
    height_m = height / 100  # convert cm to meters
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight 😔"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight 😊"
    elif 25 <= bmi < 29.9:
        category = "Overweight 😐"
    else:
        category = "Obesity 😟"

    st.markdown(f"### Your BMI is **{bmi:.2f}**")
    st.markdown(f"**Category:** {category}")

# 🧡 Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit and Python")
