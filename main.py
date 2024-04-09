# Using f-string for conditional formatting in Python

my_str = 'bobbyhadz.com'

# ✅ f-string formatting with a condition

result = f'Result: {my_str.upper() if len(my_str) > 1 else my_str.capitalize()}'
print(result)  # 👉️ Result: BOBBYHADZ.COM