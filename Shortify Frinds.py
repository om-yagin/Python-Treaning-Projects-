char_list = []
friends_input = input("enter names separated by comma: \n").lower()
friends_names = friends_input.split(",")

for name in friends_names:
  
    clean_name = name.strip()
    names = clean_name.split() 
    print(names)
    
    if len(names) >= 2:

        st1_names = names[0][0].upper()
        ed2_names = names[1][0].upper()
        
        char = st1_names + "." + ed2_names + "."
        char_list.append(char)

print(f"\n This is the first letters of friends \n {char_list}")
