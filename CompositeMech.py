import matplotlib.pyplot as plt # Import the matplotlib library for plotting graphs

# ---------------- USER INPUTS ----------------
Ef=float(input("Enter Fiber Modulus (GPa): ")) # Get fiber modulus from user in GPa
Em=float(input("Enter Matrix Modulus (GPa): ")) # Get matrix modulus from user in GPa
fs=float(input("Enter Fiber Strength(MPa): ")) # Get fiber strength from user in MPa
ms=float(input("Enter Matrix Strength(MPa): ")) # Get matrix strength from user in MPa
Vf=float(input("Enter Fiber Volume Fraction: ")) # Get fiber volume fraction from user
# ------------------------------------------------

# Calculate matrix volume fraction (remaining fraction after fiber)
Vm=1-Vf

# ---------------- CALCULATIONS ----------------
# Calculate composite modulus using Rule of Mixtures:
# Ec = (Ef * Vf) + (Em * Vm)

Ec = Ef*Vf + Em*Vm
print("The Composite Modulus is: ", Ec, "GPa")

# Calculate composite strength using Rule of Mixtures:
# σc = (fs * Vf) + (ms * Vm)

sigma_c = (fs*Vf + ms*Vm)
print("The Composite Strength is: ", sigma_c, "MPa")

# ---------------- PIE CHART VISUALIZATION ----------------
# Create a list of volume fractions for plotting

Pie=[Vf, Vm]

# Draw pie chart to show fiber vs matrix volume fraction

plt.pie(Pie, labels=["V: of Fiber", "V: of Matrix"], autopct='%1.1f%%', colors={'#66b3ff', '#ff9999'})

# Add title to the chart
plt.title("Volume Fraction of Fiber and Matrix")

# Display the chart
plt.show()