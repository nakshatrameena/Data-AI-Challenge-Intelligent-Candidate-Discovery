import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from models import db, Job, Candidate
from ai_engine import rank_candidates

# ---------------- APP SETUP ----------------
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recruiter.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = "uploads"

os.makedirs("uploads", exist_ok=True)

db.init_app(app)

with app.app_context():
    db.create_all()

# ---------------- HOME ----------------
@app.route("/")
def home():
    return "AI Recruiter System Running"

# ---------------- JOBS ----------------
@app.route("/jobs", methods=["POST"])
def create_job():
    data = request.get_json()

    job = Job(
        title=data["title"],
        description=data["description"]
    )

    db.session.add(job)
    db.session.commit()

    return jsonify({"job_id": job.id})


@app.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([
        {"id": j.id, "title": j.title}
        for j in jobs
    ])

# ---------------- CANDIDATES ----------------
@app.route("/candidates", methods=["POST"])
def create_candidate():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON received"}), 400

        name = data.get("name")
        resume_text = data.get("resume_text")

        if not name or not resume_text:
            return jsonify({"error": "Missing fields"}), 400

        c = Candidate(
            name=name,
            resume_text=resume_text
        )

        db.session.add(c)
        db.session.commit()

        return jsonify({
            "candidate_id": c.id,
            "status": "created"
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500



@app.route("/candidates", methods=["GET"])
def get_candidates():
    cands = Candidate.query.all()
    return jsonify([
        {"id": c.id, "name": c.name}
        for c in cands
    ])

# ---------------- RESUME UPLOAD ----------------
@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    try:
        file = request.files["file"]
        name = request.form.get("name", "Unknown")

        filename = secure_filename(file.filename)
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(path)

        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        c = Candidate(name=name, resume_text=text)
        db.session.add(c)
        db.session.commit()

        return jsonify({
            "message": "Resume uploaded",
            "candidate_id": c.id
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- AI RANKING ----------------
@app.route("/rank/<int:job_id>")
def rank(job_id):
    job = Job.query.get(job_id)

    if not job:
        return jsonify({"error": "Job not found"}), 404

    candidates = Candidate.query.all()

    result = rank_candidates(job.description, candidates)

    return jsonify({
        "job_title": job.title,
        "total_candidates": len(result),
        "rankings": result
    })

# ---------------- HEALTH ----------------
@app.route("/health")
def health():
    return jsonify(status="healthy")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
