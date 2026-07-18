import pandas as pd

data = {
    "EmployeeID": ["E101", "E102"],
    "Name": ["John Doe", "Jane Smith"],
    "Date": ["2026-07-01", "2026-07-01"],
    "CheckIn": ["08:55", "09:05"],
    "CheckOut": ["17:02", "17:00"],
    "Status": ["Present", "Late"]
}

df = pd.DataFrame(data)
# !pip install openpyxl
df.to_excel("attendance.xlsx", index=False)
