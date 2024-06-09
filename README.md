# crypo-ai-predictor
An A.I that is main written in python(backend) that allow the collection of data and capable of making prediction based on segmented analysis.


# Backend configuration
The backend is written in python and runs on a virtual environment
1. Create a Virtual Environment:
-Open your terminal or command prompt.
-Navigate to the directory where you want to create your project.
-Run the following command to create a virtual environment (replace myenv with your preferred name):
    python -m venv myenv

This will create a new folder named myenv containing the virtual environment.

2. Activate the Virtual Environment:
-On Windows:
    myenv\Scripts\activate

-On macOS/Linux:
    source myenv/bin/activate

You’ll see (myenv) in your terminal, indicating that the virtual environment is active.
3. Install Packages:
-While the virtual environment is active, install Python packages using pip. For example:
    pip install requests

4. Deactivate the Virtual Environment:
-To exit the virtual environment, run:
    deactivate

5. Reactivating the Virtual Environment:
-Whenever you work on your project, activate the virtual environment again.
-Using a requirements.txt File:
-Create a requirements.txt file to list all your project dependencies:
    pip freeze > requirements.txt

-To install the same dependencies later, use:
    pip install -r requirements.txt