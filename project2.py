# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Employee": ["Aman", "Priya", "Rahul", "Neha", "Rohit",
#                  "Sneha", "Vikas", "Pooja", "Arjun", "Simran",
#                  "Karan", "Meena"],
#     "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales",
#                    "IT", "Finance", "Finance", "Sales", "HR", "Finance"],
#     "Performance": [88, 76, 92, 81, 69, 95, 74, 86, 91, 72, 84, 79],
#     "Projects_Completed": [5, 3, 7, 4, 2, 6, 3, 5, 8, 4, 5, 4]
# }

# df = pd.DataFrame(data)

# Tasks

# 1. Calculate the average performance score of each department using Pandas.
# 2. Find the department with the highest average performance.
# 3. Calculate the total projects completed by each department.
# 4. Create a bar chart comparing average department performance.
# 5. Use different bar colors and add suitable titles and axis labels.
# 6. Set the Y-axis limit from 0 to 100 and show ticks at intervals of 10.
# 7. Add a grid to improve readability.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Employee": ["Aman", "Priya", "Rahul", "Neha", "Rohit",
                 "Sneha", "Vikas", "Pooja", "Arjun", "Simran",
                 "Karan", "Meena"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales",
                   "IT", "Finance", "Finance", "Sales", "HR", "Finance"],
    "Performance": [88, 76, 92, 81, 69, 95, 74, 86, 91, 72, 84, 79],
    "Projects_Completed": [5, 3, 7, 4, 2, 6, 3, 5, 8, 4, 5, 4]
}

df = pd.DataFrame(data)
print(df)
a=df.groupby("Department")["Performance"].mean()
print(a)
b=a.max()
print(b)