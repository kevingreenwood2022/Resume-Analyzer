# Resume Analyzer & Keyword Matcher

**Resume Analyzer & Keyword Matcher** is a Flask-based web application that helps users evaluate how well their resume matches a given job description. Users upload a resume file and paste a job description, and the app returns a compatibility score based on keyword overlap. This tool is designed to assist job seekers in optimizing their resumes for applicant tracking systems (ATS) and improving keyword targeting.

![screenshot](assets/img/resume-analyzer-preview.png)

---

## 🔍 Features

- Upload your resume in `.txt` or `.docx` format
- Paste any job description text
- Receive a keyword match percentage
- View lists of matched and missing terms
- Clean, responsive Bootstrap UI
- Simple scoring logic for fast results

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML, Bootstrap 5
- **Text Extraction:** Native `.txt` + `python-docx` for `.docx`
- **Comparison Logic:** Custom word-level keyword matching

---

## 📂 Project Structure

resume_analyzer/
├── app.py # Flask backend
├── analyzer.py # Text comparison logic
├── templates/ # HTML templates (base, index, result)
├── static/ # CSS & assets
├── uploads/ # Temp file storage (not committed)
└── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/kevingreenwood2022/Resume-Analyzer.git
cd Resume-Analyzer
Install dependencies

bash
Copy
Edit
pip install flask python-docx
Run the app

bash
Copy
Edit
python app.py
Open in browser
Go to http://localhost:5000

🧪 Sample Test Files
Sample resume and job description files are included in the repository for testing:

sample_resume.txt

sample_job_description.txt

✨ Future Improvements
Support for .pdf parsing

Weighted keyword scoring

Synonym detection using NLP

Exportable keyword reports

🧑‍💻 Author
Kevin Greenwood
