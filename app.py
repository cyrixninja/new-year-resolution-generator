import os
import openai
import base64
import streamlit as st


openai.api_key = "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" #openAI  API Key

st.title("New Year Resolution Generator")
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
       data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background.png')


def random():
    if st.button('Click to Generate'):
        response = openai.Completion.create(
        engine="babbage-instruct-beta",
        prompt="Create a new year resolution for the year 2022 :\n\n1.",
        temperature=0.8,
        max_tokens=75,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n\n"]
        )
        resp=response['choices'][0]['text']
        split_string = resp.split("/n", 1)
        string = split_string[0]
        st.header(string)
def profession():
    text = st.text_input('Enter your profession')
    genpromt= ("Create a new year resolution for year 2022 profession of"+"  "+ text +" :\n\n1 ")


    if st.button('Click to Generate'):
        response = openai.Completion.create(
        engine="babbage-instruct-beta",
        prompt=genpromt,
        temperature=0.8,
        max_tokens=75,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n\n"]
        )
        resp=response['choices'][0]['text']
        split_string = resp.split("\n", 1)
        string = split_string[0]
        st.header(string)

def goals():
    text = st.text_input('Enter your goal')
    genpromt= ("Create a new year resolution for goal of"+"  "+ text +" :\n\n1 ")


    if st.button('Click to Generate'):
        response = openai.Completion.create(
        engine="babbage-instruct-beta",
        prompt=genpromt,
        temperature=0.8,
        max_tokens=75,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n\n"]
        )
        resp=response['choices'][0]['text']
        split_string = resp.split("\n", 1)
        string = split_string[0]
        st.header(string)


option = st.selectbox(
      'Select an Option',
     ('Generate a Random New Year Resolution', 'Generate a Random New Year Resolution as per your Profession', 'Generate a Random New Year Resolution as per your Goals'))

if option=='Generate a Random New Year Resolution':
    random()
    
elif option=='Generate a Random New Year Resolution as per your Profession':
    profession()
elif option=='Generate a Random New Year Resolution as per your Goals':
    goals()
    

    
