import psycopg2
import itertools
from school import *
# Created by Ibukun on 11/7/2016.


def remove_sections_of_unwanted_courses(sec, wanted_courses):
    result = []
    for sec in sec:
        if sec[1] in wanted_courses:
            result.append(sec[0])
    return result


def all_sections_have_unique_id(sec):
    for i in range(len(sec)):
        if i == len(sec)-1:
            return True
        if sec[i] in sec[i+1:]:
            return False
    return True

try:
    conn = psycopg2.connect("dbname = rec host= localhost password = admin user = postgres")
except psycopg2.Error as e:
    print e.pgerror, "COULD NOT ESTABLISH CONNECTION"
cur = conn.cursor()


# ----courses-----
cur.execute("SELECT * from Courses;")
courses = cur.fetchall()
del(courses[2:5])
id_courses_wanted = []
for course in courses:
    id_courses_wanted.append(course[0])
    
      
#  CREATE COURSE OBJECTS FROM THOSE IN DATABASE....IDEALY IT SHOULD BE FROM THOSE SECTED BY USER.
course_objects = []
for course in courses:
    course_objects.append(Course(course[0], course[1]))
for i in range(len(course_objects)):
    print course_objects[i].toString()

# ----sections------
cur.execute("""SELECT * from Sections WHERE open = TRUE""")
sections = cur.fetchall()
print "\n\tAll open Sections in Database\n"
for section in sections:
    print "\t", section
    
first_filtered_sections_id = remove_sections_of_unwanted_courses(sections, id_courses_wanted)

# CREATE OBJECTS OF OPEN SECTIONS IN DATABASE.
section_objects = []
for section in sections:
    section_objects.append(Section(section[0], section[1]))
for i in range(len(section_objects)):
    print section_objects[i].toString()


print "\n\tID of Sections of only courses wanted\n"
for i_d in first_filtered_sections_id:
    print "\t", i_d
    
section_combination = itertools.combinations(first_filtered_sections_id, 4)
print "--------------------------------------------"
num = 0
print "\tCombination of all possible sections"
for combination in section_combination:
    num += 1
    print "\t", combination
print "--------------------------------------------"
print num
print "--------------------------------------------"
print"we have section list based on requested course. we need to remove combinations that have more than 1" \
     "section with the same course id. we might use some type of for loop"


     
# # ------classes------
# cur.execute("""SELECT * from Classes""")
# classes = cur.fetchall()
# print "\nShow me the classes:\n"
# for classes in classes:
#     print " ", classes

#listofcourse = []
#for courses in courses:
   # onecourse = CourseClass(courses[0], courses[1])
    #listofcourse.append(onecourse)