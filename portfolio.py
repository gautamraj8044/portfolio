import streamlit as st

# Basic Configurations
st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="wide")

# Header
st.title("Welcome to My Portfolio")
st.write("Hi, I'm Gautam Raj, a Python Developer with a passion for NLP, Machine Learning, and AI.")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Projects", "Skills", "Contact", "Resume"])

# Home Section
if page == "Home":
    st.header("About Me")
    st.write("""
    I’m a Python developer with 6 months of experience, specializing in:
    - Natural Language Processing (NLP)
    - Machine Learning and Deep Learning
    - Large Language Models (LLMs)
    - Chatbot Creation
    - MySQL Databases
    - RESTful API Development
    """)
    st.write("I have worked on several projects involving OCR, sentiment analysis, and more.")

# Projects Section
elif page == "Projects":
    st.header("My Projects")
    st.subheader("Project 1: Chatbot with Ollama")
    st.write("Developed a chatbot using Ollama 3, Chainlit for UI, Hugging Face embedding, and Chroma DB.")
    
    st.subheader("Project 2: Sentiment Analysis on IMDb Reviews")
    st.write("Built a Logistic Regression model for sentiment analysis using IMDb reviews, with text preprocessing using spaCy.")
    
    st.subheader("Project 3: PDF Processing with OCR")
    st.write("Used PaddleOCR for text extraction from PDFs, embedded using Ollama, and stored in Chroma vector database.")
    
    # Add more projects as needed

# Skills Section
elif page == "Skills":
    st.header("My Skills")
    st.write("""
    - **Languages**: Python, SQL
    - **Libraries/Frameworks**: Pandas, NumPy, Matplotlib, Flask, Scikit-learn, PyTorch
    - **Databases**: MySQL, MongoDB
    - **Version Control**: Git, GitHub
    """)
    st.write("I’m continuously learning and expanding my skill set in the field of AI and Machine Learning.")

# Contact Section
elif page == "Contact":
    st.header("Get in Touch")
    st.write("Feel free to reach out to me via the following channels:")
    st.write("- **Email**: [gautamraj8044@gmail.com](mailto:gautamraj8044@gmail.com)")
    st.write("- **LinkedIn**: [Your LinkedIn](https://www.linkedin.com/in/gautamraj8044/)")
    st.write("- **GitHub**: [Your GitHub](https://github.com/gautamraj8044)")

    st.write("I’m always open to discussing new projects, creative ideas, or opportunities to be part of your vision.")

# Resume Section
elif page == "Resume":
    st.header("Download My Resume")
    st.write("You can download my resume in PDF format by clicking the button below.")
    
    with open("resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="resume.pdf",
            mime="application/pdf"
        )
