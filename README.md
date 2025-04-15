
# IST 303 SOFTWARE DEVELOPMENT TEAM A 
# Project Title - CodeQuest: Python Mastery 🚀🐍

## 🔍 Overview  
**CodeQuest** is a Flask-based Python quiz platform that enables learners to test and master Python programming concepts.  
Built for both students and educators, the app supports student logins, admin question management, score tracking, leaderboard visibility, and custom quiz generation.

## Team Members
- Paniz Herrera
- Rogelio E. Garcia
- Hla Win Tun
- Emmanuel Nakitare
---
## 📌 Stakeholders

Understanding our stakeholders ensures that **CodeQuest** meets user needs, supports educators, and remains maintainable by developers.

1. **🧑‍🎓 Students & Learners**  
   - Primary users who take quizzes to improve Python knowledge.  
   - Includes CS students, beginner programmers, and bootcamp participants.

2. **📖 Educators & Content Managers**  
   - Use the **Admin Panel** to create, edit, or manage quiz content.  
   - Includes instructors, tutors, and teaching assistants using the app in classrooms.

3. **👨‍💻 Development Team & Future Contributors**  
   - Developers who built and maintain the quiz platform.  
   - Future coders may extend functionality, fix bugs, or enhance the user experience.

4. **🌐 Platform Managers / DevOps**  
   - Ensure the app is deployed securely and runs smoothly.  
   - Manage CI/CD pipelines, test automation, and database integrity.

---

## 🚀 Key Features

CodeQuest delivers an interactive, user-friendly Python quiz experience with dynamic admin control and performance tracking. Below are the final implemented features and planned enhancements.

### ✅ Core Features (Implemented)

- **🔐 Secure User Authentication**  
  Supports login for both **students** and **teachers** using Flask-Login. Credentials are safely stored and managed.

- **📚 Admin Panel with CRUD Functionality**  
  Admin users can **Create**, **Read**, **Update**, and **Delete** quiz questions via a dedicated dashboard.

- **🧠 Interactive Python Quiz Engine**  
  Students can take randomized multiple-choice quizzes across various topics and difficulties.

- **📊 Score Tracking & Quiz Feedback**  
  Users receive immediate feedback and a total score after submitting the quiz.

- **🏆 Leaderboard**  
  Displays top-performing users with highest scores to encourage friendly competition.

- **🛠️ Custom Quiz Generator**  
  Users can generate quizzes by selecting specific **topics**, **difficulty levels**, and number of questions.

- **📄 Export Options**  
  Users and admins can **export quizzes to PDF**, **send results via email**, and **toggle answer visibility**.

- **⚙️ GitHub Actions Integration**  
  CI/CD workflow automatically runs **Pytest test suites** on each push using `.github/workflows/actions.yml`.

---

 ### 🔭 Future Enhancements (Post-IST303 Module Roadmap)

While not part of the current course implementation, the following ideas were considered for future development to expand CodeQuest's learning experience:

- ⏱ **Timer-Based Mode** – Introduce time-limited questions for increased challenge.  
- 🧠 **Hints Per Question** – Offer optional hints to reinforce learning before submission.  
- 📊 **Progress Tracking Dashboard** – Let users view their quiz history and improvement trends.  
- 🔁 **Flashcard Review Mode** – Provide a passive review experience with question flashcards.  
- 🔊 **Sound Effects** – Add feedback sounds for correct/incorrect responses.  
- 🧮 **Adaptive Difficulty System** – Dynamically adjust question difficulty based on performance.  
- 🧩 **Gamification Features** – Incorporate badges, levels, or streaks to motivate consistent usage.  

> 📌 These enhancements are beyond the scope of the current IST 303 course but represent valuable directions for future iterations of the app.

---
 
## 🛠 Tech Stack

| Layer          | Tools Used                             |
|----------------|-----------------------------------------|
| **Frontend**   | HTML, CSS, Bootstrap                    |
| **Backend**    | Flask, Python 3.11                      |
| **Database**   | SQLite (development), schema.sql        |
| **Testing**    | Pytest, Flask Test Client               |
| **CI/CD**      | GitHub Actions (.yml configured)        |
| **Deployment** | Localhost (Render/Heroku planned)       |

---

## 📜 Updated User Stories & Estimated Completion Times

| **User Story**  | **Priority** | **Description** | **Updated Est. Time** |
|-----------------|--------------|------------------|------------------------|
| **User Registration** | High | As a new user, I want to register for an account so I can use the quiz app. | 0.5 week |
| **Student Login** | High | As a student, I want to log in with my credentials so I can take quizzes. | 0.5 week |
| **Teacher Login** | High | As a teacher, I want to log in with a teacher code so I can manage questions. | 0.5 week |
| **Take a Quiz** | High | As a student, I want to take quizzes and answer multiple-choice questions. | 1 week |
| **View Score** | High | As a student, I want to see my score immediately after submitting a quiz. | 0.5 week |
| **Quiz Feedback Toggle** | High | As a user, I want to show/hide correct answers and explanations to customize my view. | 1 week |
| **Leaderboard** | Medium | As a student, I want to see a leaderboard with top scores for motivation. | 1 week |
| **Admin Panel** | High | As a teacher, I want to add, edit, and delete quiz questions. | 1.5 weeks |
| **Filter Questions** | Medium | As a teacher, I want to filter questions by topic and difficulty for quicker editing. | 1 week |
| **Custom Quiz Generator** | High (Client Request) | As a user, I want to generate a quiz by clicking a button and filtering by difficulty, topic, and question count. | 1.5 weeks |
| **Preview Generated Quiz** | High | As a user, I want to preview generated quizzes before sharing or exporting. | 1 week |
| **Export to PDF** | Medium | As a user, I want to export the quiz to PDF so I can print it or study offline. | 1 week |
| **Email Quiz** | Medium | As a user, I want to email the quiz to myself or others for sharing. | 1 week |
| **Session Management** | Medium | As a user, I want to stay logged in securely and be notified if my session expires. | 0.5 week |
| **UI Responsiveness** | High | As a user, I want a clean and responsive interface for easy use on any device. | Ongoing |
| **GitHub Structure & Docs** | Medium | As a developer, I want clear documentation so contributors can understand the app. | Ongoing |
| **Quiz Attempt History** | Low (Future) | As a student, I want to view previous quiz attempts to track my progress. | Future |
| **Timer-Based Quiz Mode** | Low (Future) | As a user, I want a countdown timer during quizzes to manage time. | Future |
| **Adaptive Difficulty** | Low (Future) | As a user, I want quizzes to adjust difficulty based on my answers. | Future |

