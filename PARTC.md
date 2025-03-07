# **IST 303 CodeQuest - Part C Presentation** 🚀🐍  

## 📌 **Presentation Plan & Deliverables**  

This document provides a structured outline for the **Part C** presentation, aligning with the **grading rubric** to ensure all requirements are met.  

---

## **Introduction**  

### **Project Overview**
CodeQuest - Python Mastery is an **interactive Python quiz application** designed to help users test and improve their knowledge. The goal of this project is to create an engaging, user-friendly, and scalable quiz system that provides real-time feedback, score tracking, and an administrative panel for quiz management.

### **Team Members**
- Rogelio  
- Hla Win Tun  
- Paniz  
- Emmanuel  

### **Milestone 1.0 Goals**  
The first milestone focuses on developing a **Minimum Viable Product (MVP)** that includes the core features of the application. These are:  
- **User authentication:** Register and log in to save progress  
- **Quiz functionality:** Display questions, allow user input, and validate responses  
- **Score tracking:** Store and display quiz results  
- **Basic UI improvements:** Color-coded responses and interactive feedback  
- **Testing & Documentation:** Ensuring quality through structured testing  

---

## **Feature Demonstration & Working Code**  

### **Implemented Features**
Each feature will be **demonstrated live**, showing how the **code is structured and how it fulfills user stories**.

| **Feature** | **Functionality** | **Code Implementation** | **User Story** |
|------------|----------------|------------------|--------------|
| **User Authentication** | Users can register and log in | `app.py (login(), register())` | "As a user, I want to register and log in to save my progress." |
| **Quiz Functionality** | Users can start a quiz and answer questions | `app.py (quiz logic)`, `templates/quiz.html` | "As a user, I want to answer quiz questions and get feedback." |
| **Score Tracking** | Users receive a final score at the end of the quiz | `app.py (score tracking)`, `templates/result.html` | "As a user, I want to see my final score at the end of the quiz." |
| **UI Improvements** | The interface uses color-coded feedback for correct/incorrect answers | `static/style.css` | "As a user, I want an intuitive and engaging interface." |

---

### **Code Walkthrough**
We will **explain how the code works** by reviewing key components:
- **Flask Application (`app.py`)** - Handles user authentication, quiz logic, and session management  
- **Database & Schema (`database.db`, `schema.sql`)** - Stores users, questions, and results  
- **Frontend (`templates/`, `static/`)** - UI rendering using Jinja templates and CSS  

---

## **Agile Methods Documentation**  

### **GitHub Repository & Agile Practices**
- The **GitHub repository** shows a structured **commit history**, proving **continuous integration** and team collaboration.  
- **Sprint Planning & Meetings**:
  - **Part B documentation** outlines sprint goals.
  - **Meeting notes** are stored in `meeting_notes/`.
  - **Burndown chart** tracks progress and team velocity.  

### **Testing & Quality Assurance**
We conducted **manual testing** and **automated unit tests** to ensure quality.  

#### **Manual Testing**
- **User Login**: Verified authentication flow  
- **Quiz Flow**: Ensured questions load, accept input, and validate responses  
- **Score Display**: Checked if the final score is calculated correctly  

#### **Unit Testing (`test/test_quiz.py`)**
```python
def test_quiz_logic():
    assert evaluate_answer("correct_answer") == True
