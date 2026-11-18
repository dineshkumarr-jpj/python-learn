import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Ravi", "Divya"],
    "Age": [25, 28, 24, 27],
    "Salary": [25000, 30000, 22000, 28000]
}

df = pd.DataFrame(data)

print(df)