import streamlit as st
import requests
import ast

st.set_page_config(
    page_title="Devarsh Gandhi | Digital Product Owner & AI Architect",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# HIGH-CONTRAST STREAMLINED CSS (SIMPLE & CLEAN)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0B0F19 !important;
        color: #F3F4F6 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    p, span, div, label, li {
        color: #E5E7EB;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 800 !important;
    }

    .brand-title {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 50%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .section-title {
        font-size: 1.4rem !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        margin-top: 2rem !important;
        margin-bottom: 0.8rem !important;
        border-bottom: 1px solid #1F2937;
        padding-bottom: 0.4rem;
    }

    .hero-box {
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.9), rgba(11, 15, 25, 0.95));
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 16px;
        padding: 2.2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    .card {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 12px;
        padding: 1.3rem;
        margin-bottom: 1rem;
        transition: border-color 0.2s ease;
    }
    .card:hover {
        border-color: #06b6d4;
    }

    .badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 0.25rem 0.6rem;
        border-radius: 9999px;
        background: rgba(6, 182, 212, 0.12);
        color: #22d3ee;
        border: 1px solid rgba(6, 182, 212, 0.3);
        display: inline-block;
        margin-right: 0.3rem;
        margin-bottom: 0.4rem;
    }
    .badge-red {
        background: rgba(239, 68, 68, 0.12);
        color: #f87171;
        border-color: rgba(239, 68, 68, 0.3);
    }

    .metric-box {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .metric-val {
        font-size: 1.5rem;
        font-weight: 800;
        color: #22d3ee;
        font-family: 'JetBrains Mono', monospace;
    }
    .metric-lbl {
        font-size: 0.78rem;
        color: #9CA3AF;
        margin-top: 0.2rem;
    }

    .stButton > button, [data-testid="stLinkButton"] > a {
        background: linear-gradient(135deg, #06b6d4, #3b82f6) !important;
        color: #030712 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        padding: 0.55rem 1.2rem !important;
    }
    .stButton > button:hover, [data-testid="stLinkButton"] > a:hover {
        opacity: 0.9 !important;
        color: #030712 !important;
    }

    div[role="radiogroup"] label {
        background-color: #111827 !important;
        border: 1px solid #1F2937 !important;
        border-radius: 8px !important;
        padding: 0.4rem 0.8rem !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    div[role="radiogroup"] label[data-checked="true"] {
        border-color: #06b6d4 !important;
        background: rgba(6, 182, 212, 0.1) !important;
    }

    div[data-testid="stExpander"] {
        background-color: #111827 !important;
        border: 1px solid #1F2937 !important;
        border-radius: 10px !important;
    }
    div[data-testid="stExpander"] summary p {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SESSION STATE
# -----------------------------------------------------------------------------
if "repos" not in st.session_state:
    st.session_state.repos = [
        {
            "name": "ScopeForge-AI-Agent",
            "tag": "Python · Anthropic Claude",
            "desc": "AI agent automating BA workflows (BRDs, Gherkin stories, Jira/ADO exports) with enterprise security hardening (SSRF rejection, zip bomb guards, exact dependency pinning).",
            "url": "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/"
        },
        {
            "name": "Speak-English-Family-App",
            "tag": "Next.js · Prisma · Postgres",
            "desc": "Daily practice web app built for Gujarati speakers (Viresh & Nita) featuring 4 daily tasks, speech scoring, spaced repetition, and unit unlocking.",
            "url": "https://english-practice-app.vercel.app"
        },
        {
            "name": "Commercial-Planning-Ecosystem",
            "tag": "SQL · Power BI",
            "desc": "Demand & inventory planning workflows, RTM traceability matrices, and executive KPI value realization dashboards.",
            "url": "https://github.com/devarsh22"
        }
    ]

if "websites" not in st.session_state:
    st.session_state.websites = [
        {
            "name": "ScopeForge AI Web Agent",
            "badge": "FLAGSHIP PRODUCT",
            "desc": "Production-grade Streamlit agent turning raw transcripts & specs into structured requirements and Jira/ADO backlogs.",
            "url": "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/"
        },
        {
            "name": "Speak English (Parent Practice App)",
            "badge": "FAMILY IMPACT PROJECT",
            "desc": "Duolingo-style daily practice app built to help parents gain travel English confidence with speech recognition and spaced repetition.",
            "url": "https://english-practice-app.vercel.app"
        },
        {
            "name": "LinkedIn Executive Profile",
            "badge": "NETWORK",
            "desc": "Connect with Devarsh Gandhi — PMP® Certified Digital Product Owner & Senior Business Systems Analyst.",
            "url": "https://linkedin.com/in/devarsh-gandhi-pmp-2b1083144"
        }
    ]

# -----------------------------------------------------------------------------
# TOP HEADER & PROFILE SELECTOR
# -----------------------------------------------------------------------------
h_c1, h_c2, h_c3 = st.columns([1.5, 2.5, 1])
with h_c1:
    st.markdown('<div class="brand-title">DEVARSH GANDHI</div>', unsafe_allow_html=True)
    st.caption("Digital Product Owner · PMP® · AI Architect")
with h_c2:
    active_profile = st.radio(
        "Select Role Profile",
        ["Digital Product Owner", "Senior Business Analyst", "Program Delivery (PMP®)"],
        horizontal=True,
        label_visibility="collapsed"
    )
with h_c3:
    st.link_button("Launch ScopeForge ↗", "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/", use_container_width=True)

# -----------------------------------------------------------------------------
# HERO BANNER
# -----------------------------------------------------------------------------
profile_summaries = {
    "Digital Product Owner": (
        "PMP®-certified Digital Product Owner & Senior Business Systems Analyst driving enterprise technology products, "
        "data-intensive ecosystems, and full-lifecycle Agile delivery. Passionate builder of production AI agents (ScopeForge) "
        "and consumer web applications (Speak English family app). Lifelong cricket player bringing teamwork, resilience, "
        "and strategic focus to cross-functional product execution."
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
<div class="hero-box">
    <span class="badge">● AVAILABLE FOR DIGITAL PRODUCT OWNER & PM ROLES</span>
    <span class="badge">QUINCY, MA</span>
    <span class="badge">LIFELONG CRICKETER</span>
    <h2 style="margin-top:0.75rem; margin-bottom:0.5rem; font-size:2rem;">Engineering Scalable Products & AI Workflows</h2>
    <p style="font-size:1.05rem; line-height:1.6; color:#D1D5DB; margin:0;">{profile_summaries[active_profile]}</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# KEY METRICS
# -----------------------------------------------------------------------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="metric-box"><div class="metric-val">3 / 3</div><div class="metric-lbl">On-Time Go-Lives</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-box"><div class="metric-val">0%</div><div class="metric-lbl">Scope Creep</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-box"><div class="metric-val">+20%</div><div class="metric-lbl">Workflow ROI</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric-box"><div class="metric-val">500+</div><div class="metric-lbl">Defects Triaged</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FEATURED PRODUCT: SCOPEFORGE & SECURITY HARDENING
# -----------------------------------------------------------------------------
st.markdown('<div class="section-title">Flagship AI Agent: ScopeForge & Security Hardening</div>', unsafe_allow_html=True)
sf_c1, sf_c2 = st.columns([1.3, 1], gap="large")

with sf_c1:
    st.markdown("""
    <div class="card">
        <span class="badge">PYTHON</span>
        <span class="badge">STREAMLIT</span>
        <span class="badge">ANTHROPIC CLAUDE API</span>
        <h3 style="margin:0.5rem 0;">ScopeForge Business Analysis Engine</h3>
        <p style="font-size:0.95rem; line-height:1.6; color:#D1D5DB;">
            A production-grade AI web agent (~3,200 lines) that transforms messy meeting transcripts and draft requirements into structured BRDs, 
            MoSCoW priorities, Gherkin acceptance criteria, Visio-ready process maps, and Jira/Azure DevOps CSV exports.
        </p>
        <hr style="border-color:#1F2937; margin:1rem 0;">
        <h4 style="font-size:1rem; color:#22d3ee; margin-bottom:0.4rem;">Enterprise Security Hardening</h4>
        <p style="font-size:0.9rem; line-height:1.5; color:#D1D5DB;">
            Proactively closed three critical attack vectors:
            <br>• <strong>SSRF Defense:</strong> Rejects non-public IP addresses and re-checks after every redirect to prevent internal network scanning.
            <br>• <strong>Zip Bomb Protection:</strong> Limits unpacking expansion on Office files (Word/Excel/PowerPoint) to prevent memory exhaustion.
            <br>• <strong>Exact Dependency Pinning:</strong> Replaced floating package installs with verified exact library versions to prevent supply-chain hijacking.
        </p>
    </div>
    """, unsafe_allow_html=True)

with sf_c2:
    st.markdown("""
    <div class="card">
        <span class="badge badge-red">LIVE DEPLOYMENT</span>
        <h3 style="margin:0.5rem 0;">ScopeForge Live App</h3>
        <p style="font-size:0.9rem; color:#9CA3AF; margin-bottom:1rem;">
            Test the live agent engine and explore automated BA workflows.
        </p>
        <code style="display:block; padding:0.6rem; background:#0B0F19; border-radius:8px; color:#22d3ee; font-size:0.78rem; word-break:break-all; margin-bottom:1rem;">
            https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/
        </code>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Launch ScopeForge Live ↗", "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/", use_container_width=True)

# -----------------------------------------------------------------------------
# FEATURED WEB APP: SPEAK ENGLISH (FAMILY APP)
# -----------------------------------------------------------------------------
st.markdown('<div class="section-title">Family Impact Project: Speak English App</div>', unsafe_allow_html=True)
se_c1, se_c2 = st.columns([1.3, 1], gap="large")

with se_c1:
    st.markdown("""
    <div class="card">
        <span class="badge">NEXT.JS</span>
        <span class="badge">PRISMA</span>
        <span class="badge">POSTGRES</span>
        <span class="badge">VERCEL</span>
        <h3 style="margin:0.5rem 0;">Speak English — Private Daily Practice App</h3>
        <p style="font-size:0.95rem; line-height:1.6; color:#D1D5DB;">
            Built specifically for Gujarati-speaking parents (Viresh and Nita) to gain confidence speaking and understanding English while traveling. 
            Features a playful Duolingo-style interface with 4 daily tasks (vocab drill, listening comprehension clip, speaking exercise with browser speech recognition, 
            and travel-scenario dialogue). Organized into 7 progressive units (Basics through Emergencies) with spaced repetition and an Ask Anything Gujarati translation helper.
        </p>
    </div>
    """, unsafe_allow_html=True)

with se_c2:
    st.markdown("""
    <div class="card">
        <span class="badge badge-red">LIVE VERCEL APP</span>
        <h3 style="margin:0.5rem 0;">Speak English Live</h3>
        <p style="font-size:0.9rem; color:#9CA3AF; margin-bottom:1rem;">
            Explore the live family practice application deployed on Vercel.
        </p>
        <code style="display:block; padding:0.6rem; background:#0B0F19; border-radius:8px; color:#22d3ee; font-size:0.78rem; word-break:break-all; margin-bottom:1rem;">
            https://english-practice-app.vercel.app
        </code>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Visit Speak English App ↗", "https://english-practice-app.vercel.app", use_container_width=True)

# -----------------------------------------------------------------------------
# CASE STUDIES / EXPERIENCE
# -----------------------------------------------------------------------------
st.markdown('<div class="section-title">Enterprise Professional Experience</div>', unsafe_allow_html=True)

cases = [
    {
        "org": "Spruce Technology · Multi-Agency Government IT Modernization",
        "role": "Digital Product Owner / Senior Business Analyst (Apr 2024 – Present)",
        "badge": "3 Releases · 0 Scope Creep",
        "details": "Owned product backlog prioritization and Agile/SAFe ceremonies for an 8-person engineering & QA team. Translated 120+ complex requirements into acceptance-ready user stories with 100% RTM coverage, accelerated vendor API integration by 3 weeks, and delivered a 20% workflow efficiency gain."
    },
    {
        "org": "Systech Corporation · Enterprise Product Implementation",
        "role": "Business Analyst (Feb 2023 – Mar 2024)",
        "badge": "500+ Defects Cleared",
        "details": "Drove platform stability and release readiness by triaging and clearing a 500+ defect UAT backlog in under 4 months, conducting as-is vs. to-be gap analyses, and authoring 8 persona-based end-user guides."
    },
    {
        "org": "COLSH Consultants LLC · Cross-Unit Advisory & Planning",
        "role": "Business Analyst (Mar 2021 – Jan 2023)",
        "badge": "First-Pass Sign-Off",
        "details": "Enabled data-driven capacity and resource planning via workforce analytics reporting and produced 10+ BPMN/UML process models across 3 parallel workstreams with zero revision loops."
    }
]

for item in cases:
    with st.expander(f"{item['org']} — [{item['badge']}]"):
        st.caption(item["role"])
        st.markdown(f"<p style='color:#E5E7EB; font-size:0.95rem; line-height:1.6;'>{item['details']}</p>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# GITHUB REPOSITORIES & WEB APPS
# -----------------------------------------------------------------------------
st.markdown('<div class="section-title">GitHub Repositories & Web Properties</div>', unsafe_allow_html=True)
r_cols = st.columns(3)
for idx, repo in enumerate(st.session_state.repos):
    with r_cols[idx % 3]:
        st.markdown(f"""
        <div class="card">
            <span class="badge">{repo['tag']}</span>
            <h4 style="margin:0.4rem 0;">{repo['name']}</h4>
            <p style="font-size:0.85rem; color:#9CA3AF; min-height:65px;">{repo['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Repository ↗", repo["url"], use_container_width=True)

st.markdown('<div class="section-title" style="margin-top:2rem;">Digital Presence & Websites</div>', unsafe_allow_html=True)
w_cols = st.columns(2)
for idx, site in enumerate(st.session_state.websites):
    with w_cols[idx % 2]:
        st.markdown(f"""
        <div class="card">
            <span class="badge">{site['badge']}</span>
            <h4 style="margin:0.4rem 0; margin-top:0.4rem;">{site['name']}</h4>
            <p style="font-size:0.9rem; color:#D1D5DB;">{site['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Visit {site['name']} ↗", site["url"], use_container_width=True)
