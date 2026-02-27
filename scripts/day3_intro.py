"""
Day 3 — Professional Intro Script
Author: Ayushman Saxena
Date: February 28, 2026
Description: Interactive introduction program with formatted output
"""

def main():
    # Display welcome banner
    print("=" * 50)
    print("        PERSONAL INTRODUCTION BUILDER")
    print("=" * 50)
    print()
    
    # Collect user information
    print("Let's build your introduction:\n")
    
    name = input("→ What's your name? ").strip()
    while not name:
        print("  ⚠️  Name cannot be empty. Try again.")
        name = input("→ What's your name? ").strip()
    
    age = input("→ How old are you? ").strip()
    while not age:
        print("  ⚠️  Age cannot be empty. Try again.")
        age = input("→ How old are you? ").strip()
    
    city = input("→ Where are you from? ").strip()
    while not city:
        print("  ⚠️  City cannot be empty. Try again.")
        city = input("→ Where are you from? ").strip()
    
    dream = input("→ What's your dream/goal? ").strip()
    while not dream:
        print("  ⚠️  Dream/goal cannot be empty. Try again.")
        dream = input("→ What's your dream/goal? ").strip()
    
    # Generate and display introduction
    print("\n" + "=" * 50)
    print("           YOUR INTRODUCTION")
    print("=" * 50)
    print()
    print(f"👤 Name:      {name}")
    print(f"🎂 Age:       {age}")
    print(f"📍 Location:  {city}")
    print(f"🎯 Goal:      {dream}")
    print()
    print("─" * 50)
    print(f"\n💬 Hey {name}, {age} from {city}.")
    print(f"   Goal: {dream}. Let's go! 🚀")
    print("\n" + "=" * 50)
    print("✅ Introduction complete!")
    print("=" * 50)

# Entry point
if __name__ == "__main__":
    main()
# function to calculate the sum of two numbers
def calculate_sum(a, b):
    return a + b
