from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_DIR = "data"
STUDENTS_FILE = os.path.join(DATA_DIR, "students.json")
UNIVERSITIES_FILE = os.path.join(DATA_DIR, "universities.json")

# Helper functions
def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def write_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(read_json(STUDENTS_FILE))

@app.route("/students", methods=["POST"])
def add_student():
    students = read_json(STUDENTS_FILE)
    new_student = request.json
    new_student["id"] = len(students) + 1
    students.append(new_student)
    write_json(STUDENTS_FILE, students)
    return jsonify({"message": "Student added successfully."})

@app.route("/universities", methods=["GET"])
def get_universities():
    return jsonify(read_json(UNIVERSITIES_FILE))

@app.route("/link-student", methods=["POST"])
def link_student():
    students = read_json(STUDENTS_FILE)
    data = request.json
    for student in students:
        if student["id"] == data["student_id"]:
            student["university_id"] = data["university_id"]
            break
    write_json(STUDENTS_FILE, students)
    return jsonify({"message": "Student linked to university."})

if __name__ == "__main__":
    app.run(debug=True)
