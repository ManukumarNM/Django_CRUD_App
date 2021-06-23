from django.db import models

COURSE_CHOICES = (
    ("Choose", "Choose"),
    ("MCA", "MCA"),
    ("MBA", "MBA"),
    ("MTECH", "MTECH"),
    ("BCA", "BCA"),
    ("BBA", "BBA"),
    ("BE", "BE"),
)
 
SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)
class Students(models.Model):
    student_name = models.CharField(max_length=255)
    student_email = models.EmailField()
    student_address = models.TextField()
    student_course = models.CharField(
        max_length = 7,
        choices = COURSE_CHOICES,
        default = "0"
         )
    student_semester = models.CharField(
        max_length=8,
        choices = SEMESTER_CHOICES,
        default= "1"
        )
    student_mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.student_name

    # class Meta:  
    #     db_table = "crud_students" 