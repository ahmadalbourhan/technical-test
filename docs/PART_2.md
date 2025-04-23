## Part 2: Find and Fix the AI Bugs


### Fixed HTML + JS Code

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Student Page</title>
  </head>
  <body>
    <h1>Students List</h1>
    <ul id="studentList">
      <li>Ali</li>
      <li>Maya</li>
    </ul>

    <input type="text" id="name" placeholder="Enter student name" />
    <button onclick="addStudent()">Add</button>

    <script>
      function addStudent() {
        const name = document.getElementById("name").value;
        if (!name.trim()) {
          alert("Please enter a valid name.");
          return;
        }
        const li = document.createElement("li");
        li.textContent = name;
        document.getElementById("studentList").appendChild(li);
        document.getElementById("name").value = "";

        alert("Student " + name + " added");
      }
    </script>
  </body>
</html>
```

---


##  Bug Fix Summary

| ❌ Bug                                  | ✅ Fix                                  | 💬 Explanation                                                   |
|----------------------------------------|----------------------------------------|------------------------------------------------------------------|
| 1. Heading closed with `</h2>`         | Replaced with `</h1>`                  | Tag mismatch causes visual and structural issues.                |
| 2. Wrong ID `"Name"` (capital N)       | Corrected to `"name"`                  | JavaScript IDs are case-sensitive.                              |
| 3. Broken alert string concat          | Fixed to `'Student ' + name + ' added'`| Missing `+` caused a syntax error.                               |
| 4. Used string in `appendChild()`      | Used `createElement` + `textContent`   | `appendChild()` needs a DOM node, not an HTML string.           |
| 5. No input validation                 | Checked if name is empty or whitespace | Prevents blank names from being added to the list.              |

---


## How ChatGPT Helped

Initially, I reviewed the code manually and fixed the most critical bugs on my own, including:

- Correcting the mismatched heading tag (`</h2>` → `</h1>`)
- Fixing the wrong element ID reference (`"Name"` → `"name"`)
- Fixing string concatination in alert message
- Properly appending a new `<li>` element using `createElement()` instead of a string

Once the main functional issues were fixed, I asked ChatGPT to:

- Review the code for additional improvements and potential bad practices
- Suggest enhancements for cleaner, safer DOM manipulation
- Recommend adding input validation to prevent blank entries
- Explain the difference between DOM string insertion vs. node-based appending


This approach let me handle the essentials first, then refine and polish the solution with AI assistance. The result is a working, well-structured webpage with both functionality and better user experience.

---
