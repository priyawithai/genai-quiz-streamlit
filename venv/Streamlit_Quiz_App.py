import streamlit as st

# Generative AI Quiz Data
quiz_data = [
    {
        "question": "What does 'GPT' stand for in ChatGPT?",
        "options": [
            "Generative Pretrained Transformer",
            "General Purpose Tool",
            "Generated Python Text",
            "Google Processing Technology"
        ],
        "answer": "Generative Pretrained Transformer"
    },
    {
        "question": "Which company developed ChatGPT?",
        "options": [
            "OpenAI",
            "DeepMind",
            "Google",
            "Meta"
        ],
        "answer": "OpenAI"
    },
    {
        "question": "What is a common use of generative AI in creative industries?",
        "options": [
            "Creating deepfake videos",
            "Generating code snippets",
            "Writing stories and poems",
            "All of the above"
        ],
        "answer": "All of the above"
    },
    {
        "question": "Which term describes AI that generates text, images, audio, and video?",
        "options": [
            "Predictive AI",
            "Generative AI",
            "Reactive AI",
            "Sentient AI"
        ],
        "answer": "Generative AI"
    },
    {
        "question": "Which of these tools is used for generating AI images?",
        "options": [
            "Stable Diffusion",
            "Pandas",
            "NumPy",
            "BeautifulSoup"
        ],
        "answer": "Stable Diffusion"
    }
]

# Streamlit App Config
st.set_page_config(page_title="Are You Smarter Than a Gen AI?", page_icon="🧠", layout="centered")

st.title("🤖💡 Are You Smarter Than a Gen AI?")
st.caption("_Test your wits against the world of Generative AI!_")

# Initialize Session State
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.finished = False
    st.session_state.show_result = False
    st.session_state.selected_option = None

def reset_quiz():
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.finished = False
    st.session_state.show_result = False
    st.session_state.selected_option = None

# Show Quiz
if not st.session_state.finished:
    current = quiz_data[st.session_state.q_index]
    st.subheader(f"Q{st.session_state.q_index + 1}: {current['question']}")
    selected = st.radio("Select an answer:", current['options'], index=0, key=f"question_{st.session_state.q_index}")

    if st.button("Submit Answer"):
        st.session_state.selected_option = selected
        st.session_state.show_result = True
        if selected == current["answer"]:
            st.session_state.score += 1

    if st.session_state.show_result:
        if st.session_state.selected_option == current["answer"]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect!")

        st.info(f"✅ The correct answer is: **{current['answer']}**")

        if st.button("Next Question"):
            st.session_state.q_index += 1
            st.session_state.show_result = False
            st.session_state.selected_option = None
            if st.session_state.q_index >= len(quiz_data):
                st.session_state.finished = True
            st.experimental_rerun()
else:
    st.balloons()
    st.markdown("### 🎉 Quiz Complete!")
    st.markdown(f"**Your Score: {st.session_state.score} / {len(quiz_data)}**")
    if st.button("Restart Quiz"):
        reset_quiz()
        st.experimental_rerun()
