rows = 5

i = 0
asterik = "*"
asterik_count = 1
start_point = 5

for i in range(1, rows+1):

    while i < start_point :
        print(" ")
        i += 1

        while asterik_count < asterik_count+2:
         print(asterik)  
         asterik_count += 2

    start_point -= 1
        