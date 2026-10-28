import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("student.csv")

print("Student Marks Analyzer")

#print(data)

#total marks 

data["total"]=data["Python"]+data["Maths"]+data["English"]

#average

data["Average"]=data["total"]/3

print("\n Average marks of students ")

#print(data)


# Find the student with the highest total marks
topper = data.loc[data["total"].idxmax()]

print("\nTOPPER OF THE CLASS")
print("Name:", topper["Name"])
print("Total Marks:", topper["total"])
print("Average Marks:", round(topper["Average"], 2))

data["Result"]=data["Average"].apply(
    lambda marks : "pass" if marks >= 40 else "needs improvement"
)
# print("student result")
# print(data[["Name","Average","Result"]])

# plt.bar(data["Name"],["total"],color="pink")
# plt.title("Student marks Analyzer")
# plt.xlabel("Student Names")
# plt.ylabel("total Marks")
# plt.show()


print(data[["Name", "total"]])
print(data["total"].dtype)

plt.figure(figsize=(8, 5))
bars=plt.bar(data["Name"], data["total"], color="skyblue")

plt.title("Student Marks Analyzer")
plt.xlabel("Student Names")
plt.ylabel("Total Marks")

plt.ylim(0, 300)
plt.bar_label(bars)
plt.tight_layout()
plt.show()

data.to_csv("student_report.csv",index=False)
print("file Saved Successfully")