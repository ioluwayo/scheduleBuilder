# Created by Ibukun on 11/18/2016.
import psycopg2

try:
    conn = psycopg2.connect("dbname = mydb host= localhost password = 0  user = ioluwayo")
except psycopg2.Error as e:
    print e.pgerror, "COULD NOT ESTABLISH CONNECTION"
cur = conn.cursor()

class Schedule:
    def __init__(self,sections):
        self.__sections = dict(sections)
        cur.execute("SELECT * from Classes WHERE section_id in (" + ','.join(str(n) for n in self.getIdOfSections()) +
                    ")")
        self.__classes = []
        rows = cur.fetchall()
        for row in rows:
            cl_id, s_id, c_type, day, start, end = row
            self.__classes.append(Class(cl_id, s_id, c_type, day, start, end))
        self.__nsections = len(self.__sections)
        self.__nclasses = len(self.__classes)
        self.__valid = self.validate()
    def getIdOfSections(self):
        return self.__sections.values()
    def getIdOfCourses(self):
        return self.__sections.keys()
    def getClasses(self):
        return self.__classes
    def numberOfClasses(self):
        return self.__nclasses
    def numberOfSections(self):
        return self.__nsections
    def isValid(self):
        return self.__valid
    def validate(self):
        for i in xrange(len(self.__classes)):
            #print "h", self.__classes[i].toString()
            for j in xrange(i+1, len(self.__classes)):
                if self.__classes[i].hasTimeConflict(self.__classes[j]):
                    #print "n", self.__classes[j].toString()
                    return False # once any of the classes give us a conflict we stop iterating.
        return True
    def display(self):
        print "\tcourses in this schedule:", self.getIdOfCourses()
        print "\tSections in this schedule:", self.getIdOfSections()
        print "\tValid schedule:",self.__valid
        for i in self.__classes:
            i.display()
        print
        return


class Class:
    def __init__(self, class_id, section_id, class_type, day, startime, endtime):
        """

        :param class_id:
        :param section_id:
        :param day:
        :param startime:
        :param endtime:
        """
        self.__class_id = class_id
        self.__section_id = section_id
        self.__class_type = class_type
        self.__startime = startime
        self.__endtime = endtime
        self.__day = day
    def getDay(self):
        return self.__day
    def getClassId(self):
        return self.__class_id
    def getSectionId(self):
        return self.__section_id
    def getStartTime(self):
        return self.__startime
    def getEndTime(self):
        return self.__endtime
    def getClassType(self):
        return self.__class_type
    def display(self):
        print "\t",self.getSectionId(),self.getClassId(),self.getClassType(),self.getDay(),self.getStartTime(),\
            self.getEndTime()
    def toString(self):
        """

        :return: All atributes of the object as a string
        """
        return str(self.__class_id), str(self.__section_id), str(self.__day), str(self.__startime.isoformat()), \
               str(self.__endtime.isoformat())
    def hasTimeConflict(self, otherClass):
        if otherClass.getDay() != self.getDay(): #they happen on different days
            return False

        start = otherClass.getStartTime()
        end =  otherClass.getEndTime()
        if start >= self.__endtime or self.__startime >= end:
            return False # the other class starts after this class ends or when it ends
        return True # all other cases imply time conflicts


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
        
    def getCourseId(self):
        """
        :return: The course ID
        """
        return self.__course_id
    
    def getSectionId(self):
        """
        
        :return: The Section ID
        """
        return self.__section_id

    def getClasses(self):
        """

        :return: the list of classes for this section
        """
        return self.__classes
    
    def toString(self):
        """
        
        :return: All atributes of the object as a string
        """
        return str(self.__section_id) + "," + str(self.__course_id)


class Course:
    def __init__(self, course_id, course_code, course_description):
        """
        
        :param course_id:
        :param course_code:
        """
        self.__course_id = course_id
        self.__course_code = str(course_code)
        self.__course_description = course_description
        self.__sections = self.getSectionsFromDB()
    def getSectionsFromDB(self):

        return ["sections"]
        
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

    def getCourseDescription(self):
        """

        :return: The course description
        """
        return self.__course_description

    def getCourseSections(self):
        """

        :return: a list of section objects that belong to this course
        """
        return self.__sections

    def toString(self):
        """
        :return: All attributes of the object as a string
        """
        return str(self.__course_id) + str(self.__course_code) + str(self.__sections)
