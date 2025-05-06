from flask import Flask, render_template, request
from analyzer import compare_texts
from docx import Document
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def extract_text_from_docx(file_stream):
    """Extracts text from a .docx Word document."""
    doc = Document(file_stream)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files.get('resume')
    job_desc = request.form.get('job_description', '')

    if not resume_file or not job_desc.strip():
        return render_template('index.html', error="Please provide both a resume file and job description.")

    filename = resume_file.filename.lower()
    if filename.endswith('.txt'):
        resume_text = resume_file.read().decode('utf-8')
    elif filename.endswith('.docx'):
        resume_text = extract_text_from_docx(resume_file)
    else:
        return render_template('index.html', error="Unsupported file type. Please upload .txt or .docx files.")

    result = compare_texts(resume_text, job_desc)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)