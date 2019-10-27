# Import for GUI
import tkinter as tk

# Generates different musical scales
twoOctaves = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# 1 Represents a half step and 2 represents a whole step
majorScale = [2, 2, 1, 2, 2, 2, 1]
minorScale = [2, 1, 2, 2, 1, 2, 2]

# Generates the selected scale
def generateScale(gui):
    # Gets the selected root note from the gui. Sets the default scale to be major.
    rootNote = gui.noteOptionVar.get()
    scale = majorScale

    # Checks if the Minor scale is the selected option and if it is then set that to be the chosen scale to generate.
    if (gui.scaleOptionVar.get() == 'Minor'):
        scale = minorScale

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

    # For each note label check if it's in the generated scale and style according. If root note style blue, if in scale style green and if not in scale style red
    for label in gui.noteLabels:
        if (label['text'] in createdScale):
            if (label['text'] == rootNote):
                label['background'] = 'blue'
            else:
                label['background'] = 'green'
            label['foreground'] = 'white'
        else:
            label['background'] = 'red'
            label['foreground'] = 'black'

# Handles the GUI and all different components
class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Scale Generator')

        ###### Note Selection Label and OptionMenu (Dropdown select) ######
        self.noteOptionLabel = tk.Label(self.master, text = 'Note:')
        self.noteOptionLabel.grid(row = 0, column = 1, columnspan = 3)

        # Option menu variable - Needed for the OptionMenu to function correctly as this is what gets set
        self.noteOptionVar = tk.StringVar()
        self.noteOptionVar.set(twoOctaves[0])

        # Creates the OptionMenu and adds it to the master
        self.noteSelection = tk.OptionMenu(self.master, self.noteOptionVar, twoOctaves[0], twoOctaves[1], twoOctaves[2], twoOctaves[3], twoOctaves[4], twoOctaves[5], twoOctaves[6], twoOctaves[7], twoOctaves[8], twoOctaves[9], twoOctaves[10], twoOctaves[11])
        self.noteSelection.grid(row = 0, column = 4, columnspan = 3)


        ###### Scale Selection Label and OptionMenu (Dropdown select) ######
        self.scaleOptionLabel = tk.Label(self.master, text = 'Scale:')
        self.scaleOptionLabel.grid(row = 1, column = 1, columnspan = 3)

        # Option menu variable - Needed for the OptionMenu to function correctly as this is what gets set
        self.scaleOptionVar = tk.StringVar()
        self.scaleOptionVar.set('Major')

        # Creates the OptionMenu and adds it to the master
        self.scaleSelection = tk.OptionMenu(self.master, self.scaleOptionVar, 'Major', 'Minor')
        self.scaleSelection.grid(row = 1, column = 4, columnspan = 3)

        self.generateButton = tk.Button(self.master, text = 'Generate', command= lambda: generateScale(self))
        self.generateButton.grid(row = 0, column = 6, columnspan = 7, rowspan = 2)

        ###### Create the different note labels ######
        # Store the labels in an array in order to enable changing of the appearance in the future
        self.noteLabels = []

        # Create 12 note labels which will display the desired scale to the user
        for x in range(0, 12):
            self.noteLabel = tk.Label(master, text = twoOctaves[x], width = 2, background = 'red')
            self.noteLabels.append(self.noteLabel)

            self.noteLabel.grid(row = 2, column = x + 1, padx = 2, pady = 2)

# Runs the main application
def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

# Entry of the script is the main() function
if __name__ == '__main__':
    main()