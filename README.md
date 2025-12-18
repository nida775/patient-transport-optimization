# Patient Transport Optimization System 🚑

A Python-based logistics solution designed to optimize free municipal patient transport services. This project focuses on increasing the number of patients served while minimizing fuel consumption and planning staff workload effectively.

## 📌 Problem Statement
Many patients requiring regular hospital check-ups (e.g., dialysis, chemotherapy, physical therapy) lack the physical or financial means to use public transport or private taxis. 
Municipalities provide free transport, but high demand often leads to rejected appointments or long waiting times.

## 🚀 Our Solution
We developed a system that allows a single vehicle to carry up to **2 patients** simultaneously by intelligently grouping them based on appointment times and locations.
This approach aims to double the service capacity without increasing the budget.

### Key Technical Features:
- **Automatic Pickup Calculation:** Calculates the exact time a patient must leave home based on hospital distance and average vehicle speed.
- **Nearest Neighbor Algorithm:** Uses a heuristic approach to the Traveling Salesperson Problem (TSP) to determine the most efficient route between patient locations.
- **Constraint Management:** Distinguishes between "standing" and "bed-resident" patients to ensure vehicle capacity is not exceeded.

## 🛠️ Technology Stack
- **Language:** Python
- **Libraries:** `datetime` (for time-slot management)
- **Algorithm:** Nearest Neighbor (Route Optimization)

## ✅ Positive Impacts
- **Fuel Efficiency:** Significant savings by using optimal routes.
- **Increased Capacity:** Fewer rejected appointments for patients in need.
- **Time Management:** Reduced waiting times for patients and planned workload for staff.

## 👥 Contributors
- **Nida Ayşin Çakıroğlu**
- **Ahmet İsar Baş**
