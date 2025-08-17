from datetime import datetime  
current_year = datetime.now().year  

if current_year % 4 == 0:
    print(f"{current_year} - високосный")
else:
    print(f"{current_year} - невисокосный")