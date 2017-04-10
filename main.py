# Created by ioluwayo on 2017-04-06.
import itertools
import psycopg2
from school import Schedule
from filter import containsUniqueID
from school import cur

def main():

    cur.execute("SELECT * from Courses;")
    allAvailableCourses = cur.fetchall()
    print "All courses in the database: ",allAvailableCourses
    id_of_all_available_courses = [i[0] for i in allAvailableCourses]
    coursesSelected = [1,10]
    id_of_courses = filter(lambda course: course in coursesSelected, id_of_all_available_courses)
    print "The courses wanted by user: ", id_of_courses # maybe we could query sections directly using user input
    # we have just the courses the user wants, lets get the classes of open sections for this courses
    cur.execute("SELECT course_id, section_id from Sections where course_id in ("+','.join(str(n) for n in
                                                                                           id_of_courses)+ ")and " \
                                                                                                        "available = " \
                                                                                                 "TRUE ")
    rows = cur.fetchall()
    print "sections of courseses wanted ", rows
    list_containing_all_possible_section_arrangements = list(itertools.combinations(rows, len(id_of_courses)))
    print list_containing_all_possible_section_arrangements
    possibleSchedules =  filter(containsUniqueID, list_containing_all_possible_section_arrangements)
    print "These are the possible schedules"
    ValidSchedules = []
    for i in possibleSchedules:
        schedule = Schedule(i)
        if schedule.isValid():
            ValidSchedules.append(schedule)
    for i in ValidSchedules:
        i.display()
    print "There are %d valid schedules"%len(ValidSchedules)
main()