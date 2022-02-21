

def canFinish(numCourses, prerequisites):
    # We create a dictionary where the key is the course
    # And the value is the prerequisite
    preMap = { i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
    
    visitSet = set()
    def dfs(crs):
        # This means that we have already visited this course.
        # We return false
        if crs in visitSet:
            return False
        # This means there is no prerequisite for this course.
        # We return true
        if preMap[crs] == []:
            return True
        # Add the course in the visited set of courses
        visitSet.add(crs)
        # DFS Algorithm
        for pre in preMap[crs]:
            # If we get false once, we can return false
            if not dfs(pre):
                return False
        
        visitSet.remove(crs)
        preMap[crs] = []
        return True
    
    for crs in range(numCourses):
        if not dfs(crs): 
            return False
    return True
    
numCourses, prerequisites = 3,[[0,1],[0,1],[0,1]]
canFinish(numCourses, prerequisites)



def canFinish(numCourses, prerequisites):
    preMap = {}
    for i in range(numCourses):
        preMap[i] = []
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
    visitSet = set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visitSet.remove(crs)
        preMap[crs] = []
        return True
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True






def canFinish(numCourses, prerequisites):
    preMap = {}
    for i in range(numCourses):
        preMap[i] = []
    for crs, pre in prerequisites:
        preMap[crs] = pre
    visitSet = set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] in visitSet == []:
            return True
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visitSet.remove(crs)
        preMap[crs] = []
        return True
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True




preMap = {}
visitSet = set()
def dfs(crs):
    if crs in visitSet:
        return False
    if preMap[crs] in visitSet == []:
        return True
    for pre in preMap[crs]:
        if not dfs(pre):
            return False
    visitSet.remove(crs)
    preMap[crs] = []
    return True