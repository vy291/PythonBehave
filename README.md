# Python Behave
Automation codebase.

**How to run in local**
================================
1. Install Git in your local machine. (Check by command: git --version)
2. Install Python 3.9.5. (Check by command: python --version)
3. Clone the repository and place the code somewhere in your local machine and open terminal at that folder.
4. Enter below commands:
    - **python -m pip install --upgrade pip**
    - **pip install -r requirements.txt**
5. Update file setup.cfg:
   - **browser=chrome** or **browser=firefox**
6. Edit file run.bat and enter below command for running:
   - **run** (for running full test cases)
   - **run @tagName** (for running full test suites with tag name)
   - **run featureName** (for running 1 feature)
7. Check output folder for test result and screenShot folder for debugging
 



