# STUDENT GRADE TRACKER
# By: Damian Ciumacenco
# Date: Jul 2025

import json
import os

class GradeTracker:
    def __init__(self):
        self.students = {}
        self.load_data()
    
    def add_student(self, name):
        """Add a new student"""
        if name in self.students:
            print(f"Error: Student '{name}' already exists!")
        else:
            self.students[name] = []
            print(f"Success: Student '{name}' added!")
            self.save_data()
    
    def add_grade(self, name, grade):
        """Add a grade for a student"""
        if name not in self.students:
            print(f"Error: Student '{name}' not found!")
            return
        
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                self.students[name].append(grade)
                print(f"Success: Added grade {grade} for {name}")
                self.save_data()
            else:
                print("Error: Grade must be between 0 and 100")
        except ValueError:
            print("Error: Please enter a valid number")
    
    def calculate_average(self, name):
        """Calculate average grade for a student"""
        if name not in self.students:
            return None
        
        grades = self.students[name]
        if len(grades) == 0:
            return 0
        
        total = 0
        for grade in grades:
            total = total + grade
        
        return total / len(grades)
    
    def get_letter_grade(self, average):
        """Convert numerical grade to letter grade"""
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    def show_student_summary(self, name):
        """Display complete summary for a student"""
        if name not in self.students:
            print(f"Error: Student '{name}' not found!")
            return
        
        grades = self.students[name]
        print("\n" + "="*50)
        print(f"STUDENT SUMMARY: {name}")
        print("="*50)
        
        if len(grades) == 0:
            print("No grades recorded yet.")
        else:
            print(f"Grades: {grades}")
            
            # Calculate average using loop
            total = 0
            for grade in grades:
                total = total + grade
            avg = total / len(grades)
            
            # Get letter grade
            if avg >= 90:
                letter = 'A'
            elif avg >= 80:
                letter = 'B'
            elif avg >= 70:
                letter = 'C'
            elif avg >= 60:
                letter = 'D'
            else:
                letter = 'F'
            
            print(f"Average: {avg:.1f}")
            print(f"Letter Grade: {letter}")
            
            # Find highest
            highest = grades[0]
            for grade in grades:
                if grade > highest:
                    highest = grade
            
            # Find lowest
            lowest = grades[0]
            for grade in grades:
                if grade < lowest:
                    lowest = grade
            
            print(f"Highest: {highest}")
            print(f"Lowest: {lowest}")
            print(f"Total Grades: {len(grades)}")
        
        print("="*50 + "\n")
    
    def show_all_students(self):
        """Display all students and their averages"""
        if len(self.students) == 0:
            print("No students in the system yet.")
            return
        
        print("\n" + "="*50)
        print("ALL STUDENTS SUMMARY")
        print("="*50)
        
        for name in self.students:
            grades = self.students[name]
            
            if len(grades) == 0:
                print(f"{name}: No grades yet")
            else:
                total = 0
                for grade in grades:
                    total = total + grade
                avg = total / len(grades)
                
                if avg >= 90:
                    letter = 'A'
                elif avg >= 80:
                    letter = 'B'
                elif avg >= 70:
                    letter = 'C'
                elif avg >= 60:
                    letter = 'D'
                else:
                    letter = 'F'
                
                print(f"{name}: {avg:.1f}% ({letter}) - {len(grades)} grades")
        
        print("="*50 + "\n")
    
    def class_statistics(self):
        """Show overall class statistics"""
        if len(self.students) == 0:
            print("No students in the system yet.")
            return
        
        all_grades = []
        for name in self.students:
            for grade in self.students[name]:
                all_grades.append(grade)
        
        if len(all_grades) == 0:
            print("No grades recorded yet.")
            return
        
        print("\n" + "="*50)
        print("CLASS STATISTICS")
        print("="*50)
        print(f"Total Students: {len(self.students)}")
        print(f"Total Grades: {len(all_grades)}")
        
        total_sum = 0
        for grade in all_grades:
            total_sum = total_sum + grade
        class_avg = total_sum / len(all_grades)
        print(f"Class Average: {class_avg:.1f}%")
        
        highest = all_grades[0]
        for grade in all_grades:
            if grade > highest:
                highest = grade
        print(f"Highest Grade: {highest}")
        
        lowest = all_grades[0]
        for grade in all_grades:
            if grade < lowest:
                lowest = grade
        print(f"Lowest Grade: {lowest}")
        
        print("="*50 + "\n")
    
    def delete_student(self, name):
        """Delete a student"""
        if name in self.students:
            del self.students[name]
            print(f"Success: Student '{name}' deleted!")
            self.save_data()
        else:
            print(f"Error: Student '{name}' not found!")
    
    def save_data(self):
        """Save data to file"""
        with open('grades_data.json', 'w') as f:
            json.dump(self.students, f)
    
    def load_data(self):
        """Load data from file"""
        if os.path.exists('grades_data.json'):
            with open('grades_data.json', 'r') as f:
                self.students = json.load(f)
            print("Data loaded successfully!")

def main():
    """Main program loop"""
    tracker = GradeTracker()
    
    print("\n" + "="*50)
    print("         STUDENT GRADE TRACKER")
    print("="*50)
    
    while True:
        print("\nMAIN MENU:")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Summary")
        print("4. View All Students")
        print("5. Class Statistics")
        print("6. Delete Student")
        print("7. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            tracker.add_student(name)
        
        elif choice == '2':
            name = input("Enter student name: ")
            grade = input("Enter grade (0-100): ")
            tracker.add_grade(name, grade)
        
        elif choice == '3':
            name = input("Enter student name: ")
            tracker.show_student_summary(name)
        
        elif choice == '4':
            tracker.show_all_students()
        
        elif choice == '5':
            tracker.class_statistics()
        
        elif choice == '6':
            name = input("Enter student name to delete: ")
            tracker.delete_student(name)
        
        elif choice == '7':
            print("\nGoodbye! Data saved.")
            print("Thanks for using Grade Tracker!")
            print("="*50)
            break
        
        else:
            print("Invalid choice. Please enter 1-7.")

# Run the program
if __name__ == "__main__":
    main()