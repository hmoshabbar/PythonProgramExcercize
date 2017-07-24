print "........WELCOME TO RESULT PORTAL........."
import time
name={
   
  
   "Moshabbar": [
      "...........Moshabbar::Marksheet...............",
      "PHYSICS::78",
      "CHEMISTRY::90",
      "MATHEMATICS::78",
      "BIOLOGY::67",
      "ENGLISH::71",
      "HINDI::89",
      "...................................",
      "Total::473",
      "Percentage::78.83%",
      "Result:Passed with First Class"
   ],

   "Rahul": [
      "...........Rahul::Marksheet...............",
      "PHYSICS::71",
      "CHEMISTRY::80",
      "MATHEMATICS::78",
      "BIOLOGY::67",
      "ENGLISH::71",
      "HINDI::50",
      "...................................",
      "Total::417",
      "Percentage::69.5%",
      "Result:Passed with First Class"
   ],

   "Ashu": [
      "...........Ashu::Marksheet...............",
      "PHYSICS::89",
      "CHEMISTRY::90",
      "MATHEMATICS::88",
      "BIOLOGY::77",
      "ENGLISH::71",
      "HINDI::99",
      "...................................",
      "Total::514",
      "Percentage::85.66%",
      "Result:Passed with First Class with Distinction"
   ],
   
   "Ameer": [
      "...........Ameer::Marksheet...............",
      "PHYSICS::89",
      "CHEMISTRY::90",
      "MATHEMATICS::88",
      "BIOLOGY::77",
      "ENGLISH::71",
      "HINDI::99",
      "...................................",
      "Total::514",
      "Percentage::85.66%",
      "Result:Passed with First Class with Distinction"
   ],
   "Irshad": [
      "...........Irshad::Marksheet...............",
      "PHYSICS::79",
      "CHEMISTRY::55",
      "MATHEMATICS::67",
      "BIOLOGY::77",
      "ENGLISH::71",
      "HINDI::67",
      "...................................",
      "Total::416",
      "Percentage::69.33%",
      "Result:Passed with First Class"
   ],
   "Resmi": [
      "...........Resmi::Marksheet...............",
      "PHYSICS::35",
      "CHEMISTRY::40",
      "MATHEMATICS::38",
      "BIOLOGY::47",
      "ENGLISH::31",
      "HINDI::59",
      "...................................",
      "Total::250",
      "Percentage::41.66%",
      "Result:Passed with Third Class"
   ],
   "Haidar": [
      "...........Haider::Marksheet...............",
      "PHYSICS::49",
      "CHEMISTRY::50",
      "MATHEMATICS::68",
      "BIOLOGY::37",
      "ENGLISH::51",
      "HINDI::59",
      "...................................",
      "Total::314",
      "Percentage::52.33%",
      "Result:Passed with Second Class"
   ]
    
}
## If you want to get data from database and want Result just connect with database and .....coding like below...
student_name=raw_input(str("Enter your Name:"))
if(student_name=="Moshabbar" or student_name=="Rahul" or student_name=="Ashu" or student_name=="Ameer"
   or student_name=="Irshad" or student_name=="Resmi" or student_name=="Haidar"):
    if(student_name=="Moshabbar"):
        #print name["Moshabbar"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Moshabbar"]:
            
            
            print result
    elif(student_name=="Rahul"):
        #print name["Rahul"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Rahul"]:
            print result
    elif(student_name=="Ashu"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Ashu"]:
            print result

    elif(student_name=="Ameer"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Ameer"]:
            print result
    elif(student_name=="Irshad"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Irshad"]:
            print result
    elif(student_name=="Haider"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Haider"]:
            print result
            
    elif(student_name=="Resmi"):
        #print name["Ashu"]
        print "Please Wait Result is Searching......"
        time.sleep(10)
        for result in name["Resmi"]:
            print result        
            

            
else:
    print "You Entered Name is not Matching"
