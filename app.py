from rag import generate_answer
from extractor import extract
from chunker import chunk_documents
from embeddings import create_embeddings
from vector_store import VectorStore
import os
import shutil
import html
import streamlit as st

# ---------- CONFIG ----------
st.set_page_config("NightOwl", "🦉", "wide")

UPLOAD_DIR = "data/documents"
STATIC_DIR = "static"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)


# ---------- HELPERS ----------
def sync_static_files():
    """Keep uploaded files available for clickable source links."""
    for filename in os.listdir(STATIC_DIR):
        path = os.path.join(STATIC_DIR, filename)
        if os.path.isfile(path):
            os.remove(path)

    for filename in os.listdir(UPLOAD_DIR):
        source = os.path.join(UPLOAD_DIR, filename)
        destination = os.path.join(STATIC_DIR, filename)

        if os.path.isfile(source):
            shutil.copy2(source, destination)


@st.cache_resource
def build_store(files):
    store = VectorStore()

    for file in files:
        documents = extract(os.path.join(UPLOAD_DIR, file))
        chunks = chunk_documents(documents)

        if chunks:
            embeddings = create_embeddings(
                [chunk["text"] for chunk in chunks]
            )
            store.add(chunks, embeddings)

    return store


def delete_file(filename):
    path = os.path.join(UPLOAD_DIR, filename)

    if os.path.exists(path):
        os.remove(path)

    static_path = os.path.join(STATIC_DIR, filename)

    if os.path.exists(static_path):
        os.remove(static_path)

    build_store.clear()


def open_source_url(filename, page):
    from urllib.parse import quote

    safe_filename = quote(filename)
    return f"/app/static/{safe_filename}#page={page}"


# ---------- STYLE ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

* {font-family:Inter,sans-serif}

