### Setting Up the Development Environment

<br>

1. **Create a virtual environment** to ensure your production and VSCode environments are the same:

   ```bash
   python -m venv venv
   ```

<br>

2. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

<br>

3. **Install the necessary dependencies**:

   ```bash
   pip install fastapi uvicorn
   ```

<br>

4. **Generate the `requirements.txt`** to save the installed dependencies:

   ```bash
   pip freeze > requirements.txt
   ```

<br>

### Running the App

To run the FastAPI application with hot-reloading enabled, use the following command:

```bash
uvicorn main:app --reload
```

This will start the development server at `http://127.0.0.1:8000`, where you can access the API.

<br>

___

<br>

