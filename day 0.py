# 1. Functions & Parameters
def calculate_stipend(base_salary, bonus_percent):
    """Calculates final salary with bonus."""
    bonus_amount = base_salary * (bonus_percent / 100)
    return base_salary + bonus_amount

# 2. Lists & Dictionaries (Data Handling)
# In an internship, you will handle data like this:
intern_data = {
    "name": "Santhosh",
    "skills": ["Python", "C++", "PHP", "Bootstrap"],
    "base_pay": 10000,
    "completed_tasks": 5
}

# 3. Logic & Conditionals
print(f"Checking status for: {intern_data['name']}")

if intern_data["completed_tasks"] >= 5:
    performance_bonus = 10  # 10% bonus
    status = "Exceeded Expectations"
else:
    performance_bonus = 0
    status = "In Progress"

# 4. Using the Function
final_salary = calculate_stipend(intern_data["base_pay"], performance_bonus)

# 5. Loops (Iterating through data)
print(f"Intern Status: {status}")
print("Skills to showcase in interview:")
for skill in intern_data["skills"]:
    print(f"- {skill}")

print(f"\nEstimated Stipend: ₹{final_salary}")
