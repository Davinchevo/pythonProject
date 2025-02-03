for n in range(1000,3001):
        #To be able to split the number into its
        #digits we will convert it to a string
        string_number = str(n)
        #Then we split it
        split_string = list(string_number)
        #We use a boolean variable to track if we seen an odd digit
        all_even = True
        #Check each number
        for x in split_string:
            #We convert the digit back to int and check if it is odd
            if int(x) % 2 != 0:
                #Now we indicate that we seen at least one odd digit
                all_even = False
        #If all_even is still equal all digits must be even
        if all_even:
            print(n, ",", end = "")