buildtype = ""
while buildtype != "R" or buildtype != "C":
    buildtype = input.upper("enter R for residential or C for commercial")
    if buildtype != "R" or buildtype != "C":
        print("invalid input")
