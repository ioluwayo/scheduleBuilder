# Created by Ibukun on 11/18/2016.
from datetime import datetime, date, time

import itertools


class Class:
    def __init__(self, class_id, section_id, day, startime, endtime):
        """

        :param class_id:
        :param section_id:
        :param day:
        :param startime:
        :param endtime:
        """
        self.__class_id = class_id
        self.__section_id = section_id
        self.__starttime = time(startime)
        self.__endtime = time(endtime)
        self.__day = day
        
    def toString(self):
        """

        :return: All atributes of the object as a string
        """
        return str(self.__class_id) + str(self.__section_id) + str(self.__day) + str(self.__starttime.isoformat()) + str(self.__endtime.isoformat())
        
class Section:
    def __init__(self, section_id, course_id):
        """
        
        :param section_id:
        :param course_id:
        """
        self.__section_id = section_id
        self.__course_id = course_id
        self.__classes = []
        
    def addClass(self, classobject):
        """
        
        :param classobject:
        :return: None
        """
        self.classes.append(classobject)
        # each section should have a list of its classes
        
    def getCoureId(self):
        """
        :return: The course ID
        """
        return self.__course_id
    
    def getSectionId(self):
        """
        
        :return: The Section ID
        """
        return self.__section_id
    
    def toString(self):
        """
        
        :return: All atributes of the object as a string
        """
        return str(self.__section_id) + "," + str(self.__course_id)

class Course:
    def __init__(self, course_id, course_code):
        """
        
        :param course_id:
        :param course_code:
        """
        self.__course_id = course_id
        self.__course_code = str(course_code)
        self.__sections = []
        
    def addSection(self, section):
        """
        
        :param section:
        :return: None
        """
        self.sections.append(section)
        #  each course has a list of section objects attached to it.
    
    def getCourseId(self):
        """
        
        :return: The Course ID
        """
        return self.__course_id
    
    def getCourseCode(self):
        """
        :return: The course code
        """
        return self.__course_code
        
    def toString(self):
        """
        :return: All atributes of the object as a string
        """
        return str(self.__course_id) + str(self.__course_code) + str(self.__sections)

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
