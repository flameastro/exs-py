# ex234: Create a class SoftwareEngineer with "name", "age" and "skills" with parameter. Create a method "about" which says about the Software Engineer
class SoftwareEngineer:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills

    def about(self):
        print(f"{self.name} is a Software Enginner, with {self.age} years old. He/She has the skills: {", ".join(self.skills)}")


if __name__ == "__main__":
    user001 = SoftwareEngineer("Flame", 34, ["Python", "JavaScript", "HTML", "CSS", "C", "C++", "Linux", "PowerShell", "Git", "GitHub", "Java", "Arduino", "Rapsberry PI"])
    user001.about()  # Flame is a Software Enginner, with 34 years old. He/She has the skills: Python, JavaScript, HTML, CSS, C, C++, Linux, PowerShell, Git, GitHub, Java, Arduino, Rapsberry PI

    user002 = SoftwareEngineer("Julia", 25, ["HTML", "CSS", "React", "Vue", "Tailwind", "Bootstrap", "Git", "GitHub", "JavaScript", "SQL"])
    user002.about()  # Julia is a Software Enginner, with 25 years old. He/She has the skills: HTML, CSS, React, Vue, Tailwind, Bootstrap, Git, GitHub, JavaScript, SQL
