import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="AI Agent Memory Security Lab",
    page_icon="🔐",
    layout="wide"
)

# ----------------------------------------------------
# LOGIN
# ----------------------------------------------------

st.sidebar.title("Authentication")

role = st.sidebar.selectbox(
    "Login As",
    [
        "Admin",
        "Analyst"
    ]
)

if role == "Admin":
    API_KEY = "admin-key-123"
else:
    API_KEY = "analyst-key-456"

HEADERS = {
    "X-API-Key": API_KEY
}

st.title("🔐 AI Agent Memory Security Lab")

st.write(
    """
Demonstration of:

- Memory Poisoning
- Detection
- Risk Scoring
- Audit Logging
- Least Privilege
- Role Based Access Control
"""
)

# ----------------------------------------------------
# HEALTH
# ----------------------------------------------------

st.header("API Health")

try:

    health = requests.get(
        f"{API_URL}/health",
        timeout=5
    )

    if health.status_code == 200:
        st.success(health.json())
    else:
        st.error(health.text)

except Exception as e:
    st.error(e)
    st.stop()

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

try:

    memory = requests.get(
        f"{API_URL}/memory",
        headers=HEADERS
    ).json()

except Exception:

    memory = []

try:

    risk = requests.get(
        f"{API_URL}/risk",
        headers=HEADERS
    ).json()

except Exception:

    risk = {
        "risk_score": 0,
        "status": "UNKNOWN"
    }

# ----------------------------------------------------
# DASHBOARD METRICS
# ----------------------------------------------------

st.header("Security Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Memory Entries",
    len(memory)
)

col2.metric(
    "Risk Score",
    risk["risk_score"]
)

col3.metric(
    "Security Status",
    risk["status"]
)

# ----------------------------------------------------
# ALERTS
# ----------------------------------------------------

st.header("Security Alerts")

alerts = []

for note in memory:

    text = note["content"].lower()

    if "ignore" in text:
        alerts.append(
            f"Ignore instruction detected (Note {note['id']})"
        )

    if "override" in text:
        alerts.append(
            f"System Override detected (Note {note['id']})"
        )

    if "always say" in text:
        alerts.append(
            f"Response manipulation detected (Note {note['id']})"
        )

    if "never mention" in text:
        alerts.append(
            f"Hidden directive detected (Note {note['id']})"
        )

if alerts:

    for alert in alerts:
        st.error(alert)

else:

    st.success("No security alerts.")

# ----------------------------------------------------
# MEMORY
# ----------------------------------------------------

st.header("Current Memory")

if st.button("Refresh Memory"):
    st.rerun()

for note in memory:

    with st.expander(f"{note['id']} - {note['title']}"):

        st.write(f"**Title:** {note['title']}")
        st.write(note["content"])

        content = note["content"].lower()

        if "override" in content:
            st.error("Potential Memory Poisoning")

        elif "ignore" in content:
            st.warning("Suspicious Instruction")

        else:
            st.success("Trusted Memory")

# ----------------------------------------------------
# ADD MEMORY
# ----------------------------------------------------

st.header("Add Memory")

title = st.text_input("Title")

content = st.text_area("Content")

if st.button("Save Memory"):

    response = requests.post(
        f"{API_URL}/memory",
        headers=HEADERS,
        json={
            "title": title,
            "content": content
        }
    )

    if response.status_code == 200:

        st.success(response.json())

        st.rerun()

    else:

        st.error(response.text)

# ----------------------------------------------------
# INTEGRITY
# ----------------------------------------------------

st.header("Integrity Check")

if st.button("Run Integrity Check"):

    response = requests.get(
        f"{API_URL}/integrity/check",
        headers=HEADERS
    )

    if response.status_code == 200:

        result = response.json()

        if result["status"] == "PASS":

            st.success(result)

        else:

            st.error(result)

    else:

        st.error(response.text)

# ----------------------------------------------------
# ADMIN
# ----------------------------------------------------

if role == "Admin":

    st.header("Audit Logs")

    response = requests.get(
        f"{API_URL}/audit",
        headers=HEADERS
    )

    if response.status_code == 200:

        audit = response.json()

        for event in audit["events"]:
            st.code(event.strip())

    else:

        st.error(response.text)

    st.header("Integrity Baseline")

    if st.button("Create Baseline"):

        response = requests.post(
            f"{API_URL}/integrity/baseline",
            headers=HEADERS
        )

        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error(response.text)

else:

    st.info(
        "Audit Logs and Baseline Creation are available only to Administrators."
    )

st.markdown("---")

st.caption(
    "AI Agent Memory Security Lab | Defensive AI Security Demonstration"
)