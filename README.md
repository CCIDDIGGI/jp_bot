# jp_bot

This project works using a custom virtual environment that needs to be called "jp_venv", it is automatically omitted when the user does a push on the repository (check the .gitignore file on the root of the project).

How to make this work?

1.  Initial clone.
    Inside the directory you want to clone the project, open a command prompt and clone the project using git (git clone https://github.com/CCIDDIGGI/jp_bot.git).  
    After that, one should have a project structure containing also a "requirements.txt" file, located on the root of the project.
    The "requirements.txt" file contains all the dependencies and versions that the virtual environment needs to compile, run and build the project.

2.  Create the virtual environment.
    Open a command prompt inside the directory of the project and type "python -m venv jp_venv" (omit quotes), official docs for reference --> https://docs.python.org/3/library/venv.html

3.  Install all the necessary dependencies.
    After creating the virtual environment, navigate inside the newly created folder and open a command prompt inside the "Scripts" dir "...\jp_bot\jp_venv\Scripts".
    Run the "Activate" command and press enter. 
    The previous part is crucial, without an active virtual environment all the following dependencies will be installed globally, this might lead to a dependency conflict within different python projects.
    With the activated venv in the same command prompt run "pip install -r /path/to/your/files/requirements.txt" (change /path/to/your/files/requirements.txt with the dir containing the "requirements.txt" file, which should be the root of the project).
    Dependencies are now installed and the venv is active, the venv can be deactivated with the "deactivate" command, but it is needed active for step number 4.

4.  Open the project using an ide (visual studio code is recommended).
    With an active venv, on the bottom right of the ide window, right to the "Select language mode" tab select the "jp_venv" interpreter.
    The previous operation should fix all the issues correlated to dependencies and the environment is now operative.

How to install a new dependency?

With an active environment:

1.  Install the dependency.
    Run "pip install dependency-name" (change "dependency-name" with the desired dependency).

2.  Freeze the current "requirements.txt" file (optional if working alone).
    This operation is crucial since the newly installed dependency is only present in your local venv, to make it visible for everyone that a new dependency was installed we need to update the "requirements.txt" file.
    To do so, run the command "pip freeze > /path/to/your/files/requirements.txt" (change /path/to/your/files/requirements.txt with the dir containing the "requirements.txt" file, which should be the root of the project) and press enter.