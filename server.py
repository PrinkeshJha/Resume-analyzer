# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import os
# # import tempfile
# # from werkzeug.utils import secure_filename
# # import PyPDF2
# # from docx import Document
# # import re

# # app = Flask(__name__)
# # CORS(app)

# # ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}
# # MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max

# # def allowed_file(filename):
# #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # def extract_text_from_pdf(file_path):
# #     text = ""
# #     with open(file_path, 'rb') as file:
# #         pdf_reader = PyPDF2.PdfReader(file)
# #         for page in pdf_reader.pages:
# #             text += page.extract_text()
# #     return text

# # def extract_text_from_docx(file_path):
# #     doc = Document(file_path)
# #     return " ".join([paragraph.text for paragraph in doc.paragraphs])

# # def extract_text_from_txt(file_path):
# #     with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
# #         return file.read()

# # def extract_skills(text):
# #     common_skills = [
# #         "python", "javascript", "java", "c++", "react", "node", "flask", "django",
# #         "html", "css", "sql", "nosql", "mongodb", "postgresql", "mysql",
# #         "machine learning", "data analysis", "data science", "ai", "nlp",
# #         "project management", "agile", "scrum", "leadership", "communication",
# #         "problem solving", "critical thinking", "teamwork", "cloud", "aws", "azure",
# #         "docker", "kubernetes", "git", "linux", "excel", "powerbi", "tableau",
# #         "sales", "marketing", "seo", "photoshop", "figma", "illustrator", "android",
# #         "ios", "testing", "cybersecurity", "networking"
# #     ]
# #     found_skills = []
# #     for skill in common_skills:
# #         if re.search(r'\b' + re.escape(skill) + r'\b', text.lower()):
# #             found_skills.append(skill)
# #     return found_skills

# # def analyze_resume(text):
# #     skills = extract_skills(text)

# #     skill_to_career = {
# #         "python": ["Software Developer", "Data Scientist", "Machine Learning Engineer"],
# #         "javascript": ["Frontend Developer", "Full Stack Developer", "Web Developer"],
# #         "java": ["Software Engineer", "Backend Developer", "Android Developer"],
# #         "c++": ["Software Engineer", "Game Developer", "Systems Engineer"],
# #         "react": ["Frontend Developer", "UI Developer", "Web Developer"],
# #         "node": ["Backend Developer", "Full Stack Developer", "API Developer"],
# #         "sql": ["Database Administrator", "Data Analyst", "Backend Developer"],
# #         "nosql": ["Database Engineer", "Big Data Developer"],
# #         "mongodb": ["Full Stack Developer", "NoSQL Developer"],
# #         "postgresql": ["Database Engineer", "DevOps Engineer"],
# #         "mysql": ["Database Administrator", "Software Engineer"],
# #         "html": ["Frontend Developer", "Web Designer"],
# #         "css": ["Frontend Developer", "UI Designer"],
# #         "flask": ["Backend Developer", "API Developer"],
# #         "django": ["Backend Developer", "Full Stack Developer"],
# #         "machine learning": ["Data Scientist", "AI Engineer", "Research Scientist"],
# #         "data analysis": ["Data Analyst", "Business Analyst", "BI Developer"],
# #         "data science": ["Data Scientist", "ML Engineer", "Decision Scientist"],
# #         "ai": ["AI Engineer", "Research Scientist"],
# #         "nlp": ["NLP Engineer", "AI Researcher"],
# #         "project management": ["Project Manager", "Product Manager", "Scrum Master"],
# #         "agile": ["Scrum Master", "Agile Coach"],
# #         "scrum": ["Scrum Master", "Agile Project Manager"],
# #         "leadership": ["Team Lead", "Engineering Manager", "Director"],
# #         "communication": ["Customer Success", "Sales Engineer", "Product Manager"],
# #         "problem solving": ["Software Developer", "Consultant", "Solutions Architect"],
# #         "critical thinking": ["Business Analyst", "Strategy Consultant"],
# #         "teamwork": ["Team Lead", "Scrum Master"],
# #         "cloud": ["Cloud Engineer", "DevOps Engineer", "Site Reliability Engineer"],
# #         "aws": ["Cloud Engineer", "DevOps Engineer", "Solution Architect"],
# #         "azure": ["Cloud Administrator", "DevOps Engineer"],
# #         "docker": ["DevOps Engineer", "Cloud Engineer"],
# #         "kubernetes": ["Site Reliability Engineer", "DevOps Engineer"],
# #         "git": ["Software Developer", "DevOps Engineer"],
# #         "linux": ["System Administrator", "DevOps Engineer"],
# #         "excel": ["Business Analyst", "Finance Analyst"],
# #         "powerbi": ["BI Developer", "Data Analyst"],
# #         "tableau": ["Data Visualization Expert", "BI Analyst"],
# #         "sales": ["Sales Executive", "Business Development Associate"],
# #         "marketing": ["Marketing Executive", "Digital Marketer"],
# #         "seo": ["SEO Specialist", "Digital Marketing Manager"],
# #         "photoshop": ["Graphic Designer", "Creative Director"],
# #         "figma": ["UI/UX Designer", "Product Designer"],
# #         "illustrator": ["Graphic Designer", "Visual Designer"],
# #         "android": ["Android Developer", "Mobile App Developer"],
# #         "ios": ["iOS Developer", "Mobile Engineer"],
# #         "testing": ["QA Engineer", "Test Automation Engineer"],
# #         "cybersecurity": ["Security Analyst", "Cybersecurity Engineer"],
# #         "networking": ["Network Engineer", "System Administrator"]
# #     }

