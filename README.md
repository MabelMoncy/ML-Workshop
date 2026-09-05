# Machine Learning Workshop

## Introduction

As part of the **KTU 2024 Scheme**, Machine Learning is included in our academic curriculum. This workshop is designed to provide a practical introduction to Machine Learning concepts covered in our syllabus.

The workshop focuses on understanding the fundamental concepts of Machine Learning and implementing them using Python and commonly used data science libraries. It aims to bridge the gap between **theoretical concepts learned in class and their practical implementation**.

---

# Installation and Setup

## Requirements

Make sure the following software is installed on your system:

* **Python 3.12**

### Python Libraries

The workshop uses the following Python libraries:

* `numpy`
* `pandas`
* `matplotlib`
* `seaborn`
* `scikit-learn`

---

# Creating a Virtual Environment

It is recommended to create a **virtual environment** before installing the required packages. This keeps the workshop dependencies isolated from other Python projects on your system.

## Windows

### 1. Open the project folder

Open **Command Prompt** or **PowerShell** and navigate to your project directory:

```bash
cd path\to\your\project
```

### 2. Create the virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Command Prompt (CMD):**

```bash
venv\Scripts\activate
```

**PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

After successful activation, you should see something similar to:

```text
(venv) C:\YourProject>
```

---

## Linux

### 1. Open the terminal

Navigate to your project directory:

```bash
cd /path/to/your/project
```

### 2. Create the virtual environment

```bash
python3 -m venv venv
```

> If `venv` is not installed, install it using:

```bash
sudo apt install python3-venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

After successful activation, you should see:

```text
(venv) user@computer:~/project$
```

---

# Package Installation

Once the virtual environment is activated, install the required Python libraries.

### Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Install the required packages

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### Verify the installation

You can verify that the packages were installed successfully using:

```bash
pip list
```

You should see packages such as:

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
```

---

# Deactivating the Virtual Environment

When you are finished working on the project, you can deactivate the virtual environment using:

```bash
deactivate
```

This command works on both **Windows and Linux**.

---

# Quick Setup

If Python 3.12 is already installed, the complete setup can be summarized as follows.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install numpy pandas matplotlib seaborn scikit-learn
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

> **Note:** The `venv/` folder is usually not committed to Git. Add it to your `.gitignore` file.

---

## Requirements File

For easier setup, the dependencies can also be stored in a `requirements.txt` file:

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
```

Then install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## Getting Started

After completing the setup, activate the virtual environment and start working through the workshop exercises and Machine Learning implementations.

Happy Learning! 🚀
