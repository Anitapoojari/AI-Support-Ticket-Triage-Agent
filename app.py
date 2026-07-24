import pandas as pd
from classifier import classify_ticket

# Read tickets from CSV
df = pd.read_csv("tickets.csv")

# Store results
results = []

# Process each ticket
for index, row in df.iterrows():
    category, priority, team, confidence = classify_ticket(
        row["Subject"], row["Description"]
    )

    results.append({
        "Subject": row["Subject"],
        "Description": row["Description"],
        "Category": category,
        "Priority": priority,
        "Team": team,
        "Confidence": confidence
    })

# Create DataFrame
output_df = pd.DataFrame(results)

# Save to CSV
output_df.to_csv("output.csv", index=False)

# Display results
print("\n===== Support Ticket Triage Results =====\n")
print(output_df)

print("\n✅ Output saved as output.csv")