#import streamlit as st

#st.title("🎈 My new app")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)

import streamlit as st

# Title of the Streamlit app
st.title("Streamlit Slider Example")

# Slider to select a number between 0 and 100
number = st.slider("Pick a number", 0, 100)

# Slider to select a range of numbers
range_values = st.slider("Select a range", 0, 100, (20, 80))

# Display the selected number and range
st.write(f"You picked the number: {number}")
st.write(f"Range selected: {range_values[0]} to {range_values[1]}")


