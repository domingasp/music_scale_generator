# Generates different musical scales
twoOctaves = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# 1 Represents a half step and 2 represents a whole step
majorScale = [2, 2, 1, 2, 2, 2, 1]
minorScale = [2, 1, 2, 2, 1, 2, 2]

def generateScale(rootNote, scale):
    createdScale = []
    indexOfFirstRootNote = 0

    counter = 0
    while counter < len(twoOctaves):
        if (rootNote == twoOctaves[counter]):
            indexOfFirstRootNote = counter
        counter += 1
    print(indexOfFirstRootNote)

def main():
    generateScale('C#', majorScale)

if __name__ == '__main__':
    main()