import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Load dataset
df = pd.read_csv("employee_performance.csv")

# Count HR employees
hr_count = (df["department"] == "HR").sum()
print("Frequency count for HR department:", hr_count)

# Force numeric conversion for histogram
df["department_code"] = df["department"].astype("category").cat.codes

# Create HISTOGRAM (not bar chart)
plt.figure()
plt.hist(df["department_code"], bins=len(df["department"].unique()))
plt.title("Histogram of Departments")
plt.xlabel("Department (Encoded)")
plt.ylabel("Frequency")

# Save chart to HTML
html = mpld3.fig_to_html(plt.gcf())

# Python code text to embed inside HTML
python_code = """
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

df = pd.read_csv("employee_performance.csv")

hr_count = (df["department"] == "HR").sum()
print("Frequency count for HR department:", hr_count)

df["department_code"] = df["department"].astype("category").cat.codes

plt.hist(df["department_code"], bins=len(df["department"].unique()))
plt.title("Histogram of Departments")
plt.xlabel("Department (Encoded)")
plt.ylabel("Frequency")

mpld3.save_html(plt.gcf(), "employee_histogram.html")
"""

email = "24f3002886@ds.study.iitm.ac.in"

# Embed everything
embed = f"""
<hr>
<h2>Verification Block</h2>
<p>Email: {email}</p>
<p>Frequency count for "HR" department: {hr_count}</p>

<h3>Python Code Used</h3>
<pre><code>{python_code}</code></pre>
<hr>
"""

# Inject into HTML body
if "</body>" in html:
    html = html.replace("</body>", embed + "</body>")
else:
    html += embed

# Save final HTML
with open("employee_histogram.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML file created with histogram and code inside.")
