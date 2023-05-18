import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Quirky | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):


    st.write("**Twitter:** [@quirkyswirl](https://twitter.com/QuirkySwirl)")
    st.write("**Mail** : info@iyer.dev")
    st.write("**Demo ONLY**")

    st.write("**Original Source:**",
"[Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot)")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Quirky, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm Quirky, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive natural language interactions. My goal is to help you better understand your data.
    I support PDF, TXT, and CSV data, with more coming soon! 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 Quirky's Pages")
st.write("""
- **Quirky-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (can't process the whole file just index useful parts(max 4) for respond to the user ) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html) + (soon) Summarize data
- **Quirky-Sheet** : Chat on tabular data (CSV) | for precise information | can process the whole file (with python code) | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation (experimental)

""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**Quirky is not under regular development - this is just a demo project. !**
""", unsafe_allow_html=True)





