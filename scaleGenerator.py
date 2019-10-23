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

# Runs the main application
def main():
    print(generateScale('C', minorScale))

# Entry of the script is the main() function
if __name__ == '__main__':
    main()