---

## 📅 Final Development Timeline Based on Iterations

| **Iteration**            | **Date Range**             | **Key Tasks & Deliverables**                                                                 |
|--------------------------|----------------------------|-----------------------------------------------------------------------------------------------|
| **Iteration 1**          | Feb 22 – Feb 26, 2025      | 🔹 Set up project repo, team roles, and dev environment. <br> 🔹 Completed **Register & Login** page. |
| **Iteration 2**          | Mar 8 – Mar 12, 2025       | 🔹 Built **Quiz Function & Score Tracker**. <br> 🔹 Refined multiple-choice logic and UI mid-sprint. |
| **Iteration 3**          | Mar 21 – Apr 4, 2025       | 🔹 Added **Admin Panel (CRUD)** & Teacher Login. <br> 🔹 Created **Pytest** tests and milestone validation. |
| **Iteration 4**          | Apr 7 – Apr 14, 2025       | 🔹 Implemented **Client Request** – Custom Quiz Generator. <br> 🔹 Added PDF export, UI polish, and leaderboard. |
| **Final Sprint**         | Apr 15 – Apr 23, 2025      | 🔹 Final Testing, Bug Fixes. <br> 🔹 GitHub Actions & Documentation. <br> ✅ Submitted final project (Part D). |

---

## 🔄 Adjustments & Considerations:

- ✅ **Client Feedback Integrated**: Custom quiz generator was added in Iteration 4 based on new client input.
- ⚠️ **Planned Enhancements Deferred**: Flashcards, adaptive difficulty, and sound effects moved to future pipeline.
- 📉 **Burndown Chart Informed Adjustments**: Timeline was adjusted as actual workdays slightly extended in Iteration 3.
- 🧪 **Testing Prioritized**: Pytest coverage and CI automation were established ahead of final submission.
- 📦 **Modular Milestones**: Work was structured around milestone check-ins, allowing progressive delivery and review.

---

## 📂 How to Run the Application

1. **Clone the repo:**
   ```bash
   git clone https://github.com/rogelg909/ist-303-team-A.git
   cd ist-303-team-A

2. **Create & activate a virtual environment:**
   python -m venv venv
   source venv/bin/activate
   
3. **Install dependencies:**
   pip install -r requirements.txt
 
4. **Initialize the database**
   python init_db.py
   
5. **Run the Flask app:**
   python app.py
   
6. **Open in browser:**
   http://localhost:5000

---
## 🧪How To Run Test & Check Coverage

1. **Run all test cases using Pytest:**
2. **Check coverage (optional)**
3. **CI/CD via GitHub Actions:
   - actions.yml is location in .github/workflows/
   - Automatically triggers tests on every push to main

---

## ✨ Three Most Important Things We Learned

- 🔄 **Agile development** helped us manage an evolving scope and respond effectively to late-stage client feature requests (e.g., custom quiz generation).
  
- 🔁 **Flask session handling and routing logic** required careful synchronization between frontend templates and backend view functions, especially during toggling answer visibility and managing quiz flows.

- ✅ **GitHub Actions** ensured reliable continuous integration by automatically running test cases with Pytest before merging, helping us maintain code quality and deployment readiness.

---

## 📁 Repository Structure

ist-303-team-A/
├── app.py
├── requirements.txt
├── init_db.py
├── schema.sql
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── quiz_start.html
│   ├── quiz_question.html
│   ├── quiz_results.html
│   ├── quiz_feedback.html
│   ├── admin_panel.html
│   ├── add_question.html
│   ├── edit_question.html
│   ├── quiz_preview.html
│   └── quiz_pdf_template.html
│
├── static/
│   ├── style.css
│   └── bootstrap.min.css
│
├── test/
│   ├── test_auth.py
│   ├── test_quiz_flow.py
│   ├── test_access_control.py
│   └── test_validation.py
│
├── .github/
│   └── workflows/
│       └── actions.yml
│
├── .gitignore
├── README.md
├── PART_B.md
├── PART_C.md
└── PART_D.md

---

## 📂 Additional Documentation

- 📜 [PART_B.md – Planning & User Stories](PART_B.md)
- 🧩 [PART_C.md – Wireframes & Design Decisions](PART_C.md)
- 🚀 [PART_D.md – Final Delivery & Reflections](PART_D.md)

---

## Contact 
# Emails
- paniz.herrera@cgu.edu
- rogelio.garcia@cgu.edu
- hla-win.tun@cgu.edu
- emmanuel.nakitare@cgu.edu