# #     career_matches = []
# #     potential_careers = {}
# #     for skill in skills:
# #         if skill in skill_to_career:
# #             for career in skill_to_career[skill]:
# #                 potential_careers[career] = potential_careers.get(career, 0) + 1

# #     sorted_careers = sorted(potential_careers.items(), key=lambda x: x[1], reverse=True)

# #     for career, count in sorted_careers[:5]:
# #         match_score = min(100, 60 + count * 8)
# #         career_skills = [skill.title() for skill, careers in skill_to_career.items() if career in careers and skill in skills]

# #         if len(career_skills) < 4:
# #             career_skills += ["Problem Solving", "Critical Thinking", "Teamwork", "Attention to Detail"][:4 - len(career_skills)]

# #         career_matches.append({
# #             "title": career,
# #             "matchScore": match_score,
# #             "description": f"Your skills and experience align well with {career} positions.",
# #             "skills": career_skills[:4]
# #         })

# #     # Enhanced fallback suggestions
# #     generic_careers = [
# #         {
# #             "title": "Technical Writer",
# #             "matchScore": 61,
# #             "description": "Good documentation and communication skills can land you a writing job in tech.",
# #             "skills": ["Writing", "Communication", "Attention to Detail", "Research"]
# #         },
# #         {
# #             "title": "Product Manager",
# #             "matchScore": 65,
# #             "description": "Your combination of technical knowledge and communication skills align with product management.",
# #             "skills": ["Project Management", "Communication", "Problem Solving", "Strategy"]
# #         },
# #         {
# #             "title": "UX/UI Designer",
# #             "matchScore": 62,
# #             "description": "Your creative skills and user-centered thinking would be assets in design roles.",
# #             "skills": ["UI Design", "User Research", "Prototyping", "Creative Thinking"]
# #         },
# #         {
# #             "title": "QA Engineer",
# #             "matchScore": 58,
# #             "description": "Your attention to detail and methodical approach are valuable traits for quality assurance positions.",
# #             "skills": ["Testing", "Debugging", "Documentation", "Process Improvement"]
# #         },
# #         {
# #             "title": "IT Support Specialist",
# #             "matchScore": 57,
# #             "description": "Strong problem solving and technical support abilities suit this role.",
# #             "skills": ["Networking", "Troubleshooting", "Customer Support", "System Maintenance"]
# #         },
# #         {
# #             "title": "Business Analyst",
# #             "matchScore": 60,
# #             "description": "Analytical mindset and communication skills help in bridging tech and business.",
# #             "skills": ["Data Analysis", "Documentation", "Requirement Gathering", "Stakeholder Communication"]
# #         }
# #     ]

# #     fallback_index = 0
# #     while len(career_matches) < 5 and fallback_index < len(generic_careers):
# #         fallback = generic_careers[fallback_index]
# #         if fallback["title"] not in [c["title"] for c in career_matches]:
# #             career_matches.append(fallback)
# #         fallback_index += 1

