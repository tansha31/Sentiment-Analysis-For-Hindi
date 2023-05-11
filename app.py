import pandas as pd
from PIL import Image
import streamlit as st
from requests import request

workingImg = Image.open("./assets/working.png")

# sidebar setup
with st.sidebar:
    st.markdown("# About")
    st.markdown(
        "This tool allows you to run sentiment analysis for Hindi language using a Machine Learning Model trained on Bhaav dataset."
    )
    st.markdown(
        "This tool is a work in progress. "
        "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "
        "with your feedback and suggestions. 💡"
    )
    st.markdown("---")
    st.markdown(
        "## How to use\n"
        "1. Type the text in the textbox for which you want to perform sentiment analysis.\n"
        "2. Click on submit button to run the model.\n"
        "3. The model will predict and classify the text as Positive, Negative or Neutral.\n"
    )
    st.markdown("---")
    st.markdown("## Training Results")
    st.markdown(
        "We have tried different machine learning models for text classification and following are the results."
    )
    df = {
        "model": [
            "KNN",
            "Naive Bayes",
            "Random Forest",
            "Logistic Regression",
            "Transformer (BERT)*",
        ],
        "accuracy": [50.70, 57.71, 57.82, 56.98, 73.47],
    }
    st.table(pd.DataFrame(df))
    st.markdown("*currently being used as the main model.")

# mainpage setup
st.write(
    "<h1 style='text-align: center; font-size: 2.5rem;'>Sentiment Analysis <span style='margin-left: 10px;'>☹️ 😐 😄</span></h1>",
    unsafe_allow_html=True,
)
st.write(
    "<p style='font-size: 1.1rem; margin: 20px 0; text-align: justify;'>Sentiment analysis, also known as opinion mining, is a natural language processing (NLP) technique for determining the positivity, negativity, or neutrality of data. It is frequently used on textual data to assist organizations in tracking brand and product sentiment in consumer feedback, and better understanding customer demands.</p>",
    unsafe_allow_html=True,
)
st.subheader("How does it work?")
st.write(
    "<p style='font-size: 1.1rem; text-align: justify'>The artificially intelligent bots are programmed to detect whether a message is favorable, negative, or neutral based on millions of pieces of text. Sentiment analysis divides communication into topic chunks and assigns each one a sentiment score.</p>",
    unsafe_allow_html=True,
)

st.image(workingImg)
st.markdown("")

# Model
st.header("Sentiment Analysis for Hindi")
input_text = st.text_area(
    label="Type or copy text for sentiment analysis.",
    height=200,
    placeholder="इस बॉक्स में अपना वाक्य टाइप करें ⌨️",
)

if st.button(label="Submit"):
    if input_text:
        with st.spinner("Please wait.... This may take a while ⏰"):
            response = request(
                method="POST", url=f"http://127.0.0.1:5000/predict?text={input_text}"
            )

            if response.status_code == 200:
                data = response.json()

                st.code(data)

                if data["label"] == "POSITIVE":
                    st.success("Sentiment: Positive")

                elif data["label"] == "NEUTRAL":
                    st.info("Sentiment: Neutral")

                else:
                    st.error("Sentiment: Negative")

            else:
                st.error("Oops something went wrong!")

    else:
        st.error("Please provide input to the model.")
