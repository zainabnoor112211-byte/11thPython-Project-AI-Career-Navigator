"""AI Career Navigator - Streamlit dashboard (home page).

Run from the project root:  streamlit run frontend/app.py
"""
import streamlit as st

import api_client as api
import ui

ui.setup("Dashboard")

st.title("🧭 AI Career Navigator")
st.write("Find careers that fit your skills, analyze your resume and explore matching jobs.")

try:
    api.job_categories()
    st.sidebar.caption(f"Backend: connected ({api.API_URL})")
except api.ApiError as e:
    st.error(str(e))
    st.stop()

user = ui.refresh_user()
if user:
    c1, c2, c3 = st.columns(3)
    c1.metric("Skills on your profile", len(user["skills"]))
    try:
        c2.metric("Saved jobs", len(api.saved_jobs(ui.token())))
        hist = api.history(ui.token())
    except api.ApiError as e:
        ui.handle_expired(e)
        hist = []
    c3.metric("Past recommendations", len(hist))
    if hist:
        last = hist[0]["result"]
        st.subheader("Your latest recommendation")
        st.write(f"**{last['recommended_career']}** - match score **{last['match_score']}/100**")
        ui.chips(last["missing_skills"], "gap")
    elif not user["skills"]:
        st.info("Add your skills on the **Profile** page, then open **Career Results**.")
else:
    st.info("Log in or register from the sidebar to save your profile, history and jobs. "
            "You can still try **Career Results**, **Resume** and **Job Search** without an account.")

st.divider()
a, b, c = st.columns(3)
a.subheader("1. Profile")
a.write("Save your skills, education and interests.")
b.subheader("2. Career results")
b.write("See your best-matching careers, skill gaps and next steps.")
c.subheader("3. Jobs & resume")
c.write("Search jobs by skill and upload a PDF resume for feedback.")