# #     return career_matches

# # @app.route('/api/analyze-resume', methods=['POST'])
# # def upload_resume():
# #     if 'resume' not in request.files:
# #         return jsonify({"error": "No file part"}), 400
# #     file = request.files['resume']
# #     if file.filename == '':
# #         return jsonify({"error": "No selected file"}), 400
# #     if not allowed_file(file.filename):
# #         return jsonify({"error": "File type not allowed"}), 400

# #     temp_dir = tempfile.gettempdir()
# #     filename = secure_filename(file.filename)
# #     file_path = os.path.join(temp_dir, filename)
# #     file.save(file_path)

# #     try:
# #         file_ext = filename.rsplit('.', 1)[1].lower()
# #         if file_ext == 'pdf':
# #             text = extract_text_from_pdf(file_path)
# #         elif file_ext == 'docx':
# #             text = extract_text_from_docx(file_path)
# #         elif file_ext == 'txt':
# #             text = extract_text_from_txt(file_path)
# #         else:
# #             return jsonify({"error": "Unsupported file format"}), 400

# #         career_matches = analyze_resume(text)
# #         return jsonify({"careerMatches": career_matches}), 200

# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500
# #     finally:
# #         if os.path.exists(file_path):
# #             os.unlink(file_path)

# # if __name__ == '__main__':
# #     app.run(debug=True, host='0.0.0.0', port=5000)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os
# import tempfile
# from werkzeug.utils import secure_filename
# import PyPDF2
# from docx import Document
# import re
# import google.generativeai as genai
# import random

# app = Flask(__name__)
# CORS(app)

# # Configure Gemini API (replace with your actual API keys)
# # Hardcoded API Keys -  Replace with your actual keys.
# GOOGLE_API_KEYS = [
#       # Replace with your first API key
#     "AIzaSyAaaHq2z6ejcYwPmQh712e1FJzJa_ChcnA",  # Replace with your second API key
#     "AIzaSyAw1l706r8Qt-YtuLYA1fAKiGvW_JSo8cg"# Add more API keys as needed
# ]
# if not GOOGLE_API_KEYS:
#     print("Warning: No Google API Keys provided. Functionality will be limited.")

# # Initialize models (moved inside the function)
# model_pro = None
# model_vision = None
# genai.configure(api_key=GOOGLE_API_KEYS[0]) #important

# ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}
# MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB max


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def extract_text_from_pdf(file_path):
#     text = ""
#     try:
#         with open(file_path, 'rb') as file:
#             pdf_reader = PyPDF2.PdfReader(file)
#             for page in pdf_reader.pages:
#                 text += page.extract_text()
#     except Exception as e:
#         print(f"Error reading PDF: {e}")
#         return ""  # Important: Return empty string on error
#     return text


# def extract_text_from_docx(file_path):
#     try:
#         doc = Document(file_path)
#         return " ".join([paragraph.text for paragraph in doc.paragraphs])
#     except Exception as e:
#         print(f"Error reading DOCX: {e}")
#         return ""


# def extract_text_from_txt(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
#             return file.read()
#     except Exception as e:
#         print(f"Error reading TXT: {e}")
#         return ""


# def extract_skills(text):
#     common_skills = [
#         "python", "javascript", "java", "c++", "react", "node", "flask", "django",
#         "html", "css", "sql", "nosql", "mongodb", "postgresql", "mysql",
#         "machine learning", "data analysis", "data science", "ai", "nlp",
#         "project management", "agile", "scrum", "leadership", "communication",
#         "problem solving", "critical thinking", "teamwork", "cloud", "aws", "azure",
#         "docker", "kubernetes", "git", "linux", "excel", "powerbi", "tableau",
#         "sales", "marketing", "seo", "photoshop", "figma", "illustrator", "android",
#         "ios", "testing", "cybersecurity", "networking"
#     ]
#     found_skills = []
#     for skill in common_skills:
#         if re.search(r'\b' + re.escape(skill) + r'\b', text.lower()):
#             found_skills.append(skill)
#     return found_skills


# def analyze_resume(text):
#     skills = extract_skills(text)

