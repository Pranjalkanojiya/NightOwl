import streamlit as st

st.set_page_config(
    page_title="NightOwl",
    page_icon="📚",
    layout="wide"
)

st.title("📚 NightOwl")

st.markdown(
    """
    ### Your course material. Your sources. No hallucinations.

    Ask questions about your lecture notes, slides, PDFs and handwritten notes.
    """
)

st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📁 Course Materials")

    st.info(
        "Document upload will be available in the next step."
    )

with col2:
    st.subheader("💬 Ask your course")

    question = st.text_input(
        "Ask a question",
        placeholder="e.g. What is the difference between BFS and DFS?"
    )

    if st.button("Ask", type="primary"):
        if question.strip():
            st.warning(
                "Document retrieval is not connected yet. "
                "We'll build that next."
            )
        else:
            st.warning("Please enter a question.")

st.divider()

st.caption(
    "The Night Before • Evidence-based study assistant"
)