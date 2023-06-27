# Installation Guide
Follow the steps bellow to run the Flask app successfully.

# Requirements
You will need to create a virtual environment in order to install the needed libraries.
```
python3 -m venv <virtual_environment>
```

You can use the `requirements.txt` file to pip install each library/package.

# Creating A Module
In order to create the Flask app as a module, first we need to make sure that the `setup.py` file is located at the **root directory**.  Then we can run the following:
```
pip install -e .
```

# Run Flask App
To run the flask app as a module we now need to run the following:
```
flask --app blog_api/main.py run
```