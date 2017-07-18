import time
loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while loop == 1:
    #print what options you have
    
    print "..............WELCOME TO RESULT PORTAL....................... "

    print "Which Semistar  Result you want "
    print " "
    print "1) B.Tech 1st Sem"
    print "2) B.Tech 2nd Sem"
    print "3) B.Tech 3rd Sem"
    print "4) B.Tech 4th Sem"
    print "5) B.Tech 5th Sem"
    print "6) B.Tech 6th Sem"
    print "7) B.Tech 7th Sem"
    print "8) B.Tech 8th Sem"
    
    print "5) Quit Result Portal..."
    print " "
    
    # to choice Your Option...
    
    choice = input("Choose your option: ")
    
    # Mark for subject use
    if (choice==1):
        print "Ok You Want B.Tech 1st Sem Result "
        name=raw_input("Enter Your Name:")
        sub1=float(input("Enter your sub1 mark:"))
        sub2=float(input("Enter Your sub2 Mark:"))
        sub3=float(input("Enter your sub3 mark:"))
        sub4=float(input("Enter Your sub4 Mark:"))
        sub5=float(input("Enter your sub5 mark:"))
        sub6=float(input("Enter Your sub6 Mark:"))
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        
        # for invalid Mark Purpose Codings...
        
        if(sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub6>100):
            if(sub1>100):
                print "You Enterted Sub1 Mark is not Valid Please Enter a Valid Mark"
            if(sub2>100):
                print "You Enterted Sub2 Mark is not Valid Please Enter a Valid Mark"
            if(sub3>100):
                print "You Enterted Sub3 Mark is not Valid Please Enter a Valid Mark"
            if(sub4>100):
                print "You Enterted Sub4 Mark is not Valid Please Enter a Valid Mark"
            if(sub5>100):
                print "You Enterted Sub5 Mark is not Valid Please Enter a Valid Mark" 
            else:
                print "You Enterted Sub6 Mark is not Valid Please Enter a Valid Mark"  
        elif(sub1<30 or sub2<30 or sub3<30 or sub4<30 or sub5<30 or sub6<30):
            if(sub1<30 and sub2>=30 and sub3>=30 and sub4>=30 and sub5>=30 and sub6>=30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub2 Mark=",sub2, "P"
                print "Your Sub3 Mark=",sub3, "P"
                print "Your Sub4 Mark=",sub4, "P"
                print "Your Sub5 Mark=",sub5, "P"
                print "Your Sub6 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "One Backlock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            
            if(sub1<30 and sub2<30 and sub3>=30 and sub4>=30 and sub5>=30 and sub6>=30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub2 Mark=",sub2, "F"
                print "Your Sub3 Mark=",sub3, "P"
                print "Your Sub4 Mark=",sub4, "P"
                print "Your Sub5 Mark=",sub5, "P"
                print "Your Sub6 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
                
            if(sub1<30 and sub2>=30 and sub3<30 and sub4>=30 and sub5>=30 and sub6>=30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub2 Mark=",sub2, "P"
                print "Your Sub3 Mark=",sub3, "F"
                print "Your Sub4 Mark=",sub4, "P"
                print "Your Sub5 Mark=",sub5, "P"
                print "Your Sub6 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            if(sub1<30 and sub2>=30 and sub3>=30 and sub4<30 and sub5>=30 and sub6>=30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub2 Mark=",sub2, "P"
                print "Your Sub3 Mark=",sub3, "P"
                print "Your Sub4 Mark=",sub4, "F"
                print "Your Sub5 Mark=",sub5, "P"
                print "Your Sub6 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            if(sub1<30 and sub2>=30 and sub3>=30 and sub4>=30 and sub5<30 and sub6>=30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub2 Mark=",sub2, "P"
                print "Your Sub3 Mark=",sub3, "P"
                print "Your Sub4 Mark=",sub4, "P"
                print "Your Sub5 Mark=",sub5, "F"
                print "Your Sub6 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            else:
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub2 Mark=",sub2, "P"
                print "Your Sub3 Mark=",sub3, "P"
                print "Your Sub4 Mark=",sub4, "P"
                print "Your Sub5 Mark=",sub5, "P"
                print "Your Sub6 Mark=",sub6, "F"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "        

                
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=480 and sum<600):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub2 Mark=",sub2, "P"
            print "Your Sub3 Mark=",sub3, "P"
            print "Your Sub4 Mark=",sub4, "P"
            print "Your Sub5 Mark=",sub5, "P"
            print "Your Sub6 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
            
        
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=360 and sum<480):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub2 Mark=",sub2, "P"
            print "Your Sub3 Mark=",sub3, "P"
            print "Your Sub4 Mark=",sub4, "P"
            print "Your Sub5 Mark=",sub5, "P"
            print "Your Sub6 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=270 and sum<360):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub2 Mark=",sub2, "P"
            print "Your Sub3 Mark=",sub3, "P"
            print "Your Sub4 Mark=",sub4, "P"
            print "Your Sub5 Mark=",sub5, "P"
            print "Your Sub6 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 2nd Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=180 and sum<270):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub2 Mark=",sub2, "P"
            print "Your Sub3 Mark=",sub3, "P"
            print "Your Sub4 Mark=",sub4, "P"
            print "Your Sub5 Mark=",sub5, "P"
            print "Your Sub6 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, " All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
            
        else:
            print name," your Result is searching please Wait......"
            time.sleep(10)
            print "Result :: Falied "
            print "Best Of Luck Nest Time"
            
            
    elif(choice==2):
        
        
        print "Ok You Want B.Tech 2nd Sem Result "
        name=raw_input("Enter Your Name:")
        sub1=float(input("Enter your sub1 mark:"))
        sub2=float(input("Enter Your sub2 Mark:"))
        sub3=float(input("Enter your sub3 mark:"))
        sub4=float(input("Enter Your sub4 Mark:"))
        sub5=float(input("Enter your sub5 mark:"))
        sub6=float(input("Enter Your sub6 Mark:"))
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        
        # for invalid Mark Purpose Codings...
        
        if(sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub6>100):
            if(sub1>100):
                print "You Enterted Sub1 Mark is not Valid Please Enter a Valid Mark"
            elif(sub2>100):
                print "You Enterted Sub2 Mark is not Valid Please Enter a Valid Mark"
            elif(sub3>100):
                print "You Enterted Sub3 Mark is not Valid Please Enter a Valid Mark"
            elif(sub4>100):
                print "You Enterted Sub4 Mark is not Valid Please Enter a Valid Mark"
            elif(sub5>100):
                print "You Enterted Sub5 Mark is not Valid Please Enter a Valid Mark" 
            else:
                print "You Enterted Sub6 Mark is not Valid Please Enter a Valid Mark"  
        elif(sub1<30 or sub2<30 or sub3<30 or sub4<30 or sub5<30 or sub6<30):
            if(sub1<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "One Backlock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "F"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
                
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "F"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "F"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "F"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            else:
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "F"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "        

                
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=480 and sum<600):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
        
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=360 and sum<480):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=270 and sum<360):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 2nd Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=180 and sum<270):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, " All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name 
            
        else:
            print name," your Result is searching please Wait......"
            time.sleep(10)
            print "Result :: Falied "
            print "Best Of Luck Nest Time"
            
            
            
            
    elif(choice==3):
        
        
        print "Ok You Want B.Tech 3rd Sem Result "
        name=raw_input("Enter Your Name:")
        sub1=float(input("Enter your sub1 mark:"))
        sub2=float(input("Enter Your sub2 Mark:"))
        sub3=float(input("Enter your sub3 mark:"))
        sub4=float(input("Enter Your sub4 Mark:"))
        sub5=float(input("Enter your sub5 mark:"))
        sub6=float(input("Enter Your sub6 Mark:"))
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        
        # for invalid Mark Purpose Codings...
        
        if(sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub6>100):
            if(sub1>100):
                print "You Enterted Sub1 Mark is not Valid Please Enter a Valid Mark"
            elif(sub2>100):
                print "You Enterted Sub2 Mark is not Valid Please Enter a Valid Mark"
            elif(sub3>100):
                print "You Enterted Sub3 Mark is not Valid Please Enter a Valid Mark"
            elif(sub4>100):
                print "You Enterted Sub4 Mark is not Valid Please Enter a Valid Mark"
            elif(sub5>100):
                print "You Enterted Sub5 Mark is not Valid Please Enter a Valid Mark" 
            else:
                print "You Enterted Sub6 Mark is not Valid Please Enter a Valid Mark"  
        elif(sub1<30 or sub2<30 or sub3<30 or sub4<30 or sub5<30 or sub6<30):
            if(sub1<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "One Backlock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "F"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
                
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "F"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "F"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "F"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            else:
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "F"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "        

                
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=480 and sum<600):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
        
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=360 and sum<480):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=270 and sum<360):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 2nd Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=180 and sum<270):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, " All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name 
            
        else:
            print name," your Result is searching please Wait......"
            time.sleep(10)
            print "Result :: Falied "
            print "Best Of Luck Nest Time"
            
            
            
    elif(choice==4):
        
        
        print "Ok You Want B.Tech 4th Sem Result "
        name=raw_input("Enter Your Name:")
        sub1=float(input("Enter your sub1 mark:"))
        sub2=float(input("Enter Your sub2 Mark:"))
        sub3=float(input("Enter your sub3 mark:"))
        sub4=float(input("Enter Your sub4 Mark:"))
        sub5=float(input("Enter your sub5 mark:"))
        sub6=float(input("Enter Your sub6 Mark:"))
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        
        # for invalid Mark Purpose Codings...
        
        if(sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub6>100):
            if(sub1>100):
                print "You Enterted Sub1 Mark is not Valid Please Enter a Valid Mark"
            elif(sub2>100):
                print "You Enterted Sub2 Mark is not Valid Please Enter a Valid Mark"
            elif(sub3>100):
                print "You Enterted Sub3 Mark is not Valid Please Enter a Valid Mark"
            elif(sub4>100):
                print "You Enterted Sub4 Mark is not Valid Please Enter a Valid Mark"
            elif(sub5>100):
                print "You Enterted Sub5 Mark is not Valid Please Enter a Valid Mark" 
            else:
                print "You Enterted Sub6 Mark is not Valid Please Enter a Valid Mark"  
        elif(sub1<30 or sub2<30 or sub3<30 or sub4<30 or sub5<30 or sub6<30):
            if(sub1<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "One Backlock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "F"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
                
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "F"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "F"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "F"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            else:
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "F"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "        

                
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=480 and sum<600):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
        
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=360 and sum<480):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=270 and sum<360):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 2nd Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=180 and sum<270):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, " All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name 
            
        else:
            print name," your Result is searching please Wait......"
            time.sleep(10)
            print "Result :: Falied "
            print "Best Of Luck Nest Time"
            
            
            
    elif(choice==5):
        
        
        print "Ok You Want B.Tech 5th Sem Result "
        name=raw_input("Enter Your Name:")
        sub1=float(input("Enter your sub1 mark:"))
        sub2=float(input("Enter Your sub2 Mark:"))
        sub3=float(input("Enter your sub3 mark:"))
        sub4=float(input("Enter Your sub4 Mark:"))
        sub5=float(input("Enter your sub5 mark:"))
        sub6=float(input("Enter Your sub6 Mark:"))
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        
        # for invalid Mark Purpose Codings...
        
        if(sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub6>100):
            if(sub1>100):
                print "You Enterted Sub1 Mark is not Valid Please Enter a Valid Mark"
            elif(sub2>100):
                print "You Enterted Sub2 Mark is not Valid Please Enter a Valid Mark"
            elif(sub3>100):
                print "You Enterted Sub3 Mark is not Valid Please Enter a Valid Mark"
            elif(sub4>100):
                print "You Enterted Sub4 Mark is not Valid Please Enter a Valid Mark"
            elif(sub5>100):
                print "You Enterted Sub5 Mark is not Valid Please Enter a Valid Mark" 
            else:
                print "You Enterted Sub6 Mark is not Valid Please Enter a Valid Mark"  
        elif(sub1<30 or sub2<30 or sub3<30 or sub4<30 or sub5<30 or sub6<30):
            if(sub1<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "One Backlock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "F"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
                
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "F"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "F"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "F"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            else:
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "F"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "        

                
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=480 and sum<600):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
        
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=360 and sum<480):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=270 and sum<360):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 2nd Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=180 and sum<270):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, " All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name 
            
        else:
            print name," your Result is searching please Wait......"
            time.sleep(10)
            print "Result :: Falied "
            print "Best Of Luck Nest Time"
            
            
            
    elif(choice==6):
        
        
        print "Ok You Want B.Tech 6th Sem Result "
        name=raw_input("Enter Your Name:")
        sub1=float(input("Enter your sub1 mark:"))
        sub2=float(input("Enter Your sub2 Mark:"))
        sub3=float(input("Enter your sub3 mark:"))
        sub4=float(input("Enter Your sub4 Mark:"))
        sub5=float(input("Enter your sub5 mark:"))
        sub6=float(input("Enter Your sub6 Mark:"))
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        
        # for invalid Mark Purpose Codings...
        
        if(sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub6>100):
            if(sub1>100):
                print "You Enterted Sub1 Mark is not Valid Please Enter a Valid Mark"
            elif(sub2>100):
                print "You Enterted Sub2 Mark is not Valid Please Enter a Valid Mark"
            elif(sub3>100):
                print "You Enterted Sub3 Mark is not Valid Please Enter a Valid Mark"
            elif(sub4>100):
                print "You Enterted Sub4 Mark is not Valid Please Enter a Valid Mark"
            elif(sub5>100):
                print "You Enterted Sub5 Mark is not Valid Please Enter a Valid Mark" 
            else:
                print "You Enterted Sub6 Mark is not Valid Please Enter a Valid Mark"  
        elif(sub1<30 or sub2<30 or sub3<30 or sub4<30 or sub5<30 or sub6<30):
            if(sub1<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "One Backlock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "F"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
                
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "F"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "F"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "F"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            else:
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "F"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "        

                
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=480 and sum<600):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
        
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=360 and sum<480):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=270 and sum<360):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 2nd Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=180 and sum<270):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, " All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name 
            
        else:
            print name," your Result is searching please Wait......"
            time.sleep(10)
            print "Result :: Falied "
            print "Best Of Luck Nest Time"
            
            
            
            
    elif(choice==7):
        
        
        print "Ok You Want B.Tech 7th Sem Result "
        name=raw_input("Enter Your Name:")
        sub1=float(input("Enter your sub1 mark:"))
        sub2=float(input("Enter Your sub2 Mark:"))
        sub3=float(input("Enter your sub3 mark:"))
        sub4=float(input("Enter Your sub4 Mark:"))
        sub5=float(input("Enter your sub5 mark:"))
        sub6=float(input("Enter Your sub6 Mark:"))
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        
        # for invalid Mark Purpose Codings...
        
        if(sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub6>100):
            if(sub1>100):
                print "You Enterted Sub1 Mark is not Valid Please Enter a Valid Mark"
            elif(sub2>100):
                print "You Enterted Sub2 Mark is not Valid Please Enter a Valid Mark"
            elif(sub3>100):
                print "You Enterted Sub3 Mark is not Valid Please Enter a Valid Mark"
            elif(sub4>100):
                print "You Enterted Sub4 Mark is not Valid Please Enter a Valid Mark"
            elif(sub5>100):
                print "You Enterted Sub5 Mark is not Valid Please Enter a Valid Mark" 
            else:
                print "You Enterted Sub6 Mark is not Valid Please Enter a Valid Mark"  
        elif(sub1<30 or sub2<30 or sub3<30 or sub4<30 or sub5<30 or sub6<30):
            if(sub1<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "One Backlock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "F"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
                
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "F"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "F"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "F"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            else:
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "F"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "        

                
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=480 and sum<600):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
        
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=360 and sum<480):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=270 and sum<360):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 2nd Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=180 and sum<270):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, " All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name 
            
        else:
            print name," your Result is searching please Wait......"
            time.sleep(10)
            print "Result :: Falied "
            print "Best Of Luck Nest Time"
            
            
            
    elif(choice==8):
        
        
        print "Ok You Want B.Tech 8th Sem Result "
        name=raw_input("Enter Your Name:")
        sub1=float(input("Enter your sub1 mark:"))
        sub2=float(input("Enter Your sub2 Mark:"))
        sub3=float(input("Enter your sub3 mark:"))
        sub4=float(input("Enter Your sub4 Mark:"))
        sub5=float(input("Enter your sub5 mark:"))
        sub6=float(input("Enter Your sub6 Mark:"))
        sum=sub1+sub2+sub3+sub4+sub5+sub6
        avg=sum/6
        
        # for invalid Mark Purpose Codings...
        
        if(sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub6>100):
            if(sub1>100):
                print "You Enterted Sub1 Mark is not Valid Please Enter a Valid Mark"
            elif(sub2>100):
                print "You Enterted Sub2 Mark is not Valid Please Enter a Valid Mark"
            elif(sub3>100):
                print "You Enterted Sub3 Mark is not Valid Please Enter a Valid Mark"
            elif(sub4>100):
                print "You Enterted Sub4 Mark is not Valid Please Enter a Valid Mark"
            elif(sub5>100):
                print "You Enterted Sub5 Mark is not Valid Please Enter a Valid Mark" 
            else:
                print "You Enterted Sub6 Mark is not Valid Please Enter a Valid Mark"  
        elif(sub1<30 or sub2<30 or sub3<30 or sub4<30 or sub5<30 or sub6<30):
            if(sub1<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "One Backlock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "F"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
                
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "F"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "F"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "
            elif(sub1<30 and sub2<30):
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "F"
                print "Your Sub1 Mark=",sub6, "P"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "  
            else:
                print name," Your Result is searching Please Wait....... "
                time.sleep(10)
                print "............." ,name," MARKSHEET................."
                print "Your Sub1 Mark=",sub1, "F"
                print "Your Sub1 Mark=",sub2, "P"
                print "Your Sub1 Mark=",sub3, "P"
                print "Your Sub1 Mark=",sub4, "P"
                print "Your Sub1 Mark=",sub5, "P"
                print "Your Sub1 Mark=",sub6, "F"
                print ".........................................."
                print "Your Total Mark=",sum,  "Two Baclock"
                print "Your Percentage=",avg
                print "Result ::Passed "        

                
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=480 and sum<600):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name
        
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=360 and sum<480):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum,  "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=270 and sum<360):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, "All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 2nd Class "
            print "Congratulation !! ",name
        elif(sub1>30 and sub2>30 and sub3>30 and sub4>30 and sub5>30 and sub6>30 and sum>=180 and sum<270):
            print name," Your Result is searching Please Wait....... "
            time.sleep(10)
            print ".............", name," MARKSHEET................."
            print "Your Sub1 Mark=",sub1, "P"
            print "Your Sub1 Mark=",sub2, "P"
            print "Your Sub1 Mark=",sub3, "P"
            print "Your Sub1 Mark=",sub4, "P"
            print "Your Sub1 Mark=",sub5, "P"
            print "Your Sub1 Mark=",sub6, "P"
            print ".........................................."
            print "Your Total Mark=",sum, " All Clear"
            print "Your Percentage=",avg
            print "Result ::Passed With 1st Class and Distinction"
            print "Congratulation !! ",name 
            
        else:
            print name," your Result is searching please Wait......"
            time.sleep(10)
            print "Result :: Falied "
            print "Best Of Luck Nest Time"
                                       
    



