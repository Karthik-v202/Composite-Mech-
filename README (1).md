
# 🛠️ Composite Material Property Calculator (Python)

A Python-based engineering tool to calculate Young’s Modulus and Tensile Strength of fiber-reinforced composites using the Rule of Mixtures. The program also generates a color-coded pie chart to visualize fiber and matrix volume fractions.


## 📌 Features

☑️ Calculates composite modulus (Eₐ) and strength (σₐ)

☑️ Accepts custom fiber and matrix properties as input

☑️ Visualizes fiber/matrix proportions using Matplotlib

☑️ Simple CLI interface for quick calculations

☑️ Useful for engineers, students, and material scientists


## 🧮 Formula Used

Rule of Mixtures:

* Ec= Ef*Vf + Em*Vm 
* σc = σf*Vf + σm*Vm

Where:

* Ef,E𝑚 = Modulus of fiber and matrix
* σf,σm =  Strength of fiber and matrix
* Vf,Vm = Volume fraction of fiber and matrix 
## 📸 Sample Output

![App Screenshot](https://github.com/Karthik-v202/Composite-Mech-/blob/main/Figure_1.png)

## 🛠️ Requirements
- Python
* matplotlib>=3.7.0
### 🚀 Run Instructions
```text
git clone https://github.com/YourUsername/CompositeCalculator.git
cd CompositeCalculator
python CompositeMech.py
```

    
## 📂 Example Inputs


💡 Real-World Test Case: *Carbon Fiber–Epoxy Composite*


```text
Fiber (Torayca™ T700): E = 230 GPa
σ = 4900 MPa

Matrix (Epoxy): E = 3.4 GPa
σ = 70 MPa

Composition: 60% Fiber, 40% Matrix
```

🔍 Results:

Young’s Modulus (Eₐ): 139.36 GPa

Tensile Strength (σₐ): 2968 MPa
## 📃 License

This project is open-source under the MIT License [MIT](https://choosealicense.com/licenses/mit/)

