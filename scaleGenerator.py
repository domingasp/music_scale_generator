# Import for GUI
import tkinter as tk

# Generates different musical scales
twoOctaves = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# 1 Represents a half step and 2 represents a whole step
majorScale = [2, 2, 1, 2, 2, 2, 1]
minorScale = [2, 1, 2, 2, 1, 2, 2]

# Generates the selected scale
def generateScale(rootNote, scale):
    createdScale = []
    indexOfFirstRootNote = 0

    # Determines the location of the first note in the twoOctaves list
    counter = 0
    while counter < len(twoOctaves):
        if (rootNote == twoOctaves[counter]):
            indexOfFirstRootNote = counter
            break
        counter += 1
    
    # Generates the scale based on the steps in the chosen scale
    for step in scale:
        createdScale.append(twoOctaves[indexOfFirstRootNote])
        indexOfFirstRootNote += step
    createdScale.append(rootNote)

    return createdScale

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Scale Generator")

        self.noteSelection = tk.OptionMenu(self.master, "C", twoOctaves[0], twoOctaves[1], twoOctaves[2], twoOctaves[3], twoOctaves[4], twoOctaves[5], twoOctaves[6])
        self.noteSelection.grid(row = 0, column = 0)

# Runs the main application
def main():
    root = tk.Tk()
    gui = GUI(root)
    print(generateScale('C', minorScale))

    root.mainloop()

# Entry of the script is the main() function
if __name__ == '__main__':
    main()

# TODO:
# Make the script send a text to my telephone of the scale
# Create a GUI which will make selecting a scale much simpler
# Select a random scale. Easiest way would be to generate a random number from 0 - 6 as this will represent the first half of the twoOctaves list and cover all notes.