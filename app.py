from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# File paths
PATIENT_FILE = "patients.txt"
DOCTOR_FILE = "doctors.txt"
APPOINTMENT_FILE = "appointments.txt"
BILL_FILE = "bills.txt"

# ------------------- Patients -------------------
@app.route('/patients', methods=['GET'])
def get_patients():
    if not os.path.exists(PATIENT_FILE):
        return jsonify([])
    patients = []
    with open(PATIENT_FILE, "r") as file:
        for line in file:
            pid, name, age, disease = line.strip().split(",")
            patients.append({"pid": pid, "name": name, "age": age, "disease": disease})
    return jsonify(patients)

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    with open(PATIENT_FILE, "a") as file:
        file.write(f"{data['pid']},{data['name']},{data['age']},{data['disease']}\n")
    return jsonify({"message": "Patient added successfully!"})

# ------------------- Doctors -------------------
@app.route('/doctors', methods=['GET'])
def get_doctors():
    if not os.path.exists(DOCTOR_FILE):
        return jsonify([])
    doctors = []
    with open(DOCTOR_FILE, "r") as file:
        for line in file:
            did, name, specialty = line.strip().split(",")
            doctors.append({"did": did, "name": name, "specialty": specialty})
    return jsonify(doctors)

@app.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.json
    with open(DOCTOR_FILE, "a") as file:
        file.write(f"{data['did']},{data['name']},{data['specialty']}\n")
    return jsonify({"message": "Doctor added successfully!"})

# ------------------- Appointments -------------------
@app.route('/appointments', methods=['GET'])
def get_appointments():
    if not os.path.exists(APPOINTMENT_FILE):
        return jsonify([])
    appointments = []
    with open(APPOINTMENT_FILE, "r") as file:
        for line in file:
            pid, did, date = line.strip().split(",")
            appointments.append({"pid": pid, "did": did, "date": date})
    return jsonify(appointments)

@app.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.json
    with open(APPOINTMENT_FILE, "a") as file:
        file.write(f"{data['pid']},{data['did']},{data['date']}\n")
    return jsonify({"message": "Appointment added successfully!"})

# ------------------- Bills -------------------
@app.route('/bills', methods=['GET'])
def get_bills():
    if not os.path.exists(BILL_FILE):
        return jsonify([])
    bills = []
    with open(BILL_FILE, "r") as file:
        for line in file:
            pid, c, m, o = line.strip().split(",")
            bills.append({
                "pid": pid,
                "consultation_fee": float(c),
                "medicine_fee": float(m),
                "other_charges": float(o)
            })
    return jsonify(bills)

@app.route('/bills', methods=['POST'])
def add_bill():
    data = request.json
    with open(BILL_FILE, "a") as file:
        file.write(f"{data['pid']},{data['consultation_fee']},{data['medicine_fee']},{data['other_charges']}\n")
    return jsonify({"message": "Bill added successfully!"})

# ------------------- Run Server -------------------
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)