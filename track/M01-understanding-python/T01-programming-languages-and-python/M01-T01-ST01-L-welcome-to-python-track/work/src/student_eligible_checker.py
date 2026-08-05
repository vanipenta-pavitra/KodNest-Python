marks = 78
attendance = 82
project_completion = "yes"

if marks >= 60 and attendance >= 75:
    if project_completion:
        print("Eligible")
    else:
        print("Not Eligible")

else:
    print("Not Eligible")        
