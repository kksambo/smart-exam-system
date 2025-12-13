
# **📘 Smart Exam System**

A modern, secure, AI-powered online examination platform designed to maintain academic integrity in fully online learning environments. The Smart Exam System prevents cheating through **AI proctoring**, **browser lockdown**, **dynamic question paraphrasing**, **audio monitoring**, and **hardware-assisted security**.

---

## **🌍 Overview**

With education rapidly shifting to digital platforms, students can easily use AI tools like ChatGPT to complete assessments, compromising learning quality.
The **Smart Exam System** solves this challenge by creating a **strict, monitored, and controlled exam environment**—while still delivering the convenience of online testing.

---

## **✨ Key Features**

### **🛡 1. AI-Powered Anti-Cheating Technology**

* Automatic question paraphrasing (no repeated questions)
* Multiple question versions per student
* AI monitoring for suspicious behaviors
* Detection of phone usage, whispering, and extra people

### **📷 2. Smart Proctoring**

* Continuous camera monitoring (WebRTC)
* Face detection & liveness tracking
* Eye movement monitoring (optional)
* Multi-person detection
* Photo capture during suspicious events

### **🔊 3. Audio Surveillance**

* Background noise detection
* Speech-to-text monitoring
* Alerts for conversation, whispering, or prompting

### **🔒 4. Browser Lockdown Mode**

Prevents digital cheating by blocking:

* Copy / Paste / Select / Right-click
* New tabs or windows
* Alt+Tab, Ctrl+Tab, Esc, PrintScreen, Task switching
* Minimize / exiting full screen
* Screen recording (to some extent)

### **📊 5. Teacher & Admin Tools**

* Create tests
* Add questions (MCQ, short answer, long answer)
* Auto-generate paraphrased question versions
* View analytics & cheating reports
* Manage learners, classes, subjects
* Export results & logs

### **🛠 6. Hardware Integration (Arduino)**

Optional physical anti-cheating enhancements:

* Motion sensors
* Sound detectors
* External cameras
* Room activity monitors

---

## **🧪 System Architecture**

```
React Frontend (TypeScript)
       │
       ├── WebRTC Camera Stream
       ├── WebRTC Audio Stream
       │
FastAPI Backend (Python)
       │
       ├── AI Paraphrasing Engine
       ├── AI Proctoring Engine
       ├── Browser Lockdown API
       │
PostgreSQL Database
       │
Arduino Hardware Sensors (C++)
```

---

## **🧰 Tech Stack**

### **Frontend**

* React (TypeScript)
* Vite / Webpack
* WebRTC (camera + mic streaming)
* Tailwind / MUI (optional)

### **Backend**

* Python FastAPI
* WebSockets for live monitoring
* OpenCV for camera analysis
* SpeechRecognition / Whisper
* NLTK / LLaMA / GPT for paraphrasing

### **Database**

* PostgreSQL
* Prisma / SQLAlchemy

### **Hardware**

* Arduino
* C++
* PIR sensors
* Sound sensors

---

## **📁 Project Structure (Proposed)**

```
smart-exam-system/
│
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── services/
│   ├── ai/
│   └── database/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   └── utils/
│
├── arduino/
│   ├── sensors/
│   └── monitoring/
│
├── docs/
│   └── architecture-diagram.png
│
└── README.md
```

---

## **⚙️ Features In Development**

* Fingerprint authentication
* Fully offline exam mode with auto-sync
* AI scoring for essay-type questions
* Continuous face & eye tracking
* Human proctor integration (live monitoring dashboard)

---

## **🚀 Getting Started**

### **1. Clone the repository**

```sh
git clone https://github.com/yourusername/smart-exam-system.git
cd smart-exam-system
```

### **2. Setup Backend**

```sh
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### **3. Setup Frontend**

```sh
cd frontend
npm install
npm run dev
```

### **4. Run Hardware (Optional)**

Upload Arduino code from the `arduino/` folder using Arduino IDE.

---

## **📌 Roadmap**

| Phase       | Features                                           |
| ----------- | -------------------------------------------------- |
| **Phase 1** | Authentication, Test creation, Basic exam engine   |
| **Phase 2** | Browser lockdown, auto-save, question paraphrasing |
| **Phase 3** | AI proctoring, audio detection, cheating logs      |
| **Phase 4** | Hardware sensors, room monitoring                  |
| **Phase 5** | Reporting, analytics, UI/UX polishing              |

---

## **📄 License**

This project is released under the **MIT License**.
Feel free to use, modify, and contribute.

---

## **🙌 Contributing**

Pull requests are welcome!
If you find bugs or want new features, open an issue.

---

## **📬 Contact**

**Developer:** Sicelo Sambo
**Project Name:** Smart Exam System


