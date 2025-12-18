# patient-transport-optimization
A Python-based route optimization system designed for municipal patient transport services using Nearest Neighbor Algorithm.
# Patient Transport Optimization System 🚑

A Python-based logistics solution designed to optimize free municipal patient transport services. This project focuses on increasing the number of patients served while minimizing fuel consumption and planning staff workload effectively.

## 📌 Problem Statement
[cite_start]Many patients requiring regular hospital check-ups (e.g., dialysis, chemotherapy, physical therapy) lack the physical or financial means to use public transport or private taxis[cite: 13, 14, 19, 21]. [cite_start]Municipalities provide free transport, but high demand often leads to rejected appointments or long waiting times[cite: 33, 41, 42].

## 🚀 Our Solution
[cite_start]We developed a system that allows a single vehicle to carry up to **2 patients** simultaneously by intelligently grouping them based on appointment times and locations[cite: 55]. [cite_start]This approach aims to double the service capacity without increasing the budget[cite: 56].

### Key Technical Features:
- [cite_start]**Automatic Pickup Calculation:** Calculates the exact time a patient must leave home based on hospital distance and average vehicle speed[cite: 140, 141, 142].
- [cite_start]**Nearest Neighbor Algorithm:** Uses a heuristic approach to the Traveling Salesperson Problem (TSP) to determine the most efficient route between patient locations[cite: 264, 283, 291].
- [cite_start]**Constraint Management:** Distinguishes between "standing" and "bed-resident" patients to ensure vehicle capacity is not exceeded[cite: 150, 193, 198].

## 🛠️ Technology Stack
- **Language:** Python
- **Libraries:** `datetime` (for time-slot management)
- **Algorithm:** Nearest Neighbor (Route Optimization)

## ✅ Positive Impacts
- [cite_start]**Fuel Efficiency:** Significant savings by using optimal routes[cite: 279].
- [cite_start]**Increased Capacity:** Fewer rejected appointments for patients in need[cite: 282].
- [cite_start]**Time Management:** Reduced waiting times for patients and planned workload for staff[cite: 280, 285].

## 👥 Contributors
- **Nida Ayşin Çakıroğlu** - [Your LinkedIn Profile]
