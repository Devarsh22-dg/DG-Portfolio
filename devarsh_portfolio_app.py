import streamlit as st
import streamlit.components.v1 as components
import requests
import json

st.set_page_config(
    page_title="Devarsh Gandhi | Digital Product Owner & AI Architect",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #030712;
        color: #F3F4F6;
    }

    .stApp {
        background: radial-gradient(circle at 15% 15%, rgba(6, 182, 212, 0.08) 0%, transparent 40%),
                    radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.08) 0%, transparent 40%),
                    #030712;
    }

    .glass-card {
        background: rgba(17, 24, 39, 0.72);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .glass-card:hover {
        border-color: rgba(6, 182, 212, 0.45);
        transform: translateY(-2px);
    }

    .glass-card-glow {
        background: rgba(17, 24, 39, 0.85);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(6, 182, 212, 0.35);
        box-shadow: 0 0 30px rgba(6, 182, 212, 0.12);
        border-radius: 20px;
        padding: 1.75rem;
        margin-bottom: 1.25rem;
    }

    .gradient-text {
        background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 50%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    .mono-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        padding: 0.25rem 0.65rem;
        border-radius: 9999px;
        background: rgba(6, 182, 212, 0.12);
        color: #22d3ee;
        border: 1px solid rgba(6, 182, 212, 0.3);
        display: inline-block;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
    }

    .metric-box {
        background: rgba(11, 15, 25, 0.85);
        border: 1px solid rgba(55, 65, 81, 0.6);
        border-radius: 14px;
        padding: 1rem;
        text-align: center;
    }
    .metric-val {
        font-size: 1.65rem;
        font-weight: 800;
        color: #06b6d4;
        font-family: 'JetBrains Mono', monospace;
    }
    .metric-lbl {
        font-size: 0.78rem;
        color: #9CA3AF;
        margin-top: 0.2rem;
    }

    section[data-testid="stSidebar"] {
        background-color: #0B0F19;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    .stButton > button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)

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
            "badge": "Live Streamlit App",
            "desc": "Production AI workflow engine turning raw transcripts & specs into BRDs, gap analyses, and Jira/ADO backlogs.",
            "url": "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/"
        },
        {
            "name": "LinkedIn Executive Profile",
            "badge": "Professional Network",
            "desc": "Connect with Devarsh Gandhi — PMP® Certified Digital Product Owner & Senior Business Systems Analyst.",
            "url": "https://linkedin.com/in/devarsh-gandhi-pmp-2b1083144"
        }
    ]

if "interests" not in st.session_state:
    st.session_state.interests = [
        {"title": "Commercial & Demand Planning", "detail": "Inventory optimization, forecasting workflows, and ERP/API ecosystem reliability."},
        {"title": "AI Agent Productization", "detail": "Building LLM-powered workflows (Claude/Streamlit) that eliminate manual analyst toil."},
        {"title": "Lean Six Sigma & Process ROI", "detail": "Data-driven process audits delivering measurable cycle-time and efficiency gains."},
        {"title": "Agile Product Strategy", "detail": "Roadmapping, backlog prioritization, and cross-functional alignment without direct authority."}
    ]

