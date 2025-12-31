# ⌨️ Keystroke Logger Using Python and Streamlit

> ⚠️ **For Educational and Ethical Use Only**

---

## 📌 Project Title
**Keystroke Logger Using Python and Streamlit (Cyber Security Project)**

---

## 🧩 Problem Statement

With the rapid growth of cyber threats, malicious software such as keyloggers has become a serious risk to user privacy and data security. Keyloggers are capable of capturing sensitive information like passwords and confidential data without user awareness.

There is a need for practical demonstrations that help cybersecurity students understand how keystroke logging works at the operating system level so that such threats can be detected and prevented effectively.

---

## 📖 Project Description

This project is an **educational keystroke logging application** developed using **Python** and **Streamlit**.  
It demonstrates how keystrokes can be captured at the **OS level** using keyboard event listeners.

The application uses the `pynput` library to monitor keyboard activity and logs keystrokes only after explicit user consent. A Streamlit-based interface allows users to start and stop logging and view captured keystrokes in real time.

This project is strictly designed for:
- Cybersecurity education
- Ethical hacking training
- Malware analysis awareness
- Defensive security research

No data is transmitted externally or stored without user knowledge.

---

## 👥 End Users

- Cyber Security Students  
- Ethical Hackers  
- Security Researchers  
- Educators and Trainers  
- Red Team / Blue Team Professionals  

---

## 🛠️ Technologies Used

| Technology | Description |
|----------|-------------|
| Python | Core programming language |
| Streamlit | Web-based UI framework |
| pynput | OS-level keyboard listener |
| Visual Studio Code | Development environment |
| Windows OS | Testing platform |

---

## ⚙️ System Architecture

```

User Keyboard
↓
pynput Keyboard Listener
↓
Python Backend
↓
Streamlit Web Interface

````

---

## ✅ Features

- OS-level keystroke capturing
- Start and Stop logging control
- Safe handling of special keys
- Clean and simple UI
- Ethical usage warning
- No background persistence

---

## 📊 Results

- Successfully captured keystrokes at the OS level
- Demonstrated real-world keylogging behavior
- Prevented application crashes using safe key handling
- Improved understanding of keylogging attacks and defenses

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install streamlit pynput
````

### 2️⃣ Run the Application

```bash
streamlit run app.py
```

### 3️⃣ Testing Instructions

1. Click **Start Logging**
2. Type in **Notepad / VS Code / Terminal**
3. Click **Stop Logging**
4. View captured keystrokes in the Streamlit UI

> ❗ Typing inside the browser does not represent OS-level logging.

---

## 📂 Project Structure

```
keystroke_logger/
│
├── app.py          # Streamlit UI
├── logger.py       # Keystroke logging logic
├── README.md       # Project documentation
└── requirements.txt
```

---

## 🔐 Ethical Considerations

* This project is for **educational purposes only**
* User consent is mandatory
* No hidden data collection
* No remote data transmission
* Misuse of keyloggers is illegal and unethical

---

## 🚀 Future Enhancements

* Encrypted keystroke storage
* Log file export
* Keylogger detection module
* SIEM integration
* Machine learning-based threat analysis

---


## 📸 Screenshots

* Home Page UI
  <img width="1919" height="961" alt="Screenshot 2025-12-31 201805" src="https://github.com/user-attachments/assets/ab81a025-3155-4523-9c24-2fdc297060c1" />

* Start / Stop Logging
  <img width="1919" height="960" alt="Screenshot 2025-12-31 201844" src="https://github.com/user-attachments/assets/904927e2-57fd-46fd-beff-87f289ecc395" />

* Captured Keystrokes
  <img width="904" height="832" alt="Screenshot 2025-12-31 201905" src="https://github.com/user-attachments/assets/de900407-e502-46ec-9e74-0d0c1309068d" />

* `logger.py` Code
  <img width="1919" height="911" alt="Screenshot 2025-12-31 203334" src="https://github.com/user-attachments/assets/f4b2adc1-bd54-4e6e-a07d-4bd332d64dd2" />

* `app.py` Code
  <img width="1919" height="1079" alt="Screenshot 2025-12-31 203447" src="https://github.com/user-attachments/assets/8b1871ef-9076-4e79-b9bf-04072667b159" />


---

## 🙏 Acknowledgement

This project was developed as part of a **VIOS Cyber Security internship project** to understand keylogging mechanisms and raise awareness about cybersecurity threats.

---



