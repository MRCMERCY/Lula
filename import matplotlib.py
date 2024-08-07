import matplotlib.pyplot as plt

# Data
student_ids = range(1, 31)
green_electricity_usage = ["High" if i < 22 else "Medium" if i % 3 == 0 else "Low" for i in student_ids]
non_renewable_electricity_usage = ["Low" if gu == "High" else "Medium" if gu == "Medium" else "High" for gu in green_electricity_usage]

# Count students using more green electricity vs non-renewable electricity
green_electricity_count = green_electricity_usage.count("High") + green_electricity_usage.count("Medium")
non_renewable_electricity_count = non_renewable_electricity_usage.count("High") + non_renewable_electricity_usage.count("Medium")

# Create the graph
plt.figure(figsize=(8, 6))
plt.bar(["Green Electricity", "Non-Renewable Electricity"], [green_electricity_count, non_renewable_electricity_count])
plt.xlabel("Electricity Type")
plt.ylabel("Number of Students")
plt.title("Electricity Usage Among 30 Students")
plt.show()