#     skill_to_career = {
#         "python": ["Software Developer", "Data Scientist", "Machine Learning Engineer"],
#         "javascript": ["Frontend Developer", "Full Stack Developer", "Web Developer"],
#         "java": ["Software Engineer", "Backend Developer", "Android Developer"],
#         "c++": ["Software Engineer", "Game Developer", "Systems Engineer"],
#         "react": ["Frontend Developer", "UI Developer", "Web Developer"],
#         "node": ["Backend Developer", "Full Stack Developer", "API Developer"],
#         "sql": ["Database Administrator", "Data Analyst", "Backend Developer"],
#         "nosql": ["Database Engineer", "Big Data Developer"],
#         "mongodb": ["Full Stack Developer", "NoSQL Developer"],
#         "postgresql": ["Database Engineer", "DevOps Engineer"],
#         "mysql": ["Database Administrator", "Software Engineer"],
#         "html": ["Frontend Developer", "Web Designer"],
#         "css": ["Frontend Developer", "UI Designer"],
#         "flask": ["Backend Developer", "API Developer"],
#         "django": ["Backend Developer", "Full Stack Developer"],
#         "machine learning": ["Data Scientist", "AI Engineer", "Research Scientist"],
#         "data analysis": ["Data Analyst", "Business Analyst", "BI Developer"],
#         "data science": ["Data Scientist", "ML Engineer", "Decision Scientist"],
#         "ai": ["AI Engineer", "Research Scientist"],
#         "nlp": ["NLP Engineer", "AI Researcher"],
#         "project management": ["Project Manager", "Product Manager", "Scrum Master"],
#         "agile": ["Scrum Master", "Agile Coach"],
#         "scrum": ["Scrum Master", "Agile Project Manager"],
#         "leadership": ["Team Lead", "Engineering Manager", "Director"],
#         "communication": ["Customer Success", "Sales Engineer", "Product Manager"],
#         "problem solving": ["Software Developer", "Consultant", "Solutions Architect"],
#         "critical thinking": ["Business Analyst", "Strategy Consultant"],
#         "teamwork": ["Team Lead", "Scrum Master"],
#         "cloud": ["Cloud Engineer", "DevOps Engineer", "Site Reliability Engineer"],
#         "aws": ["Cloud Engineer", "DevOps Engineer", "Solution Architect"],
#         "azure": ["Cloud Administrator", "DevOps Engineer"],
#         "docker": ["DevOps Engineer", "Cloud Engineer"],
#         "kubernetes": ["Site Reliability Engineer", "DevOps Engineer"],
#         "git": ["Software Developer", "DevOps Engineer"],
#         "linux": ["System Administrator", "DevOps Engineer"],
#         "excel": ["Business Analyst", "Finance Analyst"],
#         "powerbi": ["BI Developer", "Data Analyst"],
#         "tableau": ["Data Visualization Expert", "BI Analyst"],
#         "sales": ["Sales Executive", "Business Development Associate"],
#         "marketing": ["Marketing Executive", "Digital Marketer"],
#         "seo": ["SEO Specialist", "Digital Marketing Manager"],
#         "photoshop": ["Graphic Designer", "Creative Director"],
#         "figma": ["UI/UX Designer", "Product Designer"],
#         "illustrator": ["Graphic Designer", "Visual Designer"],
#         "android": ["Android Developer", "Mobile App Developer"],
#         "ios": ["iOS Developer", "Mobile Engineer"],
#         "testing": ["QA Engineer", "Test Automation Engineer"],
#         "cybersecurity": ["Security Analyst", "Cybersecurity Engineer"],
#         "networking": ["Network Engineer", "System Administrator"]
#     }

#     career_matches = []
#     potential_careers = {}
#     for skill in skills:
#         if skill in skill_to_career:
#             for career in skill_to_career[skill]:
#                 potential_careers[career] = potential_careers.get(career, 0) + 1

#     sorted_careers = sorted(potential_careers.items(), key=lambda x: x[1], reverse=True)

#     for career, count in sorted_careers[:5]:
#         match_score = min(100, 60 + count * 8)
#         career_skills = [skill.title() for skill, careers in skill_to_career.items() if
#                          career in careers and skill in skills]

#         if len(career_skills) < 4:
#             career_skills += ["Problem Solving", "Critical Thinking", "Teamwork",
#                               "Attention to Detail"][:4 - len(career_skills)]

#         career_matches.append({
#             "title": career,
#             "matchScore": match_score,
#             "description": f"Your skills and experience align well with {career} positions.",
#             "skills": career_skills[:4]
#         })

