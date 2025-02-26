
# IST 303 SOFTWARE DEVELOPMENT TEAM A 
# Project Title - CodeQuest: Python Mastery 🚀🐍

## Overview 
CodeQuest is a **Flask-based Python Quiz Web App** designed to help users test and improve their Python knowledge.  
It features **multiple-choice questions, user authentication, score tracking, and interactive gameplay**.

## Team Members
- Paniz Herrera
- Rogelio E. Garcia
- Hla Win Tun
- Emmanuel Nakitare
---
## 📌 Project Stakeholders
Understanding our stakeholders helps us ensure the quiz application meets their needs.

1. **🧑‍💻 Users (Learners & Developers)**  
   - Individuals who take the quiz to test and improve their Python knowledge.  
   - Includes students, beginner coders, and professionals refreshing their skills.  

2. **📖 Quiz Content Managers**  
   - Responsible for creating, updating, and managing quiz questions.  
   - Includes instructors, tutors, and contributors adding new quiz content.  

3. **👨‍💻 Developers (Team & Future Contributors)**  
   - Our project team who builds and maintains the web-based quiz application.  
   - Future contributors who may extend functionality, add questions, or improve performance.  

4. **🏫 Educators & Instructors**  
   - Teachers who may use this quiz in classrooms to engage students interactively.  
   - Coding bootcamps integrating this quiz for training purposes.  

5. **🌐 Platform Managers (Hosting & Deployment Team)**  
   - Responsible for managing the **Flask web application**, including hosting, security, and database management.  
   - Ensures smooth deployment, scalability, and maintenance of the online quiz platform.

---

## **🚀 Key Features**
### **✔ Core Features**
- **📖 Interactive Python Quiz**
  - Users can answer Python quiz questions to test and improve their knowledge.
  
- **🎨 User-Friendly Web Interface**
  - A clean and responsive web-based UI built with Flask & Bootstrap.
  - Clear multiple-choice format for easy answer selection.

- **📊 Score Tracking**
  - Displays the final score at the end of the quiz for progress tracking.

- **✅ Secure User Authentication**
  - Login and registration system to track user progress.

- **⚠️ Robust Error Handling**
  - Handles invalid inputs gracefully and provides retry prompts.

### **🎯 Additional Features (Planned Enhancements)**
- ⏳ **Timer-Based Quiz Mode** – Limits response time per question.  
- 💡 **Hints for Each Question** – Provides a hint to help users learn.  
- 🔄 **Flashcard Mode** – Allows users to review questions passively.  
- 🔊 **Sound Effects** – Plays correct/wrong answer sounds for engagement.  
- 📊 **User Progress & Quiz History** – Saves past quiz results for review.  
- 🏆 **Leaderboard** – Displays top players’ highest scores.  
- ✍️ **Custom Quiz Creation** – Admins can create and manage quizzes dynamically.  
- 🎯 **Adaptive Difficulty System** – Adjusts question difficulty based on performance.  

---
 
## ⚙️ Technical Stack

### **🖥 Programming Language:**
- **Python 3.x** – Core language used for development.

### **📚 Libraries & Frameworks:**
- **Backend:**
  - Flask – Web framework for building the quiz application.
  - Flask-SQLAlchemy – ORM for database management.
  - Flask-Login – Handles user authentication.
  
- **Frontend:**
  - HTML, CSS, Bootstrap – For designing the UI.
  - JavaScript – Enhancing interactivity (optional).

- **Database:**
  - SQLite (default) – Lightweight database for local development.
  - PostgreSQL (planned) – For production deployment.

### **🛠 Development Tools:**
- **Code Editor:** Visual Studio Code (or preferred Python IDE).
- **Version Control:** Git & GitHub for repository management.
- **Virtual Environment:** `venv` (to manage dependencies).
- **Deployment (Future Consideration):**  
  - Gunicorn (for production WSGI server)  
  - Render / Heroku / AWS (for hosting)  

---

## 📜 User Stories & Estimated Completion Times

| **User Story**  | **Priority** | **Description** | **Updated Est. Time** |
| --------------  | ------------ | --------------- | ------------------ |
| **Basic Quiz Functionality**  | High | As a user, I want to answer Python quiz questions so that I can test my knowledge and improve my skills. | **1 week** |
| **User-Friendly Interface**  | High | As a user, I want the quiz to display clear and formatted questions with multiple choices so that I can easily select my answer. | **1 week** |
| **Score Tracking** | High | As a user, I want to see my score at the end of the quiz so that I can track my performance. | **0.5 week** |
| **Error Handling & Input Validation** | High | As a user, I want the quiz to handle incorrect inputs gracefully so that I can retry without breaking the experience. | **1 week** |
| **Admin Panel for Quiz Management** | High | As an admin, I want to create, update, and delete quiz questions so that I can manage quiz content dynamically. | **1.5 weeks** |
| **Randomized Questions per Attempt** | Medium | As a user, I want different quiz questions each time I play so that I can get a fresh learning experience. | **1 week** |
| **⏳ Timer-Based Quiz Mode** | Medium | As a user, I want a time limit for each question so that I can challenge my speed and accuracy. | **1 week** |
| **📊 User Progress & Quiz History** | Medium | As a user, I want to see my past quiz scores and track my improvements over time. | **1.5 weeks** |
| **🏆 Leaderboard (Top 5 Players)** | Medium | As a user, I want to see a leaderboard that shows the top players so that I can compete with others. | **1.5 weeks** |
| **✍️ Custom Quiz Creation Mode** | Medium | As an admin, I want to create my own quiz sets by adding custom questions and answers. | **2 weeks** |
| **🎯 Adaptive Difficulty System** | Low (Future) | As a user, I want the quiz to adjust its difficulty based on my performance so that I am continuously challenged at my level. | **(Deprioritized for future updates)** |

---
### **🚀 Adjustments Summary:**
- **Kept Core Features:** Basic quiz functionality, user interface, score tracking, and error handling remain the top priority.
- **Batching Features:** Related features (e.g., quiz history, leaderboard) are grouped to improve workflow efficiency.
- **Deprioritized Non-Essential Features:** **Flashcard Mode, Sound Effects, and Adaptive Difficulty** are moved to future updates.
- **Strict Deadline Awareness:** Each feature is scoped within the available time before **April 23**, ensuring completion.

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
