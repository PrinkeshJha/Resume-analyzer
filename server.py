
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import tempfile
from werkzeug.utils import secure_filename
import PyPDF2
from docx import Document
import re

app = Flask(__name__)
CORS(app)

# Limit upload size to 5MB
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

# Allowed file types
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

# ----------- Utility Functions -----------

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return " ".join([paragraph.text for paragraph in doc.paragraphs])

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

def extract_skills(text):
    common_skills = [
        "python", "javascript", "java", "c++", "react", "node", "flask", "django",
        "html", "css", "sql", "nosql", "mongodb", "postgresql", "mysql",
        "machine learning", "data analysis", "data science", "ai", "nlp",
        "project management", "agile", "scrum", "leadership", "communication",
        "problem solving", "critical thinking", "teamwork", "cloud", "aws", "azure",
        "docker", "kubernetes", "git", "linux", "excel", "powerbi", "tableau",
        "sales", "marketing", "seo", "photoshop", "figma", "illustrator", "android",
        "ios", "testing", "cybersecurity", "networking"
    ]
    found_skills = []
    for skill in common_skills:
        if re.search(r'\b' + re.escape(skill) + r'\b', text.lower()):
            found_skills.append(skill)
    return found_skills

def analyze_resume(text):
    skills = extract_skills(text)

    skill_to_career = {
        "python": ["Software Developer", "Data Scientist", "Machine Learning Engineer"],
        "javascript": ["Frontend Developer", "Full Stack Developer", "Web Developer"],
        "java": ["Software Engineer", "Backend Developer", "Android Developer"],
        "c++": ["Software Engineer", "Game Developer", "Systems Engineer"],
        "react": ["Frontend Developer", "UI Developer", "Web Developer"],
        "node": ["Backend Developer", "Full Stack Developer", "API Developer"],
        "sql": ["Database Administrator", "Data Analyst", "Backend Developer"],
        "nosql": ["Database Engineer", "Big Data Developer"],
        "mongodb": ["Full Stack Developer", "NoSQL Developer"],
        "postgresql": ["Database Engineer", "DevOps Engineer"],
        "mysql": ["Database Administrator", "Software Engineer"],
        "html": ["Frontend Developer", "Web Designer"],
        "css": ["Frontend Developer", "UI Designer"],
        "flask": ["Backend Developer", "API Developer"],
        "django": ["Backend Developer", "Full Stack Developer"],
        "machine learning": ["Data Scientist", "AI Engineer", "Research Scientist"],
        "data analysis": ["Data Analyst", "Business Analyst", "BI Developer"],
        "data science": ["Data Scientist", "ML Engineer", "Decision Scientist"],
        "ai": ["AI Engineer", "Research Scientist"],
        "nlp": ["NLP Engineer", "AI Researcher"],
        "project management": ["Project Manager", "Product Manager", "Scrum Master"],
        "agile": ["Scrum Master", "Agile Coach"],
        "scrum": ["Scrum Master", "Agile Project Manager"],
        "leadership": ["Team Lead", "Engineering Manager", "Director"],
        "communication": ["Customer Success", "Sales Engineer", "Product Manager"],
        "problem solving": ["Software Developer", "Consultant", "Solutions Architect"],
        "critical thinking": ["Business Analyst", "Strategy Consultant"],
        "teamwork": ["Team Lead", "Scrum Master"],
        "cloud": ["Cloud Engineer", "DevOps Engineer", "Site Reliability Engineer"],
        "aws": ["Cloud Engineer", "DevOps Engineer", "Solution Architect"],
        "azure": ["Cloud Administrator", "DevOps Engineer"],
        "docker": ["DevOps Engineer", "Cloud Engineer"],
        "kubernetes": ["Site Reliability Engineer", "DevOps Engineer"],
        "git": ["Software Developer", "DevOps Engineer"],
        "linux": ["System Administrator", "DevOps Engineer"],
        "excel": ["Business Analyst", "Finance Analyst"],
        "powerbi": ["BI Developer", "Data Analyst"],
        "tableau": ["Data Visualization Expert", "BI Analyst"],
        "sales": ["Sales Executive", "Business Development Associate"],
        "marketing": ["Marketing Executive", "Digital Marketer"],
        "seo": ["SEO Specialist", "Digital Marketing Manager"],
        "photoshop": ["Graphic Designer", "Creative Director"],
        "figma": ["UI/UX Designer", "Product Designer"],
        "illustrator": ["Graphic Designer", "Visual Designer"],
        "android": ["Android Developer", "Mobile App Developer"],
        "ios": ["iOS Developer", "Mobile Engineer"],
        "testing": ["QA Engineer", "Test Automation Engineer"],
        "cybersecurity": ["Security Analyst", "Cybersecurity Engineer"],
        "networking": ["Network Engineer", "System Administrator"]
    }

    career_matches = []
    potential_careers = {}
    for skill in skills:
        if skill in skill_to_career:
            for career in skill_to_career[skill]:
                potential_careers[career] = potential_careers.get(career, 0) + 1

    sorted_careers = sorted(potential_careers.items(), key=lambda x: x[1], reverse=True)

    for career, count in sorted_careers[:5]:
        match_score = min(100, 60 + count * 8)
        career_skills = [skill.title() for skill, careers in skill_to_career.items() if career in careers and skill in skills]

        if len(career_skills) < 4:
            career_skills += ["Problem Solving", "Critical Thinking", "Teamwork", "Attention to Detail"][:4 - len(career_skills)]

        career_matches.append({
            "title": career,
            "matchScore": match_score,
            "description": f"Your skills and experience align well with {career} positions.",
            "skills": career_skills[:4]
        })

    fallback_careers = [
        {
            "title": "Technical Writer",
            "matchScore": 61,
            "description": "Good documentation and communication skills can land you a writing job in tech.",
            "skills": ["Writing", "Communication", "Attention to Detail", "Research"]
        },
        {
            "title": "Product Manager",
            "matchScore": 65,
            "description": "Your combination of technical knowledge and communication skills align with product management.",
            "skills": ["Project Management", "Communication", "Problem Solving", "Strategy"]
        },
        {
            "title": "UX/UI Designer",
            "matchScore": 62,
            "description": "Your creative skills and user-centered thinking would be assets in design roles.",
            "skills": ["UI Design", "User Research", "Prototyping", "Creative Thinking"]
        },
        {
            "title": "QA Engineer",
            "matchScore": 58,
            "description": "Your attention to detail and methodical approach are valuable traits for quality assurance positions.",
            "skills": ["Testing", "Debugging", "Documentation", "Process Improvement"]
        },
        {
            "title": "IT Support Specialist",
            "matchScore": 57,
            "description": "Strong problem solving and technical support abilities suit this role.",
            "skills": ["Networking", "Troubleshooting", "Customer Support", "System Maintenance"]
        },
        {
            "title": "Business Analyst",
            "matchScore": 60,
            "description": "Analytical mindset and communication skills help in bridging tech and business.",
            "skills": ["Data Analysis", "Documentation", "Requirement Gathering", "Stakeholder Communication"]
        }
    ]

    i = 0
    while len(career_matches) < 5 and i < len(fallback_careers):
        fallback = fallback_careers[i]
        if fallback["title"] not in [c["title"] for c in career_matches]:
            career_matches.append(fallback)
        i += 1

    return career_matches

# ----------- Flask Routes for Pages -----------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

# ----------- Resume Analysis API -----------

@app.route('/api/analyze-resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    temp_dir = tempfile.gettempdir()
    filename = secure_filename(file.filename)
    file_path = os.path.join(temp_dir, filename)
    file.save(file_path)

    try:
        ext = filename.rsplit('.', 1)[1].lower()
        if ext == 'pdf':
            text = extract_text_from_pdf(file_path)
        elif ext == 'docx':
            text = extract_text_from_docx(file_path)
        elif ext == 'txt':
            text = extract_text_from_txt(file_path)
        else:
            return jsonify({"error": "Unsupported file format"}), 400

        career_matches = analyze_resume(text)
        return jsonify({"careerMatches": career_matches}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

# ----------- Run Server -----------

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
