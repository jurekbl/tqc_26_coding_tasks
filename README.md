# tqc_26_coding_tasks
This repository contains the interface code for the coding assignments in QC808:Topological Quantum Computing at SDU in spring term 2026

## Repository Structure
- Each sheet has its own folder
  
Each folder contains:
- Code Interface files, amount of provided code depends on the length of the exercises  
- Instructions for the assignment  
- Optional example input/output  

**Important:** This repo does **not** contain solutions. Implementations are kept in a separate private repository and pushed to this repository if solutions of older tasks are necessary. 

---

## How to Use
### Option A
1. Clone the repo via HTTPS (it is public, no SSH needed):
```
git clone https://github.com/jurekbl/tqc_26_coding_tasks
```
2. Install the required packages:<br>
***Especially in Python 3.12 it is highly recommended to install the packages locally in a virtual environment!*** <br>
For this, run
```
python3 -m venv venv
source venv/bin/activate
```
Install the packages by
```
pip install -r requirements.txt
 ```

3. Pull updates weekly:
```
git pull
```
There could be new requirements, so run 
```
pip install -r requirements.txt
 ```
Work only in the folder for the current sheet.  <br>
Do **not** modify interface files unless instructed to avoid pulling issues for upcoming sheets.

### Option B
- Copy the interface code from the browser and paste it in your favorite environment. Make sure to install all packages from requirements.txt (locally is recommended when working in Python 3.12, see Option A)
  
---

## Submission Options
It is mandatory to use the provided interface code as it makes the assessment much easier.
You may submit your solutions in one of two ways:

### Option A (Recommended)

Upload your solution file as:
- Python file (`.py`)  
- Jupyter notebook (`.ipynb`)
- Text file (`.txt`)
in itslearning as :
- Filename format: `yourname_sheetXX.py`

If the sheet contains math exercises as well, upload these in a different pdf. 
You can also upload a single file containing both, but if the coding assignment cannot simply be copy-pasted, it does not count (e.g. do not copy code into a Latex file).

### Option B (At your own risk)

You can create a **public Git repository** containing your solution and share the link in itslearning. 

- **Important**: something (a comment including the repo-link suffices) has to be added to itslearning, otherwise the assignment cannot be graded.
- You are fully responsible — if it does not work, it counts as failed (this is not a class about GitHub).

---

## Notes

- Each week, a new sheet folder will be added.  
- Do not change or delete previous sheets.  
- Follow the instructions in each sheet carefully.