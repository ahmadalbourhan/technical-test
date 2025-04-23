## Part 1: Build a Simple Full-Stack App (with AI Support)

### What the Tool Does

#### 1. **Backend – Flask (Python)**
Flask is a lightweight web framework written in Python, ideal for small to medium web applications. It’s simple, flexible, and provides the tools to handle essential web application features:

- **Routing**: Maps URLs to functions that execute when users visit specific paths (e.g., `/students`).
- **User Input**: Receives and processes data from user forms or APIs.
- **Response Output**: Sends back HTML pages or JSON data based on requests.
- **Database Integration**: Simple integration with data storage methods, such as JSON, for small-scale projects.

#### 2. **Database – JSON (for Simplicity)**
Instead of using a traditional database system like SQLite or PostgreSQL, this project utilizes **JSON** for storing data. This approach is lightweight and works well for rapid prototyping and small projects.

- Data is stored and managed in `.json` files (e.g., `students.json` and `universities.json`).
- Flask interacts with the JSON data using Python’s `json` module to read, update, and save data.
- Ideal for projects in the early stages or when database overhead is unnecessary.

#### 3. **Frontend – Core Web Technologies**
The frontend is built using standard web technologies to create a basic user interface and handle interactions:

- **HTML5**: Structures the content and defines the layout of the page.
- **CSS3**: Provides styling to make the interface visually appealing.
- **JavaScript**: Adds interactivity, such as sending data to the backend and updating the page dynamically.

---

### What I Asked ChatGPT/Copilot

#### 1. **Initial Setup:**
To kick off the project, I asked for a complete **project structure and boilerplate** using Flask, which included:

- Setting up a **Python virtual environment (`venv`)** to manage dependencies.
- Creating the basic **Flask app files**, such as `app.py`.
- Adding initial **API endpoints** to handle student and university data.

#### 2. **JSON Database (for Simplicity):**
I wanted to avoid the complexity of a traditional database, so I opted to store the data in a **JSON file**. This was perfect for a lightweight project.

- Data is stored in JSON format for quick access and easy manipulation.
- Flask uses Python’s built-in `json` module to read and write data to/from JSON files.
- This approach simulates basic CRUD (Create, Read, Update, Delete) operations without a database.

#### 3. **Endpoint Testing:**
Once the backend was set up, I asked for **`curl` commands** to test each API endpoint from the command line. I also used **Insomnia** to perform visual tests on the API. Both tools allowed me to:

- Verify the API functionality.
- Confirm the correct behavior of the backend when interacting with JSON data.

#### 4. **Next Steps – Frontend:**
After confirming the backend was working, I planned to ask for a simple **frontend structure** using:

- **HTML** for the content structure.
- **CSS** for styling.
- **JavaScript** for making requests to the Flask backend and displaying dynamic content.

The goal was to integrate the frontend with the backend and complete the full-stack application.

---

### How I Used AI Suggestions

1. **Project Initialization**:
   I asked the AI to generate a boilerplate Flask project, which included:

   - Setting up a **Python virtual environment**.
   - Creating basic **Flask files** (e.g., `app.py`).
   - Adding **API endpoints** for managing students and universities.

   These suggestions helped me set up the backend quickly.

2. **JSON File as a Database**:
   To manage data without a traditional database, I followed the AI's recommendation to use a **JSON file**:

   - I used Python’s **`json` module** to read from and write to the file.
   - The AI also helped me simulate operations with the JSON data, making it easier to manage the project’s data.

3. **API Testing with curl and Insomnia**:
   The AI provided **`curl` commands** for testing the backend API from the terminal. This allowed me to:

   - Verify the functionality of each API endpoint.
   - Check API responses using **Insomnia**, a GUI tool that made testing more user-friendly.

4. **Frontend Setup**:
   Once the backend was working, I requested suggestions for a **frontend structure**. The AI guided me on how to:

   - Create basic frontend files, including **index.html**, **styles.css**, and **script.js**.
   - Use **JavaScript’s `fetch()`** to send requests to the Flask API and display dynamic data on the frontend.

5. **Step-by-Step Progress**:
   I followed a **step-by-step approach** to avoid getting overwhelmed. First, I focused on getting the backend working with dummy data, then I moved on to the frontend. This approach helped me:

   - Break the process into manageable tasks.
   - Stay focused on one thing at a time, ensuring each part worked before moving to the next.

---

### Database Design (JSON-Based)

Since we’re using a **JSON file** as the database, the data is structured in a way that mimics a simple **key-value store** with entries represented as objects within lists. Here’s a basic example:

#### Example Data Structure

1. **students.json**:
   ```json
   [
     { "id": 1, "name": "Alice", "university_id": 1 },
     { "id": 2, "name": "Bob", "university_id": 2 }
   ]
   ```

2. **universities.json**:
   ```json
   [
     { "id": 1, "name": "Harvard University" },
     { "id": 2, "name": "MIT" },
     { "id": 3, "name": "Stanford" }
   ]
   ```

#### Data Relationships:
- **Students** are linked to a **university** by the `university_id` field.
- The **JSON structure** allows for easy retrieval, update, and addition of new data without complex database setups.

---

### Conclusion

Part 1 was focused on setting up the **backend with Flask** and creating a **simple JSON-based database**. The frontend will be developed in the next steps, where we’ll connect it with the backend and allow users to interact with the system.

---