#     # Enhanced fallback suggestions
#     generic_careers = [
#         {
#             "title": "Technical Writer",
#             "matchScore": 61,
#             "description": "Good documentation and communication skills can land you a writing job in tech.",
#             "skills": ["Writing", "Communication", "Attention to Detail", "Research"]
#         },
#         {
#             "title": "Product Manager",
#             "matchScore": 65,
#             "description": "Your combination of technical knowledge and communication skills align with product management.",
#             "skills": ["Project Management", "Communication", "Problem Solving", "Strategy"]
#         },
#         {
#             "title": "UX/UI Designer",
#             "matchScore": 62,
#             "description": "Your creative skills and user-centered thinking would be assets in design roles.",
#             "skills": ["UI Design", "User Research", "Prototyping", "Creative Thinking"]
#         },
#         {
#             "title": "QA Engineer",
#             "matchScore": 58,
#             "description": "Your attention to detail and methodical approach are valuable traits for quality assurance positions.",
#             "skills": ["Testing", "Debugging", "Documentation", "Process Improvement"]
#         },
#         {
#             "title": "IT Support Specialist",
#             "matchScore": 57,
#             "description": "Strong problem solving and technical support abilities suit this role.",
#             "skills": ["Networking", "Troubleshooting", "Customer Support", "System Maintenance"]
#         },
#         {
#             "title": "Business Analyst",
#             "matchScore": 60,
#             "description": "Analytical mindset and communication skills help in bridging tech and business.",
#             "skills": ["Data Analysis", "Documentation", "Requirement Gathering",
#                                    "Stakeholder Communication"]
#         }
#     ]

#     fallback_index = 0
#     while len(career_matches) < 5 and fallback_index < len(generic_careers):
#         fallback = generic_careers[fallback_index]
#         if fallback["title"] not in [c["title"] for c in career_matches]:
#             career_matches.append(fallback)
#         fallback_index += 1

#     return career_matches


# def refine_career_matches_with_gemini(resume_text, career_matches):
#     if not GOOGLE_API_KEYS:
#         return career_matches  # Return original if no API key is available

#     prompt = f"""
#     You are a career counselor. I have analyzed a resume and found these potential career matches:
    
#     Resume Text:
#     ```{resume_text}```
    
#     Potential Career Matches:
#     {career_matches}
    
#     Review each career match and determine if it is a good fit based on the resume. 
#     If a career match is not a good fit, suggest a better alternative from the given generic careers.
    
#     Generic Careers:
#     Technical Writer, Product Manager, UX/UI Designer, QA Engineer, IT Support Specialist, Business Analyst
    
#     Provide your response in JSON format.  For each career match, output the following:
    
#     {{
#         "original_title": "(Original Career Title)",
#         "is_suitable": (True/False),
#         "alternative_title": "(Alternative Career Title, only if is_suitable is False)",
#         "reason": "(A brief explanation for your assessment)"
#     }}
    
#     Example Output:
#     [
#         {
#             "original_title": "Software Developer",
#             "is_suitable": true,
#             "alternative_title": null,
#             "reason": "The resume lists programming skills like Python and Java, which are relevant to software development."
#         },
#         {
#             "original_title": "Data Scientist",
#             "is_suitable": false,
#             "alternative_title": "Business Analyst",
#             "reason": "While the resume mentions data analysis, it lacks the depth in statistical modeling and machine learning typically required for a Data Scientist. Business Analyst is a better fit."
#         },
#         ...
#     ]
#     """

#     # Convert career_matches to a string representation for the prompt
#     career_matches_str = "["
#     for match in career_matches:
#         career_matches_str += f'{{"title": "{match["title"]}", "matchScore": {match["matchScore"]}, "description": "{match["description"]}"}}, '
#     career_matches_str = career_matches_str.rstrip(', ') + "]"
#     prompt = prompt.replace("{career_matches}", career_matches_str)

