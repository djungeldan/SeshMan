with open("counter.txt", 'r') as f:
    for line in f:
        if f.read == 5:
            print("Was 5")
            f.close()
        else:
            with open("counter.txt","w") as d:
                    contents = f.read()
                    contents = int(contents)
                    contents =+ 1
                    print(contents)
                    d.write(str(contents))
                    print(f.read())



