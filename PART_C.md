# **IST 303 CodeQuest - Part C Presentation** 🚀🐍  

## 📌 **Presentation Plan & Deliverables**  
This document provides a structured outline for the **Part C** presentation, including the project overview, agile methods, testing approach, and iteration breakdown.

---

## **Introduction**  

### **Project Overview**
CodeQuest - Python Mastery is an **interactive Python quiz application** designed to help users test and improve their knowledge.  
The goal of this project is to create an engaging, user-friendly, and scalable quiz system that provides:  
✅ **Real-time feedback**  
✅ **Score tracking**  
✅ **Administrative panel for quiz management**  

### **Team Members**
- Rogelio  
- Hla Win Tun  
- Paniz  
- Emmanuel  

### **Milestone 1.0 Goals**  
The first milestone focuses on developing a **Minimum Viable Product (MVP)** that includes:  
- **User authentication:** Register and log in to save progress  
- **Quiz functionality:** Display questions, allow user input, and validate responses  
- **Score tracking:** Store and display quiz results  
- **Basic UI improvements:** Color-coded responses and interactive feedback  
- **Testing & Documentation:** Ensuring quality through structured testing  

---

## **Feature Demonstration & Working Code**  

### **Implemented Features**
Each feature will be **demonstrated live**, showing how the **code is structured and how it fulfills user stories**.

| **Feature**            | **Functionality**                              | **Code Implementation**           | **User Story** |
|------------------------|--------------------------------|--------------------------------|--------------|
| **User Authentication** | Users can register and log in | `app.py (login(), register())` | "As a user, I want to register and log in to save my progress." |
| **Quiz Functionality**  | Users can start a quiz and answer questions | `app.py (quiz logic)`, `templates/quiz.html` | "As a user, I want to answer quiz questions and get feedback." |
| **Score Tracking**      | Users receive a final score at the end of the quiz | `app.py (score tracking)`, `templates/result.html` | "As a user, I want to see my final score at the end of the quiz." |
| **UI Improvements**     | The interface uses color-coded feedback for correct/incorrect answers | `static/style.css` | "As a user, I want an intuitive and engaging interface." |

---

### **Code Walkthrough**
- **Flask Application (`app.py`)** - Handles user authentication, quiz logic, and session management  
- **Database & Schema (`database.db`, `schema.sql`)** - Stores users, questions, and results  
- **Frontend (`templates/`, `static/`)** - UI rendering using Jinja templates and CSS  

---

## **Agile Methods Documentation**  

### **GitHub Repository & Agile Practices**
- **Sprint Planning & Meetings**:
  - **Part B documentation** outlines sprint goals.
  - **Meeting notes** are stored in `meeting_notes/`.
  - **Burndown chart** tracks progress and team velocity.
- **Commit History**:
  - Frequent commits, following a feature-branch workflow.
  - Code reviews and pull requests ensure high quality.

---

## **Testing & Quality Assurance**  

### **Manual Testing**
- **User Login**: Verified authentication flow  
- **Quiz Flow**: Ensured questions load, accept input, and validate responses  
- **Score Display**: Checked if the final score is calculated correctly  

### **Unit Testing (`test/test_quiz.py`)**
python
def test_quiz_logic():
    assert evaluate_answer("correct_answer") == True

---

# **Iteration 2: Enhancements & Presentation Preparation**

## **Key Focus Areas**
Following the completion of **Iteration 1**, which established the **core quiz functionality**, the **Iteration 2 sprint (March 8 - March 12)** was focused on:

✅ **UI improvements for a more engaging user experience**  
✅ **Enhancing quiz logic with additional retry features**  
✅ **Preparing the Part C presentation and documentation**  

---

## **Iteration 2 Sprint Breakdown**
| **Task**                                        | **Time Estimate** | **Completion Status** |
|------------------------------------------------|-----------------|------------------|
| **Improve UI responsiveness and styling**       | 5 hours         | ✅ Completed |
| **Enhance quiz feedback with color-coded responses** | 5 hours | ✅ Completed |
| **Implement retry logic for incorrect answers** | 5 hours         | ✅ Completed |
| **Conduct internal testing & UI fixes**         | 10 hours        | ✅ Completed |
| **Prepare for Part C presentation**             | 5 hours         | ✅ Completed |
| **Finalize GitHub documentation & README updates** | 5 hours | ✅ Completed |

📌 **Total Iteration 2 Workload:** **40 hours**  

## **Lessons Learned from Iteration 1 & 2**  
🔹 **UI implementation took longer than expected**, so we adjusted sprint priorities.  
🔹 **Agile methods helped us quickly adapt** to scope changes and team feedback. 

