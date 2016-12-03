# Created by Ibukun on 11/18/2016.
from datetime import datetime, date, time

import itertools


class Class:
    def __init__(self, class_id, section_id, day, startime, endtime):
        self.class_id = class_id
        self.section_id = section_id
        self.starttime = time(startime)
        self.endtime = time(endtime)
        self.day = day
        
    def to_string(self):
        string_format = str(self.class_id) + str(self.section_id) + str(self.day) + str(self.starttime.isoformat()) + str(self.endtime.isoformat())
        return string_format
        ####
        
class Section:
    def __init__(self, section_id, course_id):
        self.section_id = section_id
        self.course_id =course_id
        self.classes = []
        
    def add_class(self, classobject):
        self.classes.append(classobject)
        
    def to_string(self):
        string_format = str(self.section_id) + "," + str(self.course_id)
        return string_format
        # each section should have a list of its classes


class Course:
    def __init__(self, course_id, course_code):
        self.course_id = course_id
        self.course_code = str(course_code)
        self.sections = []
        
    def add_section(self, section):
        self.sections.append(section)
        #  each course has a list of section objects attached to it.
        
    def to_string(self):
        string_format = str(self.course_id) + str(self.course_code) + str(self.sections)
        return string_format


class Filter:
    def __init__(self,list1):
        #each element of this list is itself a list of sections
        self.list1 = list1

    def listOfAvailableSchedules(self):
        #get permutations
        list_containing_all_possible_section_arrangement = itertools.combinations(list)

        return filter(self.contains_unique_id(), list_containing_all_possible_section_arrangement)
        #  we need to take this result and further filter it this time ensuring that the times dont clash
        #filtered_list = filter(self.contains_unique_id(), list_containing_all_possible_section_arrangement)

    def containsUniqueID(self, list1):
        course_id_list = [i.course_id for i in list1]
        duplicate_free_list = list(set(course_id_list))

        if len(duplicate_free_list) == len(list):
            return True
        else:
            return False

