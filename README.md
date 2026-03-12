# 🏏 Cricket AI Assistant

### LLM-Powered Bowling Analysis Engine

An experimental **AI-powered cricket analytics assistant** that analyzes bowling session data and generates **coach-style commentary using Large Language Models (LLMs)**.

This project demonstrates how **structured sports data + LLM reasoning** can be combined to produce **human-readable insights**, similar to what a professional coach or commentator would say.

---

# 🚀 Features

📊 **Session Statistics Engine**

* Calculates average bowling speed
* Measures length consistency
* Tracks off-stump corridor accuracy

🧠 **LLM Coach Analysis**

* Uses a Large Language Model to generate **high-level bowling feedback**
* Provides:

  * Overall assessment
  * Strengths
  * Areas for improvement

🎯 **Ball-by-Ball Commentary**

* Each delivery is analyzed individually
* Produces **short coaching insights for every ball**

⚙️ **Modular Architecture**

* Clean separation between:

  * Data layer
  * Analytics layer
  * LLM reasoning layer

---

# 🧠 How It Works

The system follows a **data → analysis → reasoning pipeline**:

```
Bowling Data (JSON)
        ↓
Statistics Engine
        ↓
LLM Prompt Engineering
        ↓
AI Coach Analysis
        ↓
Human-Readable Insights
```

Example flow:

```
6 deliveries
     ↓
Statistical analysis
     ↓
LLM interpretation
     ↓
Coaching commentary
```

---

# 📂 Project Structure

```
Cricket-AI-Assistant
│
├── Data
│   └── deliveries.json        # Mock bowling session data
│
├── analysis
│   ├── stats.py               # Statistics engine
│   └── llm_analysis.py        # LLM prompt + analysis logic
│
├── main.py                    # Application entry point
│
└── README.md
```

---

# 📊 Example Input Data

```json
{
 "ball": 1,
 "speed": 138,
 "line": "off stump",
 "length": "good length",
 "swing": "inswing"
}
```

---

# 🧾 Example Output

```
Bowling Session Summary
----------------------
Average Speed: 138.5 km/h
Good Length Deliveries: 4/6
Outside Off Deliveries: 5/6
```

### 🧠 AI Coach Analysis

> The bowler demonstrates strong pace and good control of the off-stump corridor.
> However, improving consistency in hitting the good length area would significantly increase wicket-taking opportunities.

---

### 🎯 Ball by Ball Analysis

```
Ball 1
A good length delivery outside off stump at high pace.

Ball 2
A fast outswinger that challenges the batsman outside off stump.

Ball 3
A short ball on middle stump that could be pulled by the batsman.
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/cricket-ai-assistant.git
```

Navigate to the project directory:

```
cd cricket-ai-assistant
```

Install dependencies:

```
pip install langchain
pip install langchain-google-genai
pip install google-generativeai
```

---

# 🔑 Setup API Key

Create an API key and set it as an environment variable.

```
setx GOOGLE_API_KEY "your_api_key_here"
```

Restart the terminal after setting the key.

---

# ▶️ Running the Project

```
python main.py
```

---

# 🧩 Tech Stack

| Technology    | Role                      |
| ------------- | ------------------------- |
| Python        | Core programming language |
| LangChain     | LLM orchestration         |
| Google Gemini | Large Language Model      |
| JSON          | Structured bowling data   |

---

# 🎯 Why This Project?

This project demonstrates how **LLMs can be integrated with structured data pipelines** to produce **contextual analysis instead of raw numbers**.

Potential real-world applications:

* 🏏 Cricket training analytics
* 📊 Sports performance insights
* 🤖 AI coaching assistants
* 🎥 Automated match commentary

---

# 🔮 Future Improvements

* 📈 Advanced performance metrics
* 🧠 Pattern detection (line/length drift)
* 📊 Visualization dashboards
* 🎥 Video-based ball tracking
* ⚡ Real-time analysis during net sessions

---

# 👨‍💻 Author

**Varun Gupta**

BTech Student | AI & Systems Enthusiast
Interested in **AI systems, algorithmic thinking, and intelligent assistants**

---

# ⭐ If You Like This Project

Consider giving the repository a **star ⭐**.

It helps others discover the project and motivates further development.

---
