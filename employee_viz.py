import pandas as pd
import matplotlib.pyplot as plt
import mpld3

EMAIL = "24f3002886@ds.study.iitm.ac.in"
HTML_FILE = "employee_histogram.html"

# 1. Load the dataset
df = pd.read_csv("employee_performance.csv")

# 2. Count HR employees
hr_count = (df["department"] == "HR").sum()
print(f'Frequency count for "HR" department: {hr_count}')

# 3. Create a HISTOGRAM (numeric) – here using performance_score
fig, ax = plt.subplots()
ax.hist(df["performance_score"], bins=10)
ax.set_title("Histogram of Employee Performance Scores")
ax.set_xlabel("Performance Score")
ax.set_ylabel("Frequency")
plt.tight_layout()

# 4. Turn the figure into HTML (SVG + JS)
fig_html = mpld3.fig_to_html(fig)

# 5. Python code (as plain text) to embed inside the HTML
python_code = r"""
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

df = pd.read_csv("employee_performance.csv")

hr_count = (df["department"] == "HR").sum()
print('Frequency count for "HR" department:', hr_count)

fig, ax = plt.subplots()
ax.hist(df["performance_score"], bins=10)
ax.set_title("Histogram of Employee Performance Scores")
ax.set_xlabel("Performance Score")
ax.set_ylabel("Frequency")
plt.tight_layout()

mpld3.save_html(fig, "employee_histogram.html")
"""

# 6. Build a full HTML page with chart + verification info
extra_block = f"""
<hr>
<h2>Verification Information</h2>
<p><b>Email:</b> {EMAIL}</p>
<p>Frequency count for "HR" department: {hr_count}</p>

<h3>Python Code Used</h3>
<pre><code>{python_code}</code></pre>
<hr>
"""

full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Employee Performance Histogram</title>
</head>
<body>
    <h1>Employee Performance Histogram</h1>
    {fig_html}
    {extra_block}
</body>
</html>
"""

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"HTML file written to: {HTML_FILE}")
