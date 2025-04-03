
# 📘 Part D: Milestone 2.0 Final Report

## 🎤 1. Milestone 2.0 Team Presentation 

Each team member contributed to a clear and structured class presentation demonstrating our completed features, architecture, and responsibilities. Live demo segments included:

- Student perspective: quiz interaction and leaderboard updates.
- Teacher perspective: admin panel access and question management.

---

## 💻 2. Working Code & Milestone Scope 

### ✅ a. Working Code Demo 

The app demonstrates:

- Functional registration/login for students and teachers.
- Dynamic quiz with scoring and explanations.
- Leaderboard tracking per category.
- Teacher-exclusive admin panel for adding/editing/deleting questions.

Code is modular, organized into Flask routes, templates, and utility functions.

---

### 📌 b. Explanation of Milestone 2.0 Functionality 

Milestone 2.0 focused on the following user stories:

1. **As a student**, I want to register and login.
2. **As a student**, I want to select quiz categories and view explanations.
3. **As a student**, I want to track my scores and see a leaderboard.
4. **As a teacher**, I want to register with a secret code and login securely.
5. **As a teacher**, I want to manage quiz questions via an admin panel.

---

### 🔁 c. Agile Methodology & Burndown Chart 

We followed Agile using 2-week sprints. Daily communication and issue tracking were maintained in GitHub Projects.

📉 Final Burndown Chart:  

![Burndownchart 20250326](https://github.com/user-attachments/assets/671b2f2c-028f-4466-8b59-600ce285da4d)

---

### 🧪 d. Testing Approach and Coverage

- **Manual testing**: User registration, quiz progression, score submission, and admin access.
- **Automated testing**: Using `pytest` with ~80% test coverage.

```bash
pytest --cov=.
```

- Covered modules: quiz logic, scoring, access control.

---

### 🧠 e. Key Successes, Failures & Lessons Learned 

**Successes:**
- Smooth UI/UX using Bootstrap and Chart.js.
- Role-based access control implementation.
- Fully functional and secure admin panel.

**Failures:**
- Initial login flow had bugs in session management.
- Burndown lagged during teacher login setup.

**Lessons Learned:**
- UI polishing takes more time than expected.
- Clear user stories streamline development.
- Collaborative Git practices are essential for velocity.

---

## 📂 3. GitHub Upload of Presentation Materials 

All presentation materials are available in the repo under:

```
/PartD/
├── slides.pdf
├── demo_walkthrough.md
├── burndown_chart.png
```

[🔗 View Repository](https://github.com/rogelg909/ist-303-team-A)

---

## 📦 4. Final Code Repository Submission 

### a. How to Run 
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize DB
python init_db.py

# Start server
python app.py
```

---

### b. How to Test 

```bash
# Run all tests
pytest

# Show coverage
pytest --cov=. --cov-report=term-missing
```

---

### c. Top 3 Learnings 

1. Design-first mindset leads to faster delivery.
2. Reusability and DRY principles improve maintainability.
3. Role-based features require careful planning from both backend and frontend.

---

### d. Commit Activity & Consistency 

- Multiple commits per week tracked via GitHub.
- Clean commit messages.
- Consistent progress over the 6-week span.

---

### e. Individual Contributions 

- Every team member has committed.
- Workload distributed fairly.
- Code, testing, and documentation tracked by GitHub Contributors page.

---

### f. Organization & Navigation 

- Clear folder structure:
    - `templates/`
    - `static/`
    - `tests/`
    - `PartD/`
- README has complete setup instructions.

---

### g. Repository Standards 

- `.gitignore` includes `/venv/`, `__pycache__/`, etc.
- `requirements.txt` lists all dependencies.
- GitHub Actions YAML present for linting and test automation.

---

### h. GitHub Feature Usage 

- Used GitHub Issues for task breakdown.
- GitHub Projects board for sprint tracking.
- GitHub Actions to automate testing pipeline.

---
