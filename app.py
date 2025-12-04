import streamlit as st
from dotenv import load_dotenv
from crew import travel_crew

load_dotenv()

st.title("🌍 Travel Assistant")

departure = st.text_input("Enter Departure Code")
arrival = st.text_input("Enter Arrival Code")

if st.button("Get Travel Info"):
    if not departure or not arrival:
        st.error("Both Departure and Arrival are required!")
    else:
        with st.spinner("Fetching travel info... ✈️🏨"):
            try:
                inputs = {"departure": departure, "arrival": arrival}
                result = travel_crew.kickoff(inputs=inputs)

                st.success("Travel Info Retrieved ✅")
                st.markdown("---")

                if hasattr(result, 'tasks_output') and result.tasks_output:
                    st.markdown("## ✈️ Available Flights")
                    st.markdown(result.tasks_output[0].raw)
                    st.markdown("---")

                    st.markdown("## 🏨 Recommended Hotels")
                    st.markdown(result.tasks_output[1].raw)
                    st.markdown("---")

                    st.markdown("## 📅 Travel Itinerary")
                    st.markdown(result.tasks_output[2].raw)
                    st.markdown("---")

                    st.markdown("## 💡 Travel Tips & Safety")
                    st.markdown(result.tasks_output[3].raw)
                else:
                    st.markdown("## 🌍 Your Complete Travel Plan")
                    st.markdown(result.raw if hasattr(
                        result, 'raw') else str(result))
            except Exception as e:
                st.error(f"An error occurred: {e}")
