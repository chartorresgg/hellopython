"""
# Crea una estructura de carpetas para un proyecto de Python
"""

import os

estructura = [
    "Python/00_Python_Introduction",
    "Python/01_Data_Structures",
    "Python/02_Basic_Types",
    "Python/03_Flow_Control",
    "Python/04_Functions",
    "Python/05_Advanced_Types",
    "Python/06_Modules_and_Packages",
    "Python/07_Projects",
    "Python/08_Advanced_Concepts",
    "Python/09_Standard_Library",
    "Python/10_Environment_Setup",
    "Python/11_Debugging_and_Testing",
    "Python/12_Concurrency_and_Parallelism",
    "Python/13_Interfacing_with_Other_Languages",
    "Python/14_Automatizacion",
    "Python/15_Web_Scraping",
    "Python/16_Data_Science",
    "Python/17_Machine_Learning",
    "Python/18_Deep_Learning",
    "Python/19_Computer_Vision",
    "Python/20_Natural_Language_Processing",
    "Python/21_Deployment",
    "Python/22_Advanced_Topics",
    "Python/23_Projects",
    "Python/24_Resources",
    "Python/25_Community",
    "Python/26_Contributing",
    "Python/27_Appendix",
    "Python/28_References",
]

for carpeta in estructura:
    os.makedirs(carpeta, exist_ok=True)

print("✅ Estructura de carpetas creada con éxito.")
