"""Student marks calculator (improved version).

Takes a student's name and subject marks, then prints the average,
grade, highest and lowest marks.
"""

GRADE_BOUNDARIES = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]


def calculate_average(marks):
    """Return the average of a non-empty list of marks."""
    if not marks:
        raise ValueError("At least one mark is required.")
    return sum(marks) / len(marks)


def get_grade(average):
    """Return the letter grade for an average score."""
    for minimum, grade in GRADE_BOUNDARIES:
        if average >= minimum:
            return grade
    return "F"


def read_int(prompt, minimum=0, maximum=None):
    """Keep asking until the user enters a valid whole number."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value < minimum or (maximum is not None and value > maximum):
            limit = f"between {minimum} and {maximum}" if maximum is not None else f"at least {minimum}"
            print(f"Value must be {limit}.")
            continue
        return value


def main():
    name = input("Enter student name: ").strip()
    subject_count = read_int("How many subjects? ", minimum=1)
    marks = [read_int(f"Marks for subject {i} (0-100): ", 0, 100)
             for i in range(1, subject_count + 1)]

    average = calculate_average(marks)
    print(f"\nReport for {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {get_grade(average)}")
    print(f"Highest: {max(marks)} (subject {marks.index(max(marks)) + 1})")
    print(f"Lowest: {min(marks)} (subject {marks.index(min(marks)) + 1})")


if __name__ == "__main__":
    main()
