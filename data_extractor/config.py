file_paths = [
    "sample_data/attendance.csv",
    "sample_data/attendance.txt",
    "sample_data/attendance_logs.txt",
    "sample_data/attendance.json",
    "sample_data/attendance.xlsx"
]

VALIDATION_CONFIG = {
    "columns": ["EmployeeID", "Name", "Date", "CheckIn", "CheckOut", "Status"],
    "no_nulls": ["EmployeeID", "Date"],
    "dtypes": {
        "EmployeeID": "object",
        "Date": "object"
    },
    "no_duplicates": ["EmployeeID", "Date"]
}