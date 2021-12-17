# COMP3311 21T3 Ass2 ... Python helper functions
# add here any functions to share between Python scripts 
# you must submit this even if you add nothing

def getProgram(db,code):
  cur = db.cursor()
  cur.execute("select * from Programs where code = %s",[code])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

def getStream(db,code):
  cur = db.cursor()
  cur.execute("select * from Streams where code = %s",[code])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

def getStudent(db,zid):
  cur = db.cursor()
  qry = """
  select p.*, c.name
  from   People p
         join Students s on s.id = p.id
         join Countries c on p.origin = c.id
  where  p.id = %s
  """
  cur.execute(qry,[zid])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info
def getCourse(db,code):
  cur = db.cursor()
  qry = """
  select code, name, uoc 
  from   subjects s
  where  s.code = %s
  """
  cur.execute(qry,[code])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info
def getRule(db, rule):
  cur = db.cursor()
  query = """
  select r.min_req, r.max_req, r.type, a.name, a.type, a.defby, a.definition
  from rules r
    join academic_object_groups a on (r.ao_group = a.id)
  where r.id = %s
  order by r.id
  """
  cur.execute(query, [rule])
  info = cur.fetchone()
  cur.close()
  if not info:
    return None
  else:
    return info

def notCompleted(rule):
  if rule['type'] == 'CC':
    if rule['courses'] == []:
      return False
    return True
  if rule['maxUoc'] is not None and rule['maxUoc'] > rule['completedUoc']:
    return True
  if rule['minUoc'] is not None and rule['minUoc'] > rule['completedUoc']:
    return True  
  return False
def printCC(courses, cur):
  query = """
  select name from subjects
  where code like %s
  """
  for subject in courses: 
    if subject[0] == '{':
      #Remove first and last character
      subject = subject[1:-1]
      #For every tuple item
      firstTime = True
      for subjectChoice in subject.split(';'):
        cur.execute(query, [subjectChoice])
        subjectName = cur.fetchone()
        #If no name found
        if subjectName is None:
          if firstTime:
            print(f'- {subjectChoice} ???')
            firstTime = False
          else:
            print(f'  or {subjectChoice} ???')
        # If its first iteration
        if firstTime:
          print(f'- {subjectChoice} {subjectName[0]}')
          firstTime = False
        else:
          print(f'  or {subjectChoice} {subjectName[0]}')
    else:       
      cur.execute(query, [subject])
      subjectName = cur.fetchone()
      if subjectName is None:
        print(f'- {subject} ???')
      else:
        print(f'- {subject} {subjectName[0]}')
def printPE(minUoc, maxUoc, completedUoc, name):
  if (minUoc is None and maxUoc is None):
      print(f'{minUoc - completedUoc} courses from {name}')
  if (minUoc is None and maxUoc is not None):  
    print(f'up to {maxUoc - completedUoc} UOC courses from {name}')
  if (minUoc is not None and maxUoc is None):  
      print(f'at least {minUoc - completedUoc} UOC courses from {name}')

  if (minUoc is not None and maxUoc is not None):
    if (minUoc == maxUoc):  
      print(f'{maxUoc - completedUoc} UOC from {name}')
    else:
      print(f'between {minUoc - completedUoc} and {maxUoc - completedUoc} UOC courses from {name}')
def canGraduate(rules):
  for rule in rules:
    if notCompleted(rules[rule]):
      return False
  return True
def sortSubjectRule(minUoc, maxUoc, typeCode, name, types, defby, definition, cur):
  if (minUoc is None and maxUoc is None):
    if (len(definition) > 1):
      print(f'all courses from {name}')
    else:
      print(name)
  if (minUoc is None and maxUoc is not None):  
    print(f'up to {maxUoc} UOC courses from {name}')

  if (minUoc is not None and maxUoc is None):  
    if (typeCode == 'FE'):
      print(f'at least {minUoc} UOC of Free Electives')
    else:
      print(f'at least {minUoc} UOC courses from {name}')

  if (minUoc is not None and maxUoc is not None):
    if (minUoc == maxUoc):
      if (typeCode == 'FE'):
        print(f'{maxUoc} UOC from {name}')
      elif typeCode == 'PE':
        print(f'{maxUoc} UOC courses from {name}')
      elif typeCode == 'GE':
        print(f'{maxUoc} UOC of {name}') 
    else:
      print(f'between {minUoc} and {maxUoc} UOC courses from {name}')

  if defby == 'pattern':
    if definition[0] == "FREE####" or definition[0] == "GEN#####":
      return
    print(f"- courses matching {','.join(definition)}")
  else :
    query = """
        select name from subjects
        where code like %s
        """
    for subject in definition:
      # If its wrapped in tuple
      if subject[0] == '{':
        #Remove first and last character
        subject = subject[1:-1]
        #For every tuple item
        firstTime = True
        for subjectChoice in subject.split(';'):
          cur.execute(query, [subjectChoice])
          subjectName = cur.fetchone()
          #If no name found
          if subjectName is None:
            if firstTime:
              print(f'- {subjectChoice} ???')
              firstTime = False
            else:
              print(f'  or {subjectChoice} ???')
          # If its first iteration
          if firstTime:
            print(f'- {subjectChoice} {subjectName[0]}')
            firstTime = False
          else:
            print(f'  or {subjectChoice} {subjectName[0]}')
      else :
        cur.execute(query, [subject])
        subjectName = cur.fetchone()
        if subjectName is None:
          print(f'- {subject} ???')
        else:
          print(f'- {subject} {subjectName[0]}')

def sortStreamRule(minUoc, maxUoc, typeCode, name, types, defby, definition, cur):
  print(f'{minUoc} stream(s) from {name}')
  for stream in definition:
    query = """
    select name from streams
    where code like %s
    """
    cur.execute(query, [stream])
    streamName = cur.fetchone()
    if streamName is not None:
      print(f'- {stream} {streamName[0]}')
    else:
      print(f'- {stream} ???')