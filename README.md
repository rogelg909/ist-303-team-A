
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

## 📅 Updated 10-12 Week Development Timeline

| **Week**   | **Task** |
|----------- |----------|
| **Week 1 (Feb 26 - Mar 3)** | Define project scope, finalize user stories, set up development environment, assign team roles. |
| **Week 2 (Mar 4 - Mar 10)** | Implement **Basic Quiz Functionality**: Question display, answer input, and flow control. |
| **Week 3 (Mar 11 - Mar 17)** | Improve **User Interface & Formatting**, add **Multiple-Choice Support**, and refine quiz logic. |
| **Week 4 (Mar 18 - Mar 24)** | Implement **Score Tracking & Randomized Question Selection** for dynamic quizzes. |
| **Week 5 (Mar 25 - Mar 31)** | Develop **Error Handling & Input Validation**, ensure quiz handles incorrect inputs gracefully. |
| **Week 6 (Apr 1 - Apr 7)** | Build **Admin Panel for Quiz Management**, allow adding/updating/deleting questions. |
| **Week 7 (Apr 8 - Apr 14)** | Implement **Leaderboard & User Quiz History** to track progress over time. |
| **Week 8 (Apr 15 - Apr 21)** | Final testing, **Bug Fixes, Code Optimization**, and UI refinements. |
| **Apr 22 - Apr 23** | Final Deployment & Documentation. **Submit Project.** ✅ |

## 🔄 Adjustments & Considerations:
- **Prioritized Core Features** to meet deadline.
- **Batching Tasks Efficiently** to avoid bottlenecks.
- **Moved Less Critical Features (e.g., Adaptive Difficulty) to Future Enhancements**.
- **Final Week Dedicated to Testing & Optimization** to ensure smooth delivery.

---

## 📂 Additional Documentation
- 📜 [Part B - Project Planning & Breakdown](PART_B.md)

---

## Contact 
# Emails
- paniz.herrera@cgu.edu
- rogelio.garcia@cgu.edu
- hla-win.tun@cgu.edu
- emmanuel.nakitare@cgu.edu