.stApp {
    background:
        radial-gradient(circle at 85% 0%, #18245c 0, transparent 30%),
        radial-gradient(circle at 5% 90%, #102d4d 0, transparent 25%),
        #060914;
}

.block-container {
    max-width:1250px;
    padding:2.5rem 2rem 4rem;
}

header,#MainMenu,footer {visibility:hidden}

section[data-testid="stSidebar"] {
    background:#080b14;
    border-right:1px solid #ffffff0d;
}

.logo {
    display:flex;
    align-items:center;
    gap:10px;
    font-size:23px;
    font-weight:800;
}

.owl {
    width:42px;
    height:42px;
    border-radius:13px;
    display:grid;
    place-items:center;
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    box-shadow:0 0 25px #4f46e555;
    font-size:23px;
}

.sub {
    color:#64748b;
    font-size:10px;
    margin-left:52px;
    margin-top:-7px;
    letter-spacing:1px;
}

.eyebrow {
    color:#818cf8;
    font-size:11px;
    font-weight:700;
    letter-spacing:2px;
}

.hero {
    font-size:46px;
    line-height:1.05;
    font-weight:800;
    letter-spacing:-2px;
}

.gradient {
    background:linear-gradient(90deg,#8b9cff,#b28cff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.desc {
    color:#94a3b8;
    font-size:15px;
    line-height:1.7;
    max-width:680px;
    margin-top:15px;
}

.status {
    display:inline-flex;
    gap:7px;
    align-items:center;
    padding:7px 12px;
    border-radius:30px;
    background:#22c55e12;
    border:1px solid #22c55e30;
    color:#86efac;
    font-size:11px;
    font-weight:600;
}

.dot {
    width:7px;
    height:7px;
    border-radius:50%;
    background:#22c55e;
    box-shadow:0 0 10px #22c55e;
}

.upload-card {
    padding:30px;
    text-align:center;
    border-radius:20px;
    border:1px dashed #6366f155;
    background:linear-gradient(145deg,#101632aa,#0b1020aa);
    box-shadow:0 15px 45px #00000025;
    margin:20px 0 28px;
}

.upload-icon {
    font-size:34px;
    margin-bottom:8px;
}

.upload-title {
    font-size:17px;
    font-weight:700;
    color:#f8fafc;
}

.upload-sub {
    color:#64748b;
    font-size:12px;
    margin-top:7px;
}

.card,.stat {
    background:#0d1223b8;
    border:1px solid #94a3b51c;
    border-radius:18px;
    padding:20px;
    box-shadow:0 15px 45px #00000025;
}

.stat {
    border-radius:16px;
}

.value {
    font-size:27px;
    font-weight:800;
    color:#f8fafc;
}

.small {
    color:#64748b;
    font-size:10px;
    letter-spacing:1px;
}

div[data-testid="stTextInput"] input {
    background:#080c1ae6 !important;
    border:1px solid #29345d !important;
    border-radius:14px !important;
    color:white !important;
    height:55px !important;
}

.stButton > button {
    background:linear-gradient(135deg,#4f46e5,#7c3aed) !important;
    color:white !important;
    border:0 !important;
    border-radius:12px !important;
    font-weight:700 !important;
    min-height:45px !important;
    box-shadow:0 8px 25px #4f46e540;
}

.delete-btn button {
    background:#ef444415 !important;
    border:1px solid #ef444440 !important;
    color:#fca5a5 !important;
    box-shadow:none !important;
    min-height:32px !important;
}

.source-btn {
    margin-top:8px;
}

.doc {
    padding:10px 12px;
    margin:7px 0;
    border-radius:11px;
    background:#0f172aa6;
    border:1px solid #94a3b312;
}

.doc b {
    font-size:12px;
    color:#dbeafe;
}

.doc small {
    display:block;
    color:#64748b;
    font-size:10px;
    margin-top:3px;
}

div[data-testid="stForm"] {
    border:0 !important;
    padding:0 !important;
}

.ask-button button {
    width:100%;
    min-height:48px !important;
    font-size:14px !important;
}
</style>
""", unsafe_allow_html=True)


# ---------- HELPERS ----------
def stat(value, label):
    st.markdown(
        f"""
        <div class="stat">
            <div class="value">{value}</div>
            <div class="small">{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- HERO ----------
hero, status = st.columns([5, 1])

with hero:

    st.markdown(
        '<div class="eyebrow">EVIDENCE-FIRST LEARNING</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero">
            Study smarter.<br>
            <span class="gradient">Trust your sources.</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="desc">
            Ask questions about your actual course material.
            NightOwl finds the evidence, explains the answer,
            and shows you exactly where it came from.
        </div>
        """,
        unsafe_allow_html=True
    )

with status:

    st.markdown(
        """
        <div style="text-align:right">
            <span class="status">
                <span class="dot"></span>
                SYSTEM READY
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- UPLOAD ----------
st.markdown(
    """
    <div class="upload-card">
        <div class="upload-icon">📚</div>
        <div class="upload-title">
            Build your knowledge vault
        </div>
        <div class="upload-sub">
            Upload lecture PDFs, slides, notes or handwritten pages
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

uploads = st.file_uploader(
    "Upload course material",
    type=["pdf", "pptx", "txt", "md", "jpg", "jpeg", "png"],
    accept_multiple_files=True,
    label_visibility="collapsed"
)

if uploads:

    new_files = 0

    for file in uploads:

        path = os.path.join(UPLOAD_DIR, file.name)

        # Avoid unnecessary rewrite if the file already exists
        if not os.path.exists(path):
            with open(path, "wb") as out:
                out.write(file.getbuffer())

            new_files += 1

    if new_files:
        build_store.clear()
        sync_static_files()

        st.success(f"✓ {new_files} new file(s) added")

        # Refresh so the new files immediately appear in the sidebar
        st.rerun()

# ---------- DOCUMENT MANAGER ----------

st.markdown("### 📚 Your Course Material")

files = sorted(
    [
        f for f in os.listdir(UPLOAD_DIR)
        if os.path.isfile(
            os.path.join(UPLOAD_DIR, f)
        )
    ]
)

if files:

    st.caption(
        f"{len(files)} document(s) currently stored"
    )

    for file in files:

        file_path = os.path.join(
            UPLOAD_DIR,
            file
        )

        size = os.path.getsize(file_path) / 1024

        document_col, delete_col = st.columns([6, 1])

        with document_col:

            st.markdown(
                f"""
                <div class="doc">
                    📄 <b>{html.escape(file)}</b>
                    <small>
                        {size:.1f} KB · Available for questions
                    </small>
                </div>
                """,
                unsafe_allow_html=True
            )

        with delete_col:

            if st.button(
                "🗑 Delete",
                key=f"delete_document_{file}",
                help=f"Delete {file}"
            ):

                delete_file(file)

                st.toast(
                    f"{file} deleted",
                    icon="🗑️"
                )

                st.rerun()

else:

    st.info("No course material uploaded yet.")
    
# ---------- ASK ----------
st.markdown("### 💬 Ask your course")

with st.form("question_form"):

    question = st.text_input(
        "Ask NightOwl",
        placeholder="Ask something from your study material...",
        label_visibility="collapsed"
    )

    st.markdown('<div class="ask-button">', unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "🦉 Ask NightOwl"
    )

    st.markdown("</div>", unsafe_allow_html=True)


if submitted:

    files = sorted(
        [
            f for f in os.listdir(UPLOAD_DIR)
            if os.path.isfile(os.path.join(UPLOAD_DIR, f))
        ]
    )

    if not question.strip():

        st.warning("Please enter a question.")

    elif not files:

        st.warning("Upload study material first.")

    else:

        with st.spinner("Searching your knowledge vault..."):

            sync_static_files()

            store = build_store(files)

            question_embedding = create_embeddings(
                [question]
            )[0]

            results = store.search(
                question_embedding,
                k=5,
                threshold=0.40
            )

        if not results:

            st.warning(
                "I couldn't find enough information "
                "in your uploaded material."
            )

        else:

            with st.spinner("Thinking from your course material..."):

                answer = generate_answer(
                    question,
                    results
                )

            st.markdown("### Answer")

            st.markdown(
                f"""
                <div class="card">
                    {answer}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### Sources")

            for index, result in enumerate(results):

                chunk = result["chunk"]

                st.markdown(
                    f"""
                    <div class="doc">
                        📄 <b>{html.escape(chunk['source'])}</b>
                        <small>
                            Page {chunk['page']}
                            · Relevance {result['score']:.2f}
                        </small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                source_url = open_source_url(
                    chunk["source"],
                    chunk["page"]
                )

                st.link_button(
                    f"↗ Open {chunk['source']} · Page {chunk['page']}",
                    source_url,
                    use_container_width=True
                )


# ---------- STATS ----------
st.write("")

files = sorted(
    [
        f for f in os.listdir(UPLOAD_DIR)
        if os.path.isfile(os.path.join(UPLOAD_DIR, f))
    ]
)

cols = st.columns(4)

for col, value, label in zip(
    cols,
    [len(files), "—", "—", "0%"],
    ["DOCUMENTS", "PAGES INDEXED", "QUESTIONS ASKED", "UNSUPPORTED ANSWERS"]
):

    with col:
        stat(value, label)


st.markdown(
    """
    <div style="
        text-align:center;
        color:#475569;
        font-size:11px;
        margin-top:30px;
    ">
        🦉NightOwl · Evidence over assumptions
    </div>
    """,
    unsafe_allow_html=True
)