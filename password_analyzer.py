import string

# Take password input
password = input("Enter Password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check uppercase letters
if any(char.isupper() for char in password):
    score += 1

# Check lowercase letters
if any(char.islower() for char in password):
    score += 1

# Check digits
if any(char.isdigit() for char in password):
    score += 1

# Check special characters
if any(char in string.punctuation for char in password):
    score += 1

# Determine strength
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"

# Display result
print("\nPassword Score:", score)
print("Password Strength:", strength)

# Suggestions
if strength == "Weak":
    print("Suggestion:")
    print("- Use at least 8 characters")
    print("- Add uppercase letters")
    print("- Add numbers")
    print("- Add special characters")

elif strength == "Moderate":
    print("Suggestion:")
    print("- Add more special characters")
    print("- Increase password length")

else:
    print("Excellent Password!")