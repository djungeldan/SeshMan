'''
RIGHT THIS IS GONNA WORK
this is a file for file manipulation testing
for some reason ive been having issues with reading a value from the txt
some data type issue
gonna start from scratch and this should work 
'''
reset = 0
with open("counter.txt","r+") as getCounter:

    total = 1

    for line in getCounter:

        try:

            total += int(line)

            with open("counter.txt","w+") as writeCounter:

                writeCounter.writelines(str(total))

                if total >= 5:
                    print("Counter is either 5 or more than 5")
                    writeCounter.close()

                    with open("counter.txt","w") as resetLines:
                        resetLines.write(str(reset))
                        break

                else:
                    print("Counter is less than 5")

        except ValueError:
            pass






