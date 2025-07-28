# Data Science Lab Setup – AI Prompt Engineering

This lab prepares your system for hands‑on LLM engineering tasks, including prompt design, token counting, embeddings, and multi‑model orchestration.

---

## 1. Overview

A **full‑spec data science environment** is required to handle the computational load of the eight‑week program.  
The instructor will walk participants through this setup to ensure **consistent environments** and **prevent setup issues** mid‑course.

---

## 2. Two Setup Pathways

### **Primary Recommendation – Anaconda**
- Creates an **isolated environment** tailored for this course.
- Ensures high compatibility with instructor demos.
- Best for complex AI workflows and multi‑package management.

### **Alternative Path – Python Virtual Environment**
- Lightweight setup using `python -m venv` and `pip`.
- Faster to configure but less guaranteed to match the course dependencies.

---

## 3. Windows Environment Setup

### **Step 1: Clone the Repository**
git clone https://github.com/ed-donner/llm_engineering/
cd llm_engineering

### **Step 2: Create Conda Environment**

conda env create -f environment.yml

*(This step may take several minutes.)*

### **Step 3: Activate Environment**

conda activate llms

### **Step 4: Deactivate (Optional)**

conda deactivate

---

## 4. Troubleshooting Conda Activation (PowerShell)

If you see:

CondaError: Run 'conda init' before 'conda activate'

### **Solution**

#### 1. Initialize Conda

conda init powershell

Close and reopen PowerShell after running this.

#### 2. Enable Script Execution

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

Press `Y` to confirm. This allows your PowerShell profile (with Conda hooks) to load at startup.

#### 3. Test Conda Activation

conda --version
conda activate llms

#### 4. Quick One-Time Fix (No Restart)

Run this to manually load Conda:

& "C:\Users\<YourUsername>\anaconda3\shell\condabin\conda-hook.ps1"
conda activate llms

---

## 5. API Key Configuration

Create a `.env` file in the project root:

OPENAI_API_KEY=your-key-here

> Must be named **exactly** `.env` (not `.env.txt`).

---

## 6. Launch Lab

Run JupyterLab or VSCode to start working on prompts: jupyter lab or code.

---

## 7. Next Actions

* Verify notebook runs with OpenAI API.
* Begin **Prompt Engineering Fundamentals** lab.
* Progress toward **multi‑model prompt chaining** and **evaluation metrics**.

---

## 8. Resources

* [Course Repository](https://github.com/ed-donner/llm_engineering)
* [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html)
* [PowerShell Execution Policies](https://go.microsoft.com/fwlink/?LinkID=135170)
