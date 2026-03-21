import streamlit as st

CIPHER_MAP = {
    'a': 'Chinga', 'b': 'Chong', 'c': 'Ching', 'd': 'Cheng',
    'e': 'Chinge', 'f': 'Fing', 'g': 'Guangdong', 'h': 'Hong',
    'i': 'Yi', 'j': 'Jiang', 'k': 'Kong', 'l': 'Long',
    'm': 'Ming', 'n': 'Nigga', 'o': 'Osaka', 'p': 'Penis',
    'q': 'Qidong', 'r': 'Rice', 's': 'Suck', 't': 'Trachea',
    'u': 'Underwear', 'v': 'Vietnam', 'w': 'Wongwenxi', 'x': 'Xray',
    'y': 'Yotta', 'z': 'Zebrawoman', ' ': '-', '-': '*'
}
REVERSE_MAP = {v.lower(): k for k, v in CIPHER_MAP.items()}


def encrypt_sentence(sentence):
    return " ".join(CIPHER_MAP.get(char, char) for char in sentence.lower())


def decode_description(encoded_text):
    words = encoded_text.split()
    return "".join(REVERSE_MAP.get(word.lower(), word) for word in words)


st.set_page_config(page_title="Mingish Translator", page_icon="🇨🇳")

st.title("Mingish Translator")
st.write("Translate Mingish to English or English to Mingish")

mode = st.sidebar.selectbox("Functions", ["English -> Mingish", "Mingish -> English"])

user_input = st.text_area("Input your text:", placeholder="input your text here")

if st.button("translate"):
    if user_input:
        if mode == "English -> Mingish":
            result = encrypt_sentence(user_input)
            st.success("translated to Mingish!")
        else:
            result = decode_description(user_input)
            st.success("translated to English!")

        st.text_area("Output:", value=result, height=400, disabled=True)
    else:
        st.warning("check ur input retard.")

st.divider()
st.caption("Wongwenxi Chinge - Long Osaka Vietnam Chinge - Hong Chinga Suck Chinga Nigga")
