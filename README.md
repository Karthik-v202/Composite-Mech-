# 🛠️ Composite Material Property Calculator (Python)

A Python-based engineering tool to calculate the mechanical properties of **fiber-reinforced composites** using the **Rule of Mixtures**.  
The program also generates **visualizations** to make composite mechanics more intuitive.  

---

## 📌 Features

### ✅ Version 2.0 (Latest)
☑️ Composite Modulus (Eₐ) & Strength (σₐ)  
☑️ Composite Density Calculation  
☑️ Specific Modulus & Specific Strength (lightweight design analysis)  
☑️ Failure Prediction (Max Stress Criterion)  
☑️ All-in-One mode (runs all calculations together)  
☑️ Pie Chart visualization for fiber/matrix volume fractions  

### 🏷 Version 1.0 (Initial Release)
☑️ Basic Rule of Mixtures for modulus & strength  
☑️ Pie chart visualization of volume fractions  
☑️ Simple CLI interface  

---

## 🧮 Formula Used

**Rule of Mixtures:**

* Ec = Ef*Vf + Em*V_m  
* sigmac = sigmaf*Vf + sigma*Vm  
* rhoc = rho f*Vf + rho m*Vm 

**Specific Properties:**  
* Specific Modulus = Ec / rho c
* Specific Strength = sigma c/rho c  

Where:  
- Ef, Em  = Modulus of fiber & matrix  
- sigma f, sigma m = Strength of fiber & matrix  
- rho f, rho m  = Density of fiber & matrix  
- Vf, Vm  = Volume fractions of fiber & matrix  

---

## 📸 Sample Output (v2.0)

Pie Chart of Fiber/Matrix Volume Fraction:  

![App Screenshot](https://github.com/Karthik-v202/Composite-Mech-/blob/main/Figure_1.png)

---

## 📂 Example Test Cases

### 🔹 1. Modulus & Strength
**Input:**  
- Fiber (Torayca™ T700): E = 230 GPa, σ = 4900 MPa  
- Matrix (Epoxy): E = 3.4 GPa, σ = 70 MPa  
- Volume Fraction: 60% Fiber  

**Result:**  
- Composite Modulus: **139.36 GPa**  
- Composite Strength: **2968 MPa**  

---

### 🔹 2. Density
**Input:**  
- Fiber Density = 1.8 g/cm³  
- Matrix Density = 1.2 g/cm³  
- Volume Fraction: 60% Fiber  

**Result:**  
- Composite Density: **1.56 g/cm³**  

---

### 🔹 3. Specific Properties
**Result:**  
- Specific Modulus: **89.3 GPa·cm³/g**  
- Specific Strength: **1902 MPa·cm³/g**  

---

### 🔹 4. Failure Prediction
**Case A:** Applied Stress = 2000 MPa → ✅ Safe  
**Case B:** Applied Stress = 3500 MPa → ❌ Failure  

---

## 🛠️ Requirements
- Python ≥ 3.8  
- matplotlib ≥ 3.7.0  

---

## 🚀 Run Instructions
```bash
git clone https://github.com/Karthik-v202/Composite-Mech-.git
cd Composite-Mech-
python CompositeMech_v2.py
