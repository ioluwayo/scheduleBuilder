def containsUniqueID(listOfsections):
    courseIds = [i[0] for i in listOfsections] # we need to use the course IDs to determine if sections from
        # different courses.
    #print courseIds
    numberOfUniqueCoursesInList= len(set(courseIds)) # set removes duplicates.
    #print numberOfUniqueCoursesInList
    if numberOfUniqueCoursesInList == len(listOfsections): # means the list has only unique courses
        return True
    else:
        return False