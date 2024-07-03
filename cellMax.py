# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt

def read_value_from_dat_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines from the .dat file
        lines = file.readlines()
        
        # Get the value from row 5 and column 2 (note that Python uses 0-based indices)
        value = float(lines[4].split()[1])
        
    return value

def main():
    output_file = "output.dat"

    # List of folders numbered from 5 to 305
    folders = [str(i) for i in range(5, 305, 5)]

    # Path to the folder containing the .dat files
    base_folder_path = "postProcessing/a1/cellMax/"

    with open(output_file, 'w') as output:
        # Write the first row with the numbers of the folders
        output.write(" ".join(folders) + "\n")

        for folder in folders:
            # Construct the full path to the current .dat file
            folder_path = os.path.join(base_folder_path, folder)
            file_path = os.path.join(folder_path, "volFieldValue.dat")

            # Read the value from the current .dat file
            value = read_value_from_dat_file(file_path)

            # Write the value to the output file
            output.write(f"{value} ")

    print("Process completed. Values have been saved to 'output.dat'.")

    # Additional part: Read the generated output.dat file and save a plot of temperature vs time
    with open(output_file, 'r') as file:
        lines = file.readlines()

    # Extract folder numbers (time) and corresponding values (temperature)
    times = list(map(int, lines[0].split()))
    temperatures = list(map(float, lines[1].split()))

    # Plot temperature vs time
    plt.figure()
    plt.plot(times, temperatures, marker='o')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temperature vs Time')
    plt.grid(True)
    plt.savefig('temperature_vs_time.png')
    plt.show()

if __name__ == "__main__":
    main()
