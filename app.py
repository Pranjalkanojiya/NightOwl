import os
import streamlit as st

# ---------- CONFIG ----------
st.set_page_config("NightOwl", "🦉", "wide")

UPLOAD_DIR = "data/documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)


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

/* Logo */
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

/* Hero */
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

/* Status */
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

/* Upload card */
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

/* Cards */
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

/* Input */
div[data-testid="stTextInput"] input {
    background:#080c1ae6 !important;
    border:1px solid #29345d !important;
    border-radius:14px !important;
    color:white !important;
    height:55px !important;
}

/* Buttons */
.stButton > button {
    background:linear-gradient(135deg,#4f46e5,#7c3aed) !important;
    color:white !important;
    border:0 !important;
    border-radius:12px !important;
    font-weight:700 !important;
    min-height:45px !important;
    box-shadow:0 8px 25px #4f46e540;
}

/* Documents */
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


# ---------- SIDEBAR ----------
with st.sidebar:

    st.markdown(
        '<div class="logo"><div class="owl">🦉</div>NightOwl</div>'
        '<div class="sub">EVIDENCE INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("KNOWLEDGE VAULT")

    files = sorted(os.listdir(UPLOAD_DIR))

    if files:

        for file in files:
            size = os.path.getsize(
                os.path.join(UPLOAD_DIR, file)
            ) / 1024

            st.markdown(
                f"""
                <div class="doc">
                    📄 <b>{file}</b>
                    <small>{size:.1f} KB · Ready</small>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.caption("No material uploaded yet.")

    st.divider()

    st.caption("🛡 Evidence-first mode")
    st.caption("Answers will be grounded in your material.")


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

    for file in uploads:

        path = os.path.join(UPLOAD_DIR, file.name)

        with open(path, "wb") as out:
            out.write(file.getbuffer())

    st.success(f"✓ {len(uploads)} file(s) added")

    files = sorted(os.listdir(UPLOAD_DIR))


# ---------- ASK ----------
st.markdown("### 💬 Ask your course")

question = st.text_input(
    "Question",
    placeholder="What is the difference between BFS and DFS?",
    label_visibility="collapsed"
)

ask, _ = st.columns([1, 5])

with ask:

    clicked = st.button(
        "✦  Ask NightOwl",
        use_container_width=True
    )


if clicked:

    if not question.strip():

        st.warning("Enter a question first.")

    elif not files:

        st.warning("Upload your course material first.")

    else:

        st.markdown(
            """
            <div class="card">
                <div class="small">NIGHTOWL RESPONSE</div>
                <h3>Evidence retrieval is coming next.</h3>
                <p style="color:#94a3b8">
                    Your material is safely stored.
                    NightOwl will soon extract the content,
                    find relevant evidence and answer from it.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------- STATS ----------
st.write("")

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
        🦉 NightOwl · Evidence over assumptions
    </div>
    """,
    unsafe_allow_html=True
)