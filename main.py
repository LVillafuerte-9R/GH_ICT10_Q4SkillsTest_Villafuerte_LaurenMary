from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
absences = np.array([0, 0, 0, 0, 0])

def update_tracker(e):
    day_index = int(document.getElementById("day-select").value)
    count = document.getElementById("absence-input").value
    
    if count == "":
        count = 0
    
    absences[day_index] = int(count)
    
    display_graph()

def display_graph():
    document.getElementById("graph-output").innerHTML = ""
    
    plt.clf() 
    
    plt.figure(figsize=(6, 4))
    plt.plot(days, absences, marker='o') 
    plt.title('ωєєкℓу αттєη∂αη¢є (αвѕєη¢єѕ)')
    plt.xlabel('ᴅᴀʏ')
    plt.ylabel('ɴᴜᴍʙᴇʀ ᴏꜰ ᴀʙꜱᴇɴᴄᴇꜱ')
    plt.grid(True)
    
    display(plt, target="graph-output")