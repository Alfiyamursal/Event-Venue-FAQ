import streamlit as st

st.title("🏢 Event Venue FAQ Chatbot")

st.write("Ask me about venue booking, pricing, facilities, and more!")

# FAQ database
faq = {
    "capacity": "Our venue can accommodate up to 500 guests.",
    "booking": "You can book the venue by filling out the booking form on our website or calling our office.",
    "price": "The rental price starts from ₹50,000 per event depending on the package.",
    "parking": "Yes, we provide parking space for up to 200 vehicles.",
    "catering": "We offer in-house catering services with customizable menu options.",
    "timing": "The venue is available from 9 AM to 11 PM.",
    "contact": "You can contact us at +91-9876543210 or email venue@example.com."
}

user_input = st.text_input("Enter your question:")

if user_input:
    user_input = user_input.lower()
    response = "Sorry, I couldn't find information about that. Please contact support."

    for key in faq:
        if key in user_input:
            response = faq[key]
            break

    st.success(response)