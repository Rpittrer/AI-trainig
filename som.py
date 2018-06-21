import main

a=10
b =190
print(main.add(90,b))

print("number is: " + str(a))

def build_profile(first, last, **user_info):
 """Build a user's profile dictionary."""
 # Build a dict with the required keys.
 profile = {'first': first, 'last': last}
 # Add any other keys and values.
 for key, value in user_info.items():
 profile[key] = value
 return profile
# Create two users with different kinds
# of information.
user_0 = build_profile('albert', 'einstein',
 location='princeton')
user_1 = build_profile('marie', 'curie',
 location='paris', field='chemistry')
print(user_0)
print(user_1)