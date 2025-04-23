# Part D: Milestone 2.0 Final Report

## 1. Milestone 2.0 Team Presentation

Each team member contributed to a clear and structured class presentation demonstrating our completed features, architecture, and responsibilities. Live demo segments included:

- Student perspective: quiz interaction, leaderboard updates, and explanations toggle.
- Teacher perspective: admin panel access, quiz generation by topic/difficulty, export to PDF, and email delivery.

---

##  2. Working Code & Milestone Scope

### a. Working Code Demo

The app demonstrates:

- Functional registration/login for both students and teachers (with teacher code).
- Dynamic quiz with category/topic filters, scoring, and explanations.
- Leaderboard tracking top scores by quiz category.
- Teacher-only admin panel for managing quiz questions.
- PDF export and quiz email functionality for teachers.
- Toggle answers visibility during preview.

---

### b. Explanation of Milestone 2.0 Functionality

Milestone 2.0 focused on delivering key user stories:

1. **As a student**, I want to register and login.
2. **As a student**, I want to select quiz categories and view explanations.
3. **As a student**, I want to track my scores and see a leaderboard.
4. **As a teacher**, I want to register with a secret code and login securely.
5. **As a teacher**, I want to manage quiz questions via an admin panel.
6. **As a teacher**, I want to generate quizzes based on topic, difficulty, and limit.
7. **As a teacher**, I want to preview the quiz and control whether answers are visible.
8. **As a teacher**, I want to export the quiz to PDF and email it to myself.

---

### c. Agile Methodology & Burndown Chart

We followed Agile using 2-week sprints. Iteration progress was tracked internally via milestone sheets and burndown charts.

📉 Final Burndown Chart:

![Burndown Chart 04222025](https://github.com/user-attachments/assets/80d89200-d27b-4ccd-a509-002f682faccd)

---

### d. Testing Approach and Coverage

- **Manual Testing:** All major user flows including login, quiz attempts, admin panel, and exports were manually tested.
- **Automated Testing:** 
  - Pytest used for testing login, role-based access, quiz logic, and validation.
  - ~80% coverage via CLI output and terminal logs.

```bash
pytest
pytest --cov=. --cov-report=term-missing

CI/CD Integration: GitHub Actions automatically runs tests on every push to main.
---

### e. Key Successes, Failures & Lessons Learned

#### Successes:
- Delivered client-requested features (quiz preview, PDF export, emailing).
- Role-based access control for teachers and students.
- Clean and functional UI using Bootstrap.
- Working automated test workflow via GitHub Actions.

#### Failures:
- Login/session logic required extra time to debug early on.
- PDF generation initially had formatting issues.

#### Lessons Learned:
- UI/UX polishing is more time-consuming than expected.
- Translating vague client ideas into specific user stories is crucial.
- Dividing logic into small reusable components (modular functions) improves testability.

---

## 3. GitHub Upload of Presentation Materials
All final materials are stored under: PART_D

---

## 4. Final Code Repository Submission

### a. How to Run
# Clone the repo
git clone https://github.com/rogelg909/ist-303-team-A.git
cd ist-303-team-A

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Run the app
python app.py
Then visit: http://localhost:5000

---

### b. How To Test
# Run tests
pytest

# Optional: Check coverage
pytest --cov=. --cov-report=term-missing

---

### c. Top 3 Learnings
- **Design-first mindset** leads to faster delivery and better client alignment.
- **Reusability and DRY principles** are crucial for scalable Flask apps.
- **Role-based features** require early planning across routes, sessions, and templates.

---

### d. Commit Activity & Consistency
- Consistent commits over 8 weeks of work.
- Clean commit messages and descriptive PRs.
- GitHub **Insights** confirms weekly contribution by all members.

---

### e. Individual Contributions
- All team members committed and pushed code regularly.
- Workload was evenly distributed across coding, UI, and testing.
- **Contributor graph** on GitHub confirms fair team effort.

---

### f. Organization & Navigation
- Clear folder structure:
  - `templates/` – Jinja2 HTML pages
  - `static/` – CSS assets
  - `test/` – Pytest test scripts
  - `PartD/` – Final milestone deliverables
- `README.md` includes full instructions for setup and testing.

---

### g. Repository Standards
- `.gitignore` excludes `/venv/`, `.pyc`, and other generated files.
- `requirements.txt` contains all necessary dependencies.
- `.github/workflows/actions.yml` automates test runs via GitHub Actions.

---

### h. GitHub Feature Usage
-  **GitHub Actions** for continuous integration and test automation.
-  **GitHub Issues** used for lightweight tracking.
-  **No public GitHub Project board** was used.
- Sprint progress tracked via burndown charts and team documentation.

---


