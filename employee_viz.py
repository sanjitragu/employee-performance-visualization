"""
Employee Performance Visualization
Email: 24f3002886@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# 1. Load the dataset
df = pd.read_csv("employee_performance.csv")

# 2. Count HR department employees
hr_count = (df["department"] == "HR").sum()

# 3. Print frequency
print("Frequency count for HR department:", hr_count)

# 4. Plot histogram / bar chart of departments
dept_counts = df["department"].value_counts()

fig, ax = plt.subplots()
ax.bar(dept_counts.index, dept_counts.values)

ax.set_title("Department Distribution")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()

# 5. Save plot to HTML
html_file = "employee_histogram.html"
mpld3.save_html(fig, html_file)

# 6. Make sure your email is plain text INSIDE the HTML <body>
email = "24f3002886@ds.study.iitm.ac.in"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

if email not in html:
    # Insert email just before </body> so it's clearly visible
    if "</body>" in html:
        html = html.replace(
            "</body>",
            f"<p>Email: {email}</p></body>"
        )
    else:
        # Fallback: just append it
        html += f"\n<p>Email: {email}</p>\n"

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)

print("Histogram saved as:", html_file)
