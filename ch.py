import matplotlib.pyplot as plt
marks=[10,20,30,40]
student=["Shivam","Rohit","Ramesh","Suresh"]
plt.plot(student, marks, color="red",label="Marks", linewidth=2, marker="o", markersize=8, markerfacecolor="blue", markeredgecolor="black")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("student_marks.png")
plt.xlabel("Students", fontsize=12, color="blue")
plt.ylabel("Marks", fontsize=12, color="blue")
plt.title("Student Marks")
plt.show()