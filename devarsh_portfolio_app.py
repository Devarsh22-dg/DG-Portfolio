import streamlit as st
import requests
import ast

st.set_page_config(
    page_title="DEVARSH | Digital Product Owner & AI Architect",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# NETFLIX-INSPIRED HIGH-CONTRAST CSS & TYPOGRAPHY
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700;800&display=swap');

    /* Global High-Contrast Dark Background & Crisp White Text */
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #141414 !important;
        color: #FFFFFF !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Force all Streamlit markdown, text, labels, and headers to high-contrast white/light gray */
    p, span, div, label, li {
        color: #F3F4F6;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 800 !important;
    }

    /* Netflix Wordmark Logo */
    .netflix-logo {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 2.6rem !important;
        letter-spacing: 0.08em !important;
        color: #E50914 !important;
        line-height: 1 !important;
        text-shadow: 0 2px 10px rgba(229, 9, 20, 0.35);
    }

    /* Row Section Headings (Netflix Style) */
    .row-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 1.45rem !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        margin-top: 1.8rem !important;
        margin-bottom: 0.85rem !important;
        letter-spacing: -0.01em;
    }

    /* Featured Billboard Hero Banner */
    .billboard {
        background: linear-gradient(90deg, #0B0B0B 0%, rgba(20, 20, 20, 0.94) 58%, rgba(229, 9, 20, 0.16) 100%);
        border: 1px solid #2A2A2A;
        border-left: 6px solid #E50914;
        border-radius: 12px;
        padding: 2.5rem 2.25rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.75);
    }
    .billboard-badge {
        display: inline-block;
        background-color: #E50914;
        color: #FFFFFF !important;
        font-weight: 800;
        font-size: 0.75rem;
        letter-spacing: 0.12em;
        padding: 0.25rem 0.65rem;
        border-radius: 4px;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
    }
    .billboard-title {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 3.6rem !important;
        letter-spacing: 0.04em;
        color: #FFFFFF !important;
        line-height: 1.05 !important;
        margin: 0.2rem 0 0.6rem 0 !important;
    }
    .billboard-meta {
        font-size: 0.92rem;
        font-weight: 700;
        color: #46D369 !important; /* Netflix 99% Match Green */
        margin-bottom: 1rem;
    }
    .billboard-desc {
        font-size: 1.08rem !important;
        line-height: 1.65 !important;
        color: #E5E5E5 !important;
        max-width: 820px;
    }

    /* Netflix Content Cards */
    .nf-card {
        background-color: #1F1F1F;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 1.35rem;
        margin-bottom: 0.85rem;
        transition: transform 0.22s ease, border-color 0.22s ease, background-color 0.22s ease;
    }
    .nf-card:hover {
        transform: scale(1.02);
        border-color: #E50914;
        background-color: #262626;
    }
    .nf-tag {
        display: inline-block;
        background-color: #2E2E2E;
        color: #FFFFFF !important;
        border: 1px solid #4B5563;
        font-size: 0.74rem;
        font-weight: 700;
        padding: 0.2rem 0.55rem;
        border-radius: 4px;
        margin-right: 0.35rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
    }
    .nf-tag-red {
        background-color: #E50914 !important;
        border-color: #E50914 !important;
        color: #FFFFFF !important;
    }
    .nf-card-title {
        font-size: 1.18rem !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        margin: 0.35rem 0 0.5rem 0 !important;
    }
    .nf-card-text {
        font-size: 0.96rem !important;
        line-height: 1.55 !important;
        color: #D4D4D4 !important;
    }

    /* Top 10 / KPI Stat Cards */
    .top10-box {
        background-color: #181818;
        border: 1px solid #2F2F2F;
        border-radius: 8px;
        padding: 1.1rem;
        display: flex;
        align-items: center;
        gap: 0.9rem;
    }
    .top10-num {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 3.1rem !important;
        line-height: 0.95 !important;
        color: #E50914 !important;
    }
    .top10-stat {
        font-size: 1.25rem !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
    }
    .top10-sub {
        font-size: 0.82rem !important;
        color: #B3B3B3 !important;
    }

    /* Primary Netflix Red Buttons & Link Buttons */
    .stButton > button, [data-testid="stLinkButton"] > a {
        background-color: #E50914 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        padding: 0.55rem 1.2rem !important;
        transition: background-color 0.2s ease !important;
    }
    .stButton > button:hover, [data-testid="stLinkButton"] > a:hover {
        background-color: #B81D24 !important;
        color: #FFFFFF !important;
    }

    /* Radio Profile Switcher Styling */
    div[role="radiogroup"] label {
        background-color: #1F1F1F !important;
        border: 1px solid #383838 !important;
        border-radius: 6px !important;
        padding: 0.45rem 0.9rem !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    div[role="radiogroup"] label[data-checked="true"] {
        background-color: #E50914 !important;
        border-color: #E50914 !important;
    }

    /* Inputs & Expanders */
    .stTextInput input, .stTextArea textarea {
        background-color: #1F1F1F !important;
        color: #FFFFFF !important;
        border: 1px solid #404040 !important;
    }
    div[data-testid="stExpander"] {
        background-color: #1B1B1B !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
    }
    div[data-testid="stExpander"] summary p {
        color: #FFFFFF !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SESSION STATE DATA
# -----------------------------------------------------------------------------
if "repos" not in st.session_state:
    st.session_state.repos = [
        {
            "name": "ScopeForge-AI-Agent",
            "tag": "Python · Anthropic API",
            "desc": "Streamlit + Claude AI agent automating BA elicitation, BRDs, Gherkin acceptance criteria, and Jira/ADO CSV exports.",
            "url": "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/"
        },
        {
            "name": "Commercial-Planning-Ecosystem",
            "tag": "SQL · Power BI",
            "desc": "Demand & inventory planning workflows, RTM traceability matrices, and executive KPI value realization dashboards.",
            "url": "https://github.com/devarsh22"
        },
        {
            "name": "Agile-Backlog-Toolkit",
            "tag": "Jira · Azure DevOps",
            "desc": "Automated epics, MoSCoW prioritization frameworks, and sprint predictability tracking scripts.",
            "url": "https://github.com/devarsh22"
        }
    ]

if "websites" not in st.session_state:
    st.session_state.websites = [
        {
            "name": "ScopeForge AI Web Agent",
            "badge": "LIVE ORIGINAL APP",
            "desc": "Production AI workflow engine turning raw transcripts & specs into BRDs, gap analyses, and Jira/ADO backlogs.",
            "url": "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/"
        },
        {
            "name": "LinkedIn Executive Profile",
            "badge": "NETWORK",
            "desc": "Connect with Devarsh Gandhi — PMP® Certified Digital Product Owner & Senior Business Systems Analyst.",
            "url": "https://linkedin.com/in/devarsh-gandhi-pmp-2b1083144"
        }
    ]

# -----------------------------------------------------------------------------
# TOP NETFLIX NAVIGATION BAR
# -----------------------------------------------------------------------------
nav_c1, nav_c2, nav_c3 = st.columns([1.2, 2.5, 1.3])
with nav_c1:
    st.markdown('<div class="netflix-logo">DEVARSHFLIX</div>', unsafe_allow_html=True)
with nav_c2:
    active_profile = st.radio(
        "Who's Watching? (Select Role Profile)",
        ["Digital Product Owner", "Senior Business Analyst", "Program Delivery (PMP®)"],
        horizontal=True,
        label_visibility="collapsed"
    )
with nav_c3:
    st.link_button("▶ Launch ScopeForge AI", "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/", use_container_width=True)

# -----------------------------------------------------------------------------
# FEATURED BILLBOARD HERO (NETFLIX BANNER)
# -----------------------------------------------------------------------------
profile_summaries = {
    "Digital Product Owner": (
        "PMP®-certified Digital Product Owner & Senior Business Systems Analyst driving enterprise technology products, "
        "data-intensive ecosystems, and full-lifecycle Agile delivery. Proven track record owning product vision, "
        "roadmaps, and prioritized backlogs from concept through KPI value realization."
    ),
    "Senior Business Analyst": (
        "Senior Business Analyst specializing in structured discovery, end-to-end Requirements Traceability Matrices (RTM), "
        "BPMN/UML process modeling, and translating ambiguous enterprise workflows into acceptance-ready epics and user stories."
    ),
    "Program Delivery (PMP®)": (
        "PMP®-certified delivery leader with 5+ years managing multi-vendor, matrixed IT programs — delivering 3 consecutive "
        "enterprise platform releases on schedule and within budget with zero scope creep and zero missed go-live dates."
    )
}

st.markdown(f"""
<div class="billboard">
    <div class="billboard-badge">N SERIES · FEATURED CANDIDATE</div>
    <div class="billboard-title">DEVARSH GANDHI</div>
    <div class="billboard-meta">99% Match &nbsp;·&nbsp; 2026 &nbsp;·&nbsp; PMP® Certified &nbsp;·&nbsp; Lean Six Sigma Green Belt &nbsp;·&nbsp; Quincy, MA</div>
    <div class="billboard-desc">{profile_summaries[active_profile]}</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ROW 1: TOP 10 CAREER HIGHLIGHTS (METRICS)
# -----------------------------------------------------------------------------
st.markdown('<div class="row-title">Top Impact Metrics in Product & Enterprise Delivery</div>', unsafe_allow_html=True)
t1, t2, t3, t4 = st.columns(4)
with t1:
    st.markdown('<div class="top10-box"><div class="top10-num">1</div><div><div class="top10-stat">3 / 3 Releases</div><div class="top10-sub">100% On-Time Go-Lives</div></div></div>', unsafe_allow_html=True)
with t2:
    st.markdown('<div class="top10-box"><div class="top10-num">2</div><div><div class="top10-stat">0% Creep</div><div class="top10-sub">Zero Unplanned Scope</div></div></div>', unsafe_allow_html=True)
with t3:
    st.markdown('<div class="top10-box"><div class="top10-num">3</div><div><div class="top10-stat">+20% ROI</div><div class="top10-sub">Workflow Efficiency Gain</div></div></div>', unsafe_allow_html=True)
with t4:
    st.markdown('<div class="top10-box"><div class="top10-num">4</div><div><div class="top10-stat">500+ Bugs</div><div class="top10-sub">Cleared in Under 4 Mos</div></div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ROW 2: FEATURED ORIGINAL — SCOPEFORGE AI AGENT
# -----------------------------------------------------------------------------
st.markdown('<div class="row-title">Featured Original: ScopeForge AI Workflow Engine</div>', unsafe_allow_html=True)
sf_c1, sf_c2 = st.columns([1.45, 1], gap="large")

with sf_c1:
    st.markdown("""
    <div class="nf-card">
        <span class="nf-tag nf-tag-red">LIVE AI PRODUCT</span>
        <span class="nf-tag">PYTHON</span>
        <span class="nf-tag">STREAMLIT</span>
        <span class="nf-tag">ANTHROPIC CLAUDE API</span>
        <div class="nf-card-title">ScopeForge — End-to-End Business Analysis & Backlog Automation</div>
        <div class="nf-card-text">
            A BA's day is reading messy source material — meeting transcripts, draft requirements, stakeholder docs — and turning it into structured deliverables. 
            ScopeForge keeps that whole workflow in one place (~3,200 lines of Python), generating BRDs, FRDs, MoSCoW priorities, Gherkin acceptance criteria, 
            Visio Data Visualizer process maps, and Jira/Azure DevOps CSV exports with zero persistent client document storage.
        </div>
    </div>
    """, unsafe_allow_html=True)

    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.markdown("""
        <div class="nf-card">
            <div class="nf-card-title">Multimodal Doc Hub & Meeting Intel</div>
            <div class="nf-card-text">Parses Word, PDF, PPTX, Excel, CSV, and embedded UI screenshots via vision AI; converts transcripts into verified action items.</div>
        </div>
        """, unsafe_allow_html=True)
    with m_col2:
        st.markdown("""
        <div class="nf-card">
            <div class="nf-card-title">Gap Detector & Traceability Matrix</div>
            <div class="nf-card-text">Flags ambiguities, missing NFRs, and scope risks; builds fuzzy-matched Requirement → Story → Test Case RTMs.</div>
        </div>
        """, unsafe_allow_html=True)

with sf_c2:
    st.markdown("""
    <div class="nf-card">
        <span class="nf-tag nf-tag-red">STREAM NOW</span>
        <div class="nf-card-title">Launch Live Application</div>
        <div class="nf-card-text" style="margin-bottom:1rem;">
            <strong>Endpoint:</strong><br>
            <span style="color:#FFFFFF; font-weight:600; word-break:break-all;">https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/</span><br><br>
            Includes embedded <strong>ScopeBot</strong> contextual assistant on every screen and session-isolated privacy architecture.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("▶ Open ScopeForge Live App", "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/", use_container_width=True)

# -----------------------------------------------------------------------------
# ROW 3: CASE STUDIES (EPISODES)
# -----------------------------------------------------------------------------
st.markdown('<div class="row-title">Season 1: Enterprise Case Studies & Career Episodes</div>', unsafe_allow_html=True)

episodes = [
    {
        "ep": "EPISODE 1 · SPRUCE TECHNOLOGY (APR 2024 – PRESENT)",
        "title": "Digital Product Owner / Senior BA — Multi-Agency IT Modernization",
        "meta": "3 Releases Delivered · 100% RTM Coverage · -15% Sprint Slippage",
        "details": "Owned product backlog prioritization and Agile/SAFe ceremonies for an 8-person engineering & QA team. Translated 120+ complex requirements into acceptance-ready user stories, accelerated vendor API integration by 3 weeks, and delivered a 20% workflow efficiency gain."
    },
    {
        "ep": "EPISODE 2 · SYSTECH CORPORATION (FEB 2023 – MAR 2024)",
        "title": "Business Analyst — Enterprise Product Implementation & UAT",
        "meta": "500+ Defects Cleared · Under 4 Months · On-Time Launch",
        "details": "Drove platform stability and release readiness by triaging and clearing a 500+ defect UAT backlog in under 4 months, conducting as-is vs. to-be gap analyses, and authoring 8 persona-based end-user guides."
    },
    {
        "ep": "EPISODE 3 · COLSH CONSULTANTS LLC (MAR 2021 – JAN 2023)",
        "title": "Business Analyst — Cross-Unit Planning & Process Modeling",
        "meta": "10+ BPMN/UML Models · 4 Business Units · First-Pass Sign-Off",
        "details": "Enabled data-driven capacity and resource planning via workforce analytics reporting and produced 10+ BPMN/UML process models across 3 parallel workstreams with zero revision loops."
    }
]

for item in episodes:
    with st.expander(f"{item['ep']}  |  {item['title']}", expanded=True):
        st.markdown(f"<p style='color:#46D369; font-weight:700; margin-bottom:0.4rem;'>{item['meta']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#E5E5E5; font-size:1rem; line-height:1.6;'>{item['details']}</p>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ROW 4: GITHUB REPOSITORIES & CODEBASE
# -----------------------------------------------------------------------------
st.markdown('<div class="row-title">Trending Repositories & Technical Tooling</div>', unsafe_allow_html=True)
gh_c1, gh_c2 = st.columns([2.5, 1])
with gh_c1:
    gh_user = st.text_input("GitHub Username", value="devarsh22", label_visibility="collapsed")
with gh_c2:
    if st.button("🔄 Sync Live GitHub Repos", use_container_width=True):
        try:
            resp = requests.get(f"https://api.github.com/users/{gh_user}/repos?sort=updated&per_page=6", timeout=5)
            if resp.status_code == 200 and resp.json():
                st.session_state.repos = [
                    {
                        "name": r["name"],
                        "tag": r.get("language") or "Repository",
                        "desc": r.get("description") or "Enterprise & product engineering repository.",
                        "url": r["html_url"]
                    }
                    for r in resp.json()
                ]
                st.success(f"Synced repositories for @{gh_user}!")
            else:
                st.info("Showing featured repositories.")
        except Exception:
            st.info("Showing featured repositories.")

r_cols = st.columns(3)
for idx, repo in enumerate(st.session_state.repos):
    with r_cols[idx % 3]:
        st.markdown(f"""
        <div class="nf-card">
            <span class="nf-tag nf-tag-red">{repo['tag']}</span>
            <div class="nf-card-title">{repo['name']}</div>
            <div class="nf-card-text" style="min-height:68px;">{repo['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Code ↗", repo["url"], use_container_width=True)

# -----------------------------------------------------------------------------
# ROW 5: WEBSITES, FOCUS AREAS & CUSTOMIZER STUDIO
# -----------------------------------------------------------------------------
st.markdown('<div class="row-title">Websites, Interests & Studio Customizer</div>', unsafe_allow_html=True)
w_cols = st.columns(2)
for idx, site in enumerate(st.session_state.websites):
    with w_cols[idx % 2]:
        st.markdown(f"""
        <div class="nf-card">
            <span class="nf-tag nf-tag-red">{site['badge']}</span>
            <div class="nf-card-title">{site['name']}</div>
            <div class="nf-card-text">{site['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Open {site['name']} ↗", site["url"], use_container_width=True)

with st.expander("➕ Add Custom Repository or Live Website to This Page"):
    f_c1, f_c2 = st.columns(2)
    with f_c1:
        with st.form("nf_add_repo"):
            st.markdown("**Add GitHub Repository**")
            rn = st.text_input("Repo Name")
            rt = st.text_input("Tech Tag", value="Python")
            rd = st.text_input("Description")
            ru = st.text_input("URL", value="https://github.com/devarsh22")
            if st.form_submit_button("Add Repository"):
                if rn:
                    st.session_state.repos.append({"name": rn, "tag": rt, "desc": rd, "url": ru})
                    st.rerun()
    with f_c2:
        with st.form("nf_add_web"):
            st.markdown("**Add Website / App**")
            wn = st.text_input("Site Name")
            wb = st.text_input("Badge", value="LIVE APP")
            wd = st.text_input("Summary")
            wu = st.text_input("URL", value="https://")
            if st.form_submit_button("Add Website"):
                if wn and wu:
                    st.session_state.websites.append({"name": wn, "badge": wb, "desc": wd, "url": wu})
                    st.rerun()
