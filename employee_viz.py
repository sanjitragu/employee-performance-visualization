"""
Employee Performance Visualization
Email: 24f3002886@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Python code as string (to embed inside HTML)
python_code = """
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Load dataset
df = pd.read_csv("employee_performance.csv")

# Count HR employees
hr_count = (df["department"] == "HR").sum()
print("Frequency count for HR department:", hr_count)

# Create histogram / bar chart
dept_counts = df["department"].value_counts()
plt.bar(dept_counts.index, dept_counts.values)
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()

# Save visualization as HTML
import mpld3
mpld3.save_html(plt.gcf(), "employee_histogram.html")
"""

# 1. Load the dataset
df = pd.read_csv("employee_performance.csv")

# 2. Count HR department
hr_count = (df["department"] == "HR").sum()
print("Frequency count for HR department:", hr_count)

# 3. Create plot
dept_counts = df["department"].value_counts()
fig, ax = plt.subplots()
ax.bar(dept_counts.index, dept_counts.values)
ax.set_title("Department Distribution")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()

# 4. Convert chart to HTML
html = mpld3.fig_to_html(fig)

email = "24f3002886@ds.study.iitm.ac.in"

# 5. Embed email + Python code into HTML
embed_block = f"""
<hr>
<h2>Verification Information</h2>
<p><b>Email:</b> {email}</p>

<h3>Python Code Used</h3>
<pre><code>
{python_code}
</code></pre>
<hr>
"""

# Inject into HTML body
if "</body>" in html:
    html = html.replace("</body>", embed_block + "</body>")
else:
    html += embed_block

# 6. Write final HTML
with open("employee_histogram.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML file with chart, email and Python code saved successfully.")
