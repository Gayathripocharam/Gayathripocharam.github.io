<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,100:8A2BE2&height=200&section=header&text=Disk%20Scheduling%20Visualizer&fontSize=45&fontAlignY=35&animation=fadeIn&fontColor=ffffff"/>
</p>

<h3 align="center">⚡ Operating Systems Disk Management Simulation ⚡</h3>

<p align="center">
  <img src="https://img.shields.io/badge/FOCUS-OS%20SIMULATION-00F7FF?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/STACK-PYTHON%20%7C%20GUI-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/STATUS-ACTIVE-success?style=for-the-badge"/>
</p>

**A comprehensive, interactive simulation & visualization tool for Disk Scheduling Algorithms**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Modern_UI-1F6FEB?style=for-the-badge)](https://github.com/TomSchimansky/CustomTkinter)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualizations-11557C?style=for-the-badge)](https://matplotlib.org)

---

## 📑 Table of Contents

| # | Section |
|---|---------|
| 1 | [Overview](#overview) |
| 2 | [Algorithm Breakdown](#algorithm-breakdown) |
| 3 | [Tech Stack](#tech-stack) |
| 4 | [Setup & Installation](#setup--installation) |
| 5 | [Usage Guide](#usage-guide) |
| 6 | [Performance Benchmarks](#performance-benchmarks) |

---

## Overview

The **Disk Scheduling Algorithm Visualizer** is a Python GUI application that brings Operating System theory to life through real-time simulation and interactive dynamic visualization. 

> Built for OS coursework, academic demos, and lab sessions.
```
┌─────────────────────────────────────────────────────────────────────┐
│                    WHAT THIS PROJECT COVERS                         │
├──────────────────────┬──────────────────────┬───────────────────────┤
│   💾 Disk I/O        │   📊 Dynamic Charts   │   ✨ Dark UI          │
│   FCFS, SSTF         │   Visual Line Plots  │   Cyber-Glassmorphism │
├──────────────────────┼──────────────────────┼───────────────────────┤
│   🔍 Directional I/O │   ⏱ Performance metrics│   🎲 Randomizer      │
│   SCAN, C-SCAN       │   Total Head Seek    │   Test Generators     │
└──────────────────────┴──────────────────────┴───────────────────────┘
```

---

## Algorithm Breakdown

### 💾 Supported Disk I/O Management Algorithms
```
  Disk Track Layout  (0 ──────────────────────────── 199)

  Head: 53 ──▶
  Requests: [98, 183, 37, 122, 14, 124, 65, 67]

  FCFS:   53→98→183→37→122→14→124→65→67     Total: 640
  SSTF:   53→65→67→37→14→98→122→124→183     Total: 236  ← ✅ Best
  SCAN:   53→65→67→98→122→124→183→37→14     Total: 331
```

**Algorithms Supported:**

| Algorithm | Strategy | Starvation Risk | Complexity |
|-----------|----------|-----------------|------------|
| FCFS | First Come First Serve | Low | O(n) |
| SSTF | Shortest Seek Time First | **High** | O(n²) |
| SCAN | Elevator (bidirectional) | None | O(n log n) |
| C-SCAN | Circular SCAN | None | O(n log n) |

---

## Tech Stack
```
┌─────────────────────────────────────────────────────────────────┐
│                        TECH STACK                               │
├─────────────────────┬───────────────────────────────────────────┤
│  Language           │  Python 3.8+                              │
├─────────────────────┼───────────────────────────────────────────┤
│  GUI Framework      │  CustomTkinter (dark/light adaptive UI)   │
│                     │  Tkinter (base widgets)                   │
├─────────────────────┼───────────────────────────────────────────┤
│  Visualization      │  Matplotlib (plots + animations)          │
└─────────────────────┴───────────────────────────────────────────┘
```

---

## Setup & Installation

### Prerequisites
```
✅ Python 3.8 or higher
✅ pip (Python package manager)
✅ Git
```

### Installation Steps
```bash
# 1. Clone the repository
git clone https://github.com/Gayathripocharam/disk-scheduling-visualizer.git

# 2. Navigate to the project directory
cd disk-scheduling-visualizer

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Launch the visualizer 
python disk_scheduling_gui.py
```

### Dependencies (`requirements.txt`)
```
customtkinter
matplotlib
```

---

## Usage Guide

### Disk Scheduling — Step by Step

| Step | Action |
|------|--------|
| 1 | Check sidebar, enter number of requests OR click **"Generate"** under Random Requests |
| 2 | Fill in **Requests (space-sep)** (integers, range 0–199 e.g. 98 183 37 122) |
| 3 | Set **Head Position** (single integer e.g. 53) |
| 4 | Change **Disk Size** if necessary |
| 5 | Choose **SCAN/C-SCAN Direction** — Left or Right |
| 6 | Click **"Run Analysis"** |
| 7 | View the results in the **Results** tab (dynamically highlights the best track) |
| 8 | Switch to the **FCFS**, **SSTF**, **SCAN**, and **C-SCAN** graph tabs to see matplotlib plot data |

---

## Performance Benchmarks

### Algorithm Efficiency Comparison (Sample Run)
```
  Total Head Movement (Lower = Better)

  FCFS   ████████████████████████████████ 640
  SCAN   █████████████████ 331
  SSTF   ████████████ 236  ← 🏆 Optimal
  C-SCAN ███████████████████ 370

         0        200      400      600
```

### Big-O Complexity Reference

| Algorithm | Time Complexity | Space | Notes |
|-----------|----------------|-------|-------|
| FCFS | O(n) | O(1) | No sorting needed |
| SSTF | O(n²) | O(1) | Greedy nearest search |
| SCAN | O(n log n) | O(n) | Sort + single pass |
| C-SCAN | O(n log n) | O(n) | Circular variant |

---



<div align="center">

---

**Designed & Developed for Operating Systems Analysis & Teaching**

⭐ Star this repo if it helped you · 
🐛 Found a bug? Open an issue

---

*Built with Python · CustomTkinter · Matplotlib*

</div>
