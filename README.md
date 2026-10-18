# 11thPython-Project-AI-Career-Navigator
An AI-powered career guidance platform that helps users explore career paths, assess skills, and discover suitable career opportunities. Copy Description
AI Career Navigator is a career guidance platform designed to help students and job seekers identify suitable career paths based on their skills, interests, and goals.
Key Features
- Career guidance and career-path exploration
- Skill assessment and analysis
- Backend API built with FastAPI
- Interactive frontend using Streamlit
- Data management with SQLAlchemy
- Career-related information and recommendations
Technologies Used
- Python
- FastAPI
- Streamlit
- Pandas
- SQLAlchemy
- SQLite / database integration, depending on project configuration
How to Run
python -m pip install -r requirements.txt
python -m uvicorn backend.main:app --reload


Open http://127.0.0.1:8000/docs to explore the API.
In a second terminal, run the frontend:
python -m streamlit run frontend/app.py


Open http://localhost:8501 to access the application.
Purpose
The goal of this project is to make career exploration easier by combining Python development, data analysis, and web application technologies.
