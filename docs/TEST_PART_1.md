# Example test cases

### ✅ Backend API Tests (with Examples)

#### 🔹 `GET /students`
**Test:** Retrieve all students

```bash
curl http://127.0.0.1:5000/students
```

**Expected Response:**
```json
[
  {
    "id": 1,
    "name": "Alice",
    "university_id": 1
  },
  {
    "id": 2,
    "name": "Bob"
  }
]
```

---

#### 🔹 `POST /students`
**Test:** Add a new student

```bash
curl -X POST http://127.0.0.1:5000/students \
     -H "Content-Type: application/json" \
     -d '{"name": "Charlie"}'
```

**Expected Response:**
```json
{
  "message": "Student added successfully."
}
```

---

#### 🔹 `GET /universities`
**Test:** Fetch all universities

```bash
curl http://127.0.0.1:5000/universities
```

**Expected Response:**
```json
[
  {"id": 1, "name": "Harvard University"},
  {"id": 2, "name": "MIT"},
  {"id": 3, "name": "Stanford"}
]
```

---

#### 🔹 `POST /link-student`
**Test:** Link a student to a university (e.g., Charlie → MIT)

```bash
curl -X POST http://127.0.0.1:5000/link-student \
     -H "Content-Type: application/json" \
     -d '{"student_id": 3, "university_id": 2}'
```

**Expected Response:**
```json
{
  "message": "Student linked to university."
}
```

---
