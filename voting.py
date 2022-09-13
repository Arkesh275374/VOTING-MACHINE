print("\tVoting System\n\n")
candidate1=input("Enter 1st Candidate Name : ")
candidate2=input("Enter 2nd Candidate Name : ")
can1_votes=0
can2_votes=0
nota_votes=0
voters_id=[1,2,3,4,5,6,7,8,9,10]
no_voters=len(voters_id)
voted=[]


while True:
    
    if voters_id==[]:
        print("\n\n\tElection is completed\n")
        
        if can1_votes>can2_votes:
            a=(can1_votes-can2_votes)
            print(f"{candidate1} Won the Election by {a} votes lead")
        
        elif can2_votes>can1_votes:
            b=(can2_votes-can1_votes)
            print(f"{candidate1} Won the Election by {b} votes lead")
        
        elif can2_votes==can1_votes:
            print("Tied")
        
        break
           
    else:
        voter=int(input("Enter your Voter ID : "))
        if voter in voted:
            print("You already Voted")
        else:
            if voter in voters_id:
                
                print(f"\n1.{candidate1}\n2.{candidate2}")
                choice=int(input("\nEnter your choice : "))
                
                if choice==1:
                    can1_votes+=1
                    print(f"You Voted {candidate1}")
                
                elif choice==2:
                    can2_votes+=1
                    print(f"You Voted {candidate2}")
                
                else:
                    nota_votes+=1
                    print("You Voted None Of The Above")
                
                voters_id.remove(voter)
                voted.append(voter)
            
            else:
                print("You are not eligible for voting ")