---

## **Velocity Consideration**
- **Total Workload for Iteration 1 & 2:** **80 hours**  
- **Team Capacity:** **40 hours/week (4 members × 10 hours each)**  
- **Planned Iterations Before Milestone 1.0 Completion:** **2 iterations**  
- **Completion Goal:** **Ensure the project is presentation-ready before March 12 (Part C deadline).**  

---

## **Beyond Iteration 2: Preparing for Milestone 2.0**
With **Iteration 2** completed, we are transitioning towards **Milestone 2.0**, which focuses on **enhanced features and scalability**. The next iteration will include:

📌 **Iteration 3 (Mar 15 - Mar 22)**  
🔹 **Admin Panel Development** (Manage users & quiz content)  
🔹 **Backend refinements for database efficiency**  
🔹 **Expanded Question Categories** (Python, SQL, Data Science)  

📌 **Iteration 4 (Mar 22 - Mar 29)**  
🔹 **Implement Leaderboard** (Show top quiz performers)  
🔹 **Enhanced Security Features** (User authentication improvements)  

📌 **Final Testing & Bug Fixes (Apr 1 - Apr 15)**  
🔹 **UI Optimization & Performance Testing**  
🔹 **Mobile Responsiveness Improvements**  

---

# **Burndown Chart - Workdays Remaining**  

## **Burndown Chart: Workdays Left for IST 303 Milestones**  

| **Iteration Milestone**                        | **Planned Days Remaining** | **Actual Days Remaining** |
|---------------------------------------------|------------------------|-----------------------|
| **Iteration 1 Start (Feb 22, 2025)**         | 20                     | 20                    |
| **Feb 24 (Completed Register & Login Page)** | 18                  | 18.76                 |
| **Feb 26 (Planned Completion of Iteration 1)** | 16                  | 15                    |
| **Iteration 2 Start (Mar 8, 2025)**          | 14                   | 13                    |
| **Mar 10 (Midpoint of Iteration 2)**         | 12                   | 11.5                     |
| **Mar 12 (Planned Completion of Iteration 2)** | 10                    | 11                    |
| **Iteration 3 Start (Mar 15, 2025)**         | 8                    | -                     |
| **Mar 22 (Milestone 2 Midpoint)**            | 6                     | -                     |
| **Mar 29 (Completion of Milestone 2)**       | 4                    | -                     |
| **Iteration 4 Start (Apr 1, 2025)**          | 2                   | -                     |
| **Apr 15 - 23 (Final Testing & Bug Fixes, Part D Submission)**       |                  | 

📌 **Note:** The "Actual Days Remaining" will be updated as progress continues.

![Burndownchart 20250307](https://github.com/user-attachments/assets/490d8dd4-4440-4c6b-95c1-389da45880a6)

## **Burndown Chart & Velocity Analysis**  

### **Burndown Chart Analysis**
📉 **The team maintained a steady burndown rate**, aligning closely with planned estimates.  
⚡ **The biggest gap occurred in Iteration 1 (UI delays), but we caught up by Iteration 2.**  
🏆 **Overall, the project stayed on track** for Milestone 1.0 completion by March 12.

---

## **Beyond Iteration 2: Preparing for Milestone 2.0**
### **What’s Next?**
- **Transition from MVP to full-featured product**: Expanding user interactivity.  
- **Biggest challenge:** Secure admin role management & database scalability.  
- **New priorities:** Adding a leaderboard & improving authentication security.  

### **Upcoming Features**
- **Admin Panel**: Allow management of quiz questions and user accounts  
- **Leaderboard**: Display top scores and rankings  
- **Expanded Question Categories**: Python, SQL, Data Science, and more  
- **UI Enhancements**: Improved layout, animations, and mobile responsiveness  

---

## **Development Timeline**  

| **Feature**                     | **Planned Completion** |
|----------------------------------|-----------------------|
| **Admin Panel Development**      | March 20, 2025       |
| **Implement Leaderboard**        | March 27, 2025       |
| **UI Enhancements**              | April 5, 2025        |
| **Final Testing**                | April 15, 2025       |
| **Submission (Part D)**          | April 23, 2025       |

---

## **Final Thoughts**
🚀 The project successfully delivered a working MVP in **Milestone 1.0**.  
🚀 **Milestone 2.0** will focus on **scalability, enhanced functionality, and a better user experience**.  
🚀 Agile methodologies, testing strategies, and continuous feedback have been crucial to our success.  