with st.sidebar:
    st.markdown("""
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:1rem;">
            <div style="width:40px; height:40px; border-radius:12px; background:linear-gradient(135deg,#06b6d4,#3b82f6,#8b5cf6); display:flex; align-items:center; justify-content:center; font-weight:800; color:white;">DG</div>
            <div>
                <div style="font-weight:800; font-size:1rem; letter-spacing:0.05em;">DEVARSH.OS</div>
                <div style="font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:#22d3ee;">v3.4 · Streamlit Edition</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    nav_section = st.radio(
        "Navigate OS",
        [
            "🚀 Command Stage (Home)",
            "🤖 ScopeForge AI Agent",
            "📊 Enterprise Case Studies",
            "💻 GitHub & Repositories",
            "🌐 Websites & Focus Areas",
            "🛠️ Portfolio Studio (Customize)"
        ]
    )

    st.divider()
    st.markdown("**📍 Location:** Quincy, MA (Greater Boston)")
    st.markdown("**🎓 Credentials:** PMP® · Lean Six Sigma GB · MS Marketing")
    st.markdown("**📧 Contact:** devarsh.22.dg@gmail.com")
    st.link_button("Launch ScopeForge Live ↗", "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/", use_container_width=True)

def render_3d_torus():
    torus_html = """
    <div style="background: rgba(17,24,39,0.85); border: 1px solid rgba(6,182,212,0.35); border-radius: 20px; padding: 14px; text-align: center; box-shadow: 0 0 25px rgba(6,182,212,0.15); font-family: 'JetBrains Mono', monospace;">
        <div style="position: relative; width: 320px; height: 320px; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
            <svg viewBox="0 0 320 320" style="position: absolute; inset: 0; width: 100%; height: 100%; animation: spinSlow 24s linear infinite;">
                <defs>
                    <path id="orbitPath" d="M 160, 160 m -132, 0 a 132,132 0 1,1 264,0 a 132,132 0 1,1 -264,0" />
                </defs>
                <text fill="#22d3ee" font-size="10.5" font-weight="700" letter-spacing="3.2">
                    <textPath href="#orbitPath" startOffset="0%">
                        DIGITAL PRODUCT OWNER • ZERO SCOPE CREEP • AI WORKFLOWS • DATA INTEGRITY •
                    </textPath>
                </text>
            </svg>
            <canvas id="donutCanvas" width="260" height="260" style="cursor: grab; z-index: 2;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px; color:#22d3ee; background:#030712; padding:6px 12px; border-radius:10px; border:1px solid rgba(6,182,212,0.25); margin-top:6px;">
            <span>3D TORUS SHADER · 60 FPS</span>
            <button onclick="cycleShader()" style="background:none; border:none; color:#38bdf8; text-decoration:underline; cursor:pointer; font-family:inherit; font-size:11px;">SWITCH SHADER</button>
        </div>
    </div>
    <style>
        @keyframes spinSlow { 100% { transform: rotate(360deg); } }
    </style>
    <script>
        const canvas = document.getElementById('donutCanvas');
        const ctx = canvas.getContext('2d');
        let A = 0, B = 0, shaderMode = 0;
        const colors = ['#06b6d4', '#3b82f6', '#8b5cf6', '#10b981'];
        function cycleShader() { shaderMode = (shaderMode + 1) % colors.length; }
        function render() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            const w = canvas.width, h = canvas.height;
            const z = [];
            A += 0.035; B += 0.018;
            const cA = Math.cos(A), sA = Math.sin(A), cB = Math.cos(B), sB = Math.sin(B);
            for (let j = 0; j < 6.28; j += 0.07) {
                const ct = Math.cos(j), st = Math.sin(j);
                for (let i = 0; i < 6.28; i += 0.025) {
                    const sp = Math.sin(i), cp = Math.cos(i);
                    const h2 = ct + 2;
                    const D = 1 / (sp * h2 * sA + st * cA + 5);
                    const t = sp * h2 * cA - st * sA;
                    const x = Math.floor(w / 2 + 24 * D * (cp * h2 * cB - t * sB));
                    const y = Math.floor(h / 2 + 24 * D * (cp * h2 * sB + t * cB));
                    const o = x + w * y;
                    const N = Math.floor(8 * ((st * sA - sp * ct * cA) * cB - sp * ct * sA - st * cA - cp * ct * sB));
                    if (h > y && y > 0 && x > 0 && w > x && D > (z[o] || 0)) {
                        z[o] = D;
                        ctx.fillStyle = colors[shaderMode];
                        ctx.globalAlpha = Math.max(0.15, N / 8);
                        ctx.fillRect(x, y, 2.2, 2.2);
                    }
                }
            }
            requestAnimationFrame(render);
        }
        render();
    </script>
    """
    components.html(torus_html, height=400)

if nav_section == "🚀 Command Stage (Home)":
    col1, col2 = st.columns([1.35, 1], gap="large")

    with col1:
        st.markdown('<span class="mono-badge">● AVAILABLE FOR DIGITAL PRODUCT OWNER & PM ROLES</span>', unsafe_allow_html=True)
        st.markdown("""<h1 style="font-size:3rem; line-height:1.15; margin-top:0.5rem;">Hi, I'm <span class="gradient-text">Devarsh Gandhi</span></h1>""", unsafe_allow_html=True)

        lens = st.radio(
            "Select Interactive Role Lens:",
            ["Digital Product Owner", "Senior Business Analyst", "Program Delivery (PMP®)"],
            horizontal=True
        )

        lens_copy = {
            "Digital Product Owner": "PMP®-certified Digital Product Owner & Senior Business Systems Analyst driving enterprise technology products, data-intensive ecosystems, and full-lifecycle Agile delivery. Proven track record owning product vision, roadmaps, and prioritized backlogs from concept through KPI value realization.",
            "Senior Business Analyst": "Senior Business Analyst specializing in structured discovery, end-to-end Requirements Traceability Matrices (RTM), BPMN/UML process modeling, and translating ambiguous enterprise workflows into acceptance-ready epics and user stories.",
            "Program Delivery (PMP®)": "PMP®-certified delivery leader with 5+ years managing multi-vendor, matrixed IT programs — delivering 3 consecutive enterprise platform releases on schedule and within budget with zero scope creep and zero missed go-live dates."
        }

        st.markdown(f'<div class="glass-card"><p style="font-size:1.05rem; line-height:1.65; color:#E5E7EB; margin:0;">{lens_copy[lens]}</p></div>', unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown('<div class="metric-box"><div class="metric-val">3/3</div><div class="metric-lbl">On-Time Releases</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric-box"><div class="metric-val">0%</div><div class="metric-lbl">Scope Creep</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric-box"><div class="metric-val">+20%</div><div class="metric-lbl">Workflow ROI</div></div>', unsafe_allow_html=True)
        with m4:
            st.markdown('<div class="metric-box"><div class="metric-val">500+</div><div class="metric-lbl">Defects Triaged</div></div>', unsafe_allow_html=True)

    with col2:
        render_3d_torus()

    st.divider()
    st.subheader("Core Competency Matrix")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color:#22d3ee; margin-top:0;">Product Ownership</h4>
            <p style="font-size:0.88rem; color:#D1D5DB;">Product Vision & Roadmap · Backlog Prioritization · KPIs & Value Realization · Technical Tradeoffs · Release Readiness</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color:#60a5fa; margin-top:0;">Agile & Cross-Functional Leadership</h4>
            <p style="font-size:0.88rem; color:#D1D5DB;">Scrum / SAFe / Kanban · Epics & User Stories · Influencing Without Authority · Multi-Vendor & Architecture Alignment</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color:#a78bfa; margin-top:0;">Data, Systems & Analytics</h4>
            <p style="font-size:0.88rem; color:#D1D5DB;">Data Integrity & Governance · ERP / REST API Integrations · SQL · Power BI · Python · Azure DevOps & Jira</p>
        </div>
        """, unsafe_allow_html=True)

elif nav_section == "🤖 ScopeForge AI Agent":
    st.markdown('<span class="mono-badge">FLAGSHIP AI PRODUCT · LIVE DEPLOYMENT</span>', unsafe_allow_html=True)
    st.markdown('<h2>ScopeForge AI — Business Analysis & Product Workflow Engine</h2>', unsafe_allow_html=True)

    col_a, col_b = st.columns([1.4, 1], gap="large")
    with col_a:
        st.markdown("""
        <div class="glass-card-glow">
            <p style="font-size:1rem; line-height:1.65;">
                A BA's day is reading messy source material — meeting transcripts, draft requirements, stakeholder docs — and turning it into structured deliverables. 
                <strong>ScopeForge</strong> keeps that entire workflow in one place, powered by the <strong>Anthropic Claude API</strong> and <strong>Streamlit</strong> (~3,200 lines of Python), with full export to Word, Excel, Visio Data Visualizer, and Jira/Azure DevOps CSV.
            </p>
            <div style="margin-top:1rem;">
                <span class="mono-badge">Python</span>
                <span class="mono-badge">Streamlit</span>
                <span class="mono-badge">Anthropic Claude API</span>
                <span class="mono-badge">Zero-Persistence Privacy</span>
                <span class="mono-badge">Jira / ADO CSV Export</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Core Product Modules")
        mod1, mod2 = st.columns(2)
        with mod1:
            st.markdown("""
            <div class="glass-card">
                <h5 style="color:#22d3ee; margin:0 0 0.4rem 0;">1. Project & Multimodal Document Hub</h5>
                <p style="font-size:0.85rem; color:#9CA3AF; margin:0;">Ingests Word, PDF, PPTX, Excel, CSV, or URLs. Extracts tables, comments, strikethroughs, and uses vision AI to parse embedded UI mockups.</p>
            </div>
            <div class="glass-card">
                <h5 style="color:#60a5fa; margin:0 0 0.4rem 0;">3. Elicitation & Gap Detector</h5>
                <p style="font-size:0.85rem; color:#9CA3AF; margin:0;">Flags ambiguities, missing NFRs, stakeholder conflicts, and scope risks. Generates workshop agendas and MoSCoW prioritization.</p>
            </div>
            """, unsafe_allow_html=True)
        with mod2:
            st.markdown("""
            <div class="glass-card">
                <h5 style="color:#a78bfa; margin:0 0 0.4rem 0;">2. Meeting Intelligence</h5>
                <p style="font-size:0.85rem; color:#9CA3AF; margin:0;">Converts transcripts into executive summaries, decisions, and verified action items with strict anti-hallucination owner grounding.</p>
            </div>
            <div class="glass-card">
                <h5 style="color:#34d399; margin:0 0 0.4rem 0;">4. Agile Backlog & Traceability Matrix</h5>
                <p style="font-size:0.85rem; color:#9CA3AF; margin:0;">Generates BRDs, FRDs, Gherkin acceptance criteria, fuzzy-matched Requirement → Story → Test Case RTMs, and change impact analyses.</p>
            </div>
            """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="glass-card">
            <h4 style="margin-top:0;">Live Application Endpoint</h4>
            <code style="display:block; padding:0.75rem; background:#030712; border-radius:10px; color:#22d3ee; word-break:break-all; margin-bottom:1rem;">
                https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/
            </code>
            <p style="font-size:0.85rem; color:#9CA3AF;">
                <strong>Security & Architecture:</strong> Deliberately architected without a persistent backend database — all client artifacts stay isolated in encrypted user session state. Includes embedded <strong>ScopeBot</strong> contextual assistant on every tab.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("🚀 Open ScopeForge Live App", "https://synergyai-rq3uhz8sth6hvtnzzruhur.streamlit.app/", use_container_width=True)

elif nav_section == "📊 Enterprise Case Studies":
    st.markdown('<span class="mono-badge">PROVEN DELIVERY & VALUE REALIZATION</span>', unsafe_allow_html=True)
    st.markdown('<h2>Enterprise Case Studies</h2>', unsafe_allow_html=True)

    cases = [
        {
            "org": "Spruce Technology · Multi-Agency Government IT Modernization",
            "role": "Digital Product Owner / Senior Business Analyst (Apr 2024 – Present)",
            "badge": "3 Releases · 0 Scope Creep",
            "problem": "Multi-agency government modernization program suffered from fragmented requirements, manual workflow bottlenecks, and a 6-week rework cycle across 8 engineers, QA leads, and external vendors.",
            "action": "Owned product backlog prioritization and Agile/SAFe ceremonies; established a standardized discovery-to-delivery framework; translated 120+ complex requirements into acceptance-ready user stories with 100% RTM coverage.",
            "outcome": "Delivered 3 successive platform releases on time and on budget with zero missed go-live dates, cut sprint milestone slippage by 15%, accelerated vendor API integration by 3 weeks, and achieved a 20% workflow efficiency gain."
        },
        {
            "org": "Systech Corporation · Enterprise Product Implementation",
            "role": "Business Analyst (Feb 2023 – Mar 2024)",
            "badge": "500+ Defects Resolved",
            "problem": "Critical enterprise product launch was threatened by a backlog of 500+ UAT defects and stakeholder-to-engineering ambiguity.",
            "action": "Triaged and prioritized defects by business and user impact across QA, engineering, and client leaders; conducted as-is vs. to-be gap analyses and authored 8 persona-based user guides.",
            "outcome": "Cleared the entire 500+ defect UAT backlog in under 4 months, secured an on-time product launch, and reduced post-launch support volume."
        },
        {
            "org": "COLSH Consultants LLC · Cross-Unit Advisory & Planning",
            "role": "Business Analyst (Mar 2021 – Jan 2023)",
            "badge": "First-Pass Sign-Off",
            "problem": "Four parallel business units and third-party vendors lacked unified process visibility and data-driven capacity planning.",
            "action": "Built workforce analytics reports for headcount/capacity decisions and authored 10+ BPMN/UML process models across 3 parallel workstreams.",
            "outcome": "Achieved first-pass stakeholder sign-off with zero revision loops and shortened cross-vendor integration decision cycles."
        }
    ]

    for c in cases:
        with st.expander(f"{c['org']}  —  [{c['badge']}]", expanded=True):
            st.caption(c["role"])
            col1, col2, col3 = st.columns(3)
            col1.markdown(f"**Problem / Context**\n\n{c['problem']}")
            col2.markdown(f"**Product & BA Execution**\n\n{c['action']}")
            col3.markdown(f"**Measurable Outcome**\n\n{c['outcome']}")

elif nav_section == "💻 GitHub & Repositories":
    st.markdown('<span class="mono-badge">OPEN SOURCE & TECHNICAL TOOLING</span>', unsafe_allow_html=True)
    st.markdown('<h2>GitHub Repositories</h2>', unsafe_allow_html=True)

    col_u1, col_u2 = st.columns([2, 1])
    with col_u1:
        gh_user = st.text_input("GitHub Username (Live API Sync)", value="devarsh22")
    with col_u2:
        st.write("")
        st.write("")
        if st.button("🔄 Sync Live GitHub Repos", use_container_width=True):
            try:
                resp = requests.get(f"https://api.github.com/users/{gh_user}/repos?sort=updated&per_page=6", timeout=5)
                if resp.status_code == 200:
                    data = resp.json()
                    if data:
                        st.session_state.repos = [
                            {
                                "name": r["name"],
                                "tag": r.get("language") or "Repository",
                                "desc": r.get("description") or "Enterprise & product engineering repository.",
                                "url": r["html_url"]
                            }
                            for r in data
                        ]
                        st.success(f"Synced {len(data)} live repositories for @{gh_user}!")
                    else:
                        st.info("No public repositories found; showing featured repositories.")
                else:
                    st.warning("GitHub API rate limit or user not found — displaying featured repositories.")
            except Exception as e:
                st.warning(f"Offline mode: displaying featured repositories ({e}).")

    cols = st.columns(3)
    for idx, repo in enumerate(st.session_state.repos):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="glass-card">
                <span class="mono-badge">{repo['tag']}</span>
                <h4 style="margin:0.5rem 0;">{repo['name']}</h4>
                <p style="font-size:0.85rem; color:#9CA3AF; min-height:60px;">{repo['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("View Repository ↗", repo["url"], use_container_width=True)

elif nav_section == "🌐 Websites & Focus Areas":
    st.markdown('<span class="mono-badge">DIGITAL PRESENCE & DOMAIN INTERESTS</span>', unsafe_allow_html=True)
    st.markdown('<h2>Websites & Live Apps</h2>', unsafe_allow_html=True)

    wcols = st.columns(2)
    for idx, site in enumerate(st.session_state.websites):
        with wcols[idx % 2]:
            st.markdown(f"""
            <div class="glass-card">
                <span class="mono-badge">{site['badge']}</span>
                <h4 style="margin:0.5rem 0;">{site['name']}</h4>
                <p style="font-size:0.88rem; color:#D1D5DB;">{site['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Visit {site['name']} ↗", site["url"], use_container_width=True)

    st.divider()
    st.markdown('<h2>Interests & Focus Areas</h2>', unsafe_allow_html=True)
    icols = st.columns(2)
    for idx, item in enumerate(st.session_state.interests):
        with icols[idx % 2]:
            st.markdown(f"""
            <div class="glass-card">
                <h4 style="color:#22d3ee; margin:0 0 0.4rem 0;">{item['title']}</h4>
                <p style="font-size:0.88rem; color:#9CA3AF; margin:0;">{item['detail']}</p>
            </div>
            """, unsafe_allow_html=True)

elif nav_section == "🛠️ Portfolio Studio (Customize)":
    st.markdown('<span class="mono-badge">LIVE STUDIO · NO-CODE CUSTOMIZER</span>', unsafe_allow_html=True)
    st.markdown('<h2>Portfolio Studio</h2>', unsafe_allow_html=True)
    st.write("Add new GitHub repositories, live web apps, or focus areas directly into your Streamlit session.")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        with st.form("add_repo_form"):
            st.subheader("➕ Add Repository")
            r_name = st.text_input("Repository Name", placeholder="e.g., Demand-Forecasting-Engine")
            r_tag = st.text_input("Tech Stack Tag", placeholder="e.g., Python · SQL")
            r_desc = st.text_area("Description", placeholder="What problem does this repo solve?")
            r_url = st.text_input("GitHub URL", value="https://github.com/devarsh22")
            if st.form_submit_button("Add to Portfolio"):
                if r_name:
                    st.session_state.repos.append({"name": r_name, "tag": r_tag, "desc": r_desc, "url": r_url})
                    st.success(f"Added repository '{r_name}'!")

    with col_s2:
        with st.form("add_web_form"):
            st.subheader("➕ Add Website / Live App")
            w_name = st.text_input("App / Website Name", placeholder="e.g., Power BI Executive Dashboard")
            w_badge = st.text
