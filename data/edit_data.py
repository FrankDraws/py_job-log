import json

# Load data from JSON file
with open('data.json', 'r') as file:
    job_data = json.load(file)

# Define search criteria (replace with your logic)
company_to_edit = "Universal Destinations & Experiences"  # Update this with the company name you want to edit

# Find the job application to edit
for job in job_data:
    if job['company'] == company_to_edit:
        job_to_edit = job
        break  # Exit the loop after finding a match

# Check if a match was found
if job_to_edit:
    # Modify specific fields
    job_to_edit['position'] = "Senior Technologist"  # Update these with desired changes
    job_to_edit['description'] = "With ATI/R&D at UniCreative."

    # Write updated data back to JSON file
    with open('data.json', 'w') as file:
        json.dump(job_data, file, indent=4)

    print(f"Job application for '{company_to_edit}' edited successfully!")
else:
    print(f"Job application with company '{company_to_edit}' not found.")
