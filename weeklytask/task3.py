
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SHOW = False

marks = np.array([
    [78, 85, 90],
    [65, 70, 60],
    [88, 92, 95],
    [55, 60, 58],
])

shape = marks.shape                       
student_avg = marks.mean(axis=1)            
subject_avg = marks.mean(axis=0)            

grace_marks = marks + 5                     
grace_marks = np.minimum(grace_marks, 100)  

weights = np.array([0.5, 0.3, 0.2])         
weighted_score = np.dot(grace_marks, weights)

print("Student averages:", student_avg.round(2))

if SHOW == True:
    print("Shape:", shape)
    print("Subject averages:", subject_avg)
    print("Marks after grace:")
    print(grace_marks)
    print("Weighted scores:", weighted_score)

employees = pd.read_csv("employees_raw.csv")
departments = pd.read_csv("departments.csv")

if SHOW == True:
    employees.info()
    print(employees.describe())
    print(employees.loc[0:2, ["name", "salary"]])   
    print(employees.iloc[0:3, 0:3])                 
    print(employees[employees["department"] == "IT"])   

employees = employees.drop_duplicates()
median_salary = employees["salary"].median()
employees["salary"] = employees["salary"].fillna(median_salary)

employees["salary"] = employees["salary"].astype(int)
employees["join_date"] = pd.to_datetime(employees["join_date"])

summary = employees.groupby("department").agg(
    headcount=("emp_id", "count"),
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
)
headcount_line = "Headcount:"
for dept in departments["department"]:
    if dept in summary.index:
        count = summary.loc[dept, "headcount"]
        headcount_line = headcount_line + " " + dept + " " + str(count) + " |"
headcount_line = headcount_line.rstrip(" |")  
print(headcount_line)

inner = pd.merge(employees, departments, on="department", how="inner")
left = pd.merge(employees, departments, on="department", how="left")
outer = pd.merge(employees, departments, on="department", how="outer")

no_employees = outer[outer["name"].isna()]
print("Outer join: department with no employees ->", no_employees["department"].tolist())

if SHOW == True:
    print("Inner rows:", len(inner), "| Left rows:", len(left), "| Outer rows:", len(outer))

plt.figure()
plt.bar(summary.index, summary["avg_salary"], label="Average salary")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average salary (INR)")
plt.legend()
plt.savefig("bar_chart.png")
plt.close()
plt.figure()
plt.hist(employees["salary"], bins=5, label="Employees")
plt.title("Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of employees")
plt.legend()
plt.savefig("histogram.png")
plt.close()

plt.figure()
plt.scatter(employees["experience"], employees["salary"], label="Employees")
plt.title("Salary vs Experience")
plt.xlabel("Experience (years)")
plt.ylabel("Salary (INR)")
plt.legend()
plt.savefig("scatter_plot.png")
plt.close()

hires = employees.groupby(employees["join_date"].dt.year).size()
plt.figure()
plt.plot(hires.index, hires.values, marker="o", label="Hires per year")
plt.title("Hiring Trend by Join Year")
plt.xlabel("Join year")
plt.ylabel("Employees hired")
plt.legend()
plt.savefig("line_chart.png")
plt.close()

print("Charts saved: bar_chart.png, histogram.png, scatter_plot.png, line_chart.png")

highest = summary["avg_salary"].idxmax()
lowest = summary["avg_salary"].idxmin()
correlation = employees["experience"].corr(employees["salary"])

insight_file = open("insights.txt", "w")
insight_file.write("Bar chart: " + highest + " has the highest average salary and " + lowest + " has the lowest.\n")
insight_file.write("Histogram: the median salary is " + str(int(employees["salary"].median())) + ".\n")
insight_file.write("Scatter plot: the correlation between experience and salary is " + str(round(correlation, 2)) + ".\n")
insight_file.write("Line chart: the company hired at most " + str(hires.max()) + " employee(s) in any year.\n")
insight_file.close()