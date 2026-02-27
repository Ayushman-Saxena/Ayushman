# Grade checker - taking user marks and giving feedback
# Day 4 practice with if/elif/else

def main():
    print("=" * 50)
    print("        GRADE CHECKER")
    print("=" * 50)
    print()
    
    marks = int(input("Enter your marks (0-100): "))
    
    # checking what grade they got
    if marks >= 90:
        grade = "Excellent"
        message = "Outstanding! Keep it up!"
    elif marks >= 75:
        grade = "Good"
        message = "Great work! Keep pushing!"
    elif marks >= 40:
        grade = "Pass"
        message = "You passed! Practice more."
    else:
        grade = "Fail"
        message = "Don't give up! Let's improve!"
    
    print()
    print("-" * 50)
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"{message}")
    print("-" * 50)

if __name__ == "__main__":
    main()