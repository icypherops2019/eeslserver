"""
Models defining the school data
"""
from django.db import models
from hbook.users.models import User2

class School(models.Model):
    """
    Schools owner, name, details (blank currently)
    """
    owner = models.ForeignKey(User2, related_name='created_schools', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    """
    A user may have more than one Student account
    roll_number, school, auth(user), details(blank currently)
    """
    roll_number = models.CharField(max_length=15)
    name = models.CharField(max_length=40, null=True, blank=True)
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)
    auth = models.ForeignKey(User2, on_delete=models.CASCADE, related_name='student_profiles')
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    """
    Same as student but with different name-properties
    """
    roll_number = models.CharField(max_length=15)
    name = models.CharField(max_length=40, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    auth = models.ForeignKey(User2, on_delete=models.CASCADE, related_name='teacher_profiles')
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class ClassGroup(models.Model):
    """
    Containing a list of groups of students with a mentor (teacher_incharge)
    """
    school = models.ForeignKey(School, related_name='class_groups', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='class_groups')#, on_delete=models.CASCADE)
    teacher_incharge = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes_incharged_with')
    name = models.CharField(max_length=20, null=True, blank=True)
    details = models.TextField(null=True, blank=True, help_text="Save timetable here in json along with other details")
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    """
    Name of subject, Time alloted in minutes to make timetable
    """
    name = models.CharField(max_length=40)
    time_alloted = models.PositiveIntegerField(default=0, help_text="Time alloted in minutes")
    max_consecutive_time = models.PositiveIntegerField(default=0)
    min_consecutive_time = models.PositiveIntegerField(default=0)
    class_groups_assigned = models.ManyToManyField(ClassGroup, related_name='subjects')#, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Period(models.Model):
    """
    Times a student gets attendance
    """
    class_group = models.ForeignKey(ClassGroup, related_name='periods', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='periods')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='periods')
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    students_present = models.ManyToManyField(Student, related_name='periods_attended')#, on_delete=models.CASCADE)

    def __str__(self):
        return self.from_time + ' ' + self.to_time

