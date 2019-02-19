def bill(): 
            bn=73273
            print("**************INVOICE**************")
            print("     welcome to cabz service")
            print("-----------------------------------")
            print("bill number                ",bn)
            print("Total ride distance is     ",k,"km")
            print("wehicle type is")
            
           


            if(typ==1):
                      print("Fare of the ride is       ",bill1,"Rs")
            elif(typ==2):
                      print("Fare of the ride is       ",bill2,"Rs")
            elif(typ==3):
                      print("Fare of the ride is       ",bill3,"Rs")
            print("************************************\n")
            
            

while True:

            try:
                print("WELCOME TO CABZ")
                source=float(input("Starting odometer reading:\n"))
                if (source>=0):
                               while True:
                                            try:
                                                des=float(input("Ending odometer reading:\n"))
                                                
                                                if(des<source):
                                                              print("invalid entry")
                                                              
                                        

                                                else:   
                                                        k=des-source
                                                        
                                                        while True:
                                                                    try:
                                                                        print("select the type :")
                                                                        print(" 1.auto \n 2.micro \n 3.mini")
                                                                        typ=int(input())
                                                                        if(typ==1):
                                                                                    print("auto")
                                                                                    rate=20
                                                                                    bill1=(k*rate)
                                                                                    bill()
                                                                                    break

                                                                        elif(typ==2):
                                                                                    print("micro")
                                                                                    rate=30
                                                                                    bill2=(k*rate)
                                                                                    bill()
                                                                                    break

                                                                        elif(typ==3):
                                                                                    print("mini")
                                                                                    rate=40
                                                                                    bill3=(k*rate)
                                                                                    bill()
                                                                                    break
                                                                        else:
                                                                              print("INVALID CHOICE")
                                                                    except:
                                                                             break


                                                  




            
                                            except:
                                                     break
                else:
                     print("INVALID INPUT")


            except:
                      print("INVALID INPUTS")
                      break