#     for key_index in range(len(GOOGLE_API_KEYS)):  # Iterate through the keys
#         try:
#             genai.configure(api_key=GOOGLE_API_KEYS[key_index])
#             model_pro = genai.GenerativeModel('gemini-pro')
#             response = model_pro.generate_content(prompt)
#             response_text = response.parts[0].text
#             print(f"Gemini (Pro) Response: {response_text} using key index {key_index}")  # Debugging
#             refined_results = eval(response_text)
#             break  # If successful, break the loop
#         except Exception as e:
#             print(f"Error during Gemini API call with key {key_index}: {e}")
#             if key_index == len(GOOGLE_API_KEYS) - 1:  # If it's the last key
#                 print("All Gemini API keys failed.")
#                 return career_matches # Return the original
#             # If not the last key, continue to the next one

#     # Parse the JSON response from Gemini
#     refined_results = eval(response_text)  # Use json.loads for safer parsing

#     # Update career_matches based on Gemini's feedback
#     updated_career_matches = []
#     for result in refined_results:
#         if result["is_suitable"]:
#             # Find the original career in career_matches to keep its details
#             for original_match in career_matches:
#                 if original_match["title"] == result["original_title"]:
#                     updated_career_matches.append(original_match)
#                     break  # Exit the inner loop once found
#         else:
#             # Find the alternative career from the generic careers
#             alternative_title = result["alternative_title"]
#             # Refactor this part to avoid unnecessary loops and improve efficiency
#             generic_careers_dict = {
#                 "Technical Writer": {
#                     "title": "Technical Writer",
#                     "matchScore": 61,
#                     "description": "Good documentation and communication skills can land you a writing job in tech.",
#                     "skills": ["Writing", "Communication", "Attention to Detail", "Research"]
#                 },
#                 "Product Manager": {
#                     "title": "Product Manager",
#                     "matchScore": 65,
#                     "description": "Your combination of technical knowledge and communication skills align with product management.",
#                     "skills": ["Project Management", "Communication", "Problem Solving", "Strategy"]
#                 },
#                 "UX/UI Designer": {
#                     "title": "UX/UI Designer",
#                     "matchScore": 62,
#                     "description": "Your creative skills and user-centered thinking would be assets in design roles.",
#                     "skills": ["UI Design", "User Research", "Prototyping", "Creative Thinking"]
#                 },
#                 "QA Engineer": {
#                     "title": "QA Engineer",
#                     "matchScore": 58,
#                     "description": "Your attention to detail and methodical approach are valuable traits for quality assurance positions.",
#                     "skills": ["Testing", "Debugging", "Documentation", "Process Improvement"]
#                 },
#                 "IT Support Specialist": {
#                     "title": "IT Support Specialist",
#                     "matchScore": 57,
#                     "description": "Strong problem solving and technical support abilities suit this role.",
#                     "skills": ["Networking", "Troubleshooting", "Customer Support", "System Maintenance"]
#                 },
#                 "Business Analyst": {
#                     "title": "Business Analyst",
#                     "matchScore": 60,
#                     "description": "Analytical mindset and communication skills help in bridging tech and business.",
#                     "skills": ["Data Analysis", "Documentation", "Requirement Gathering",
#                                "Stakeholder Communication"]
#                 }
#             }

#             if alternative_title in generic_careers_dict:
#                 updated_career_matches.append(generic_careers_dict[alternative_title])

#     return updated_career_matches



# @app.route('/api/analyze-resume', methods=['POST'])
# def upload_resume():
#     if 'resume' not in request.files:
#         return jsonify({"error": "No file part"}), 400
#     file = request.files['resume']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400
#     if not allowed_file(file.filename):
#         return jsonify({"error": "File type not allowed"}), 400

#     temp_dir = tempfile.gettempdir()
#     filename = secure_filename(file.filename)
#     file_path = os.path.join(temp_dir, filename)
#     file.save(file_path)

#     try:
#         file_ext = filename.rsplit('.', 1)[1].lower()
#         text = ""
#         if file_ext == 'pdf':
#             text = extract_text_from_pdf(file_path)
#         elif file_ext == 'docx':
#             text = extract_text_from_docx(file_path)
#         elif file_ext == 'txt':
#             text = extract_text_from_txt(file_path)
#         else:
#             return jsonify({"error": "Unsupported file format"}), 400

#         career_matches = analyze_resume(text)
#         refined_career_matches = refine_career_matches_with_gemini(text, career_matches)  # Use Gemini
#         return jsonify({"careerMatches": refined_career_matches}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         if os.path.exists(file_path):
#             os.unlink(file_path)


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

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
