#!/bin/bash

# Set current directory as the working directory
cd "$(pwd)"

# Remove current POTCAR and reveal the headlines of a file named POSCAR
rm -i POTCAR
head POSCAR

# Ask for the input "which is the element line"
read -p "Which is the element line? " element_line

# Extract elements from the specified line
elements=$(sed -n "${element_line}p" POSCAR)

# Loop over each element to perform the required operations
for element in $elements; do
    case $element in
        C)
            new_name="C_GW_new"
            ;;
        Li)
            new_name="Li_sv_GW"
            ;;
        H)
            new_name="H_GW"
            ;;
        O)
            new_name="O_GW_new"
            ;;
        N)
            new_name="N_GW_new"
            ;;
        He)
            new_name="He"
            ;;
        S)
            new_name="S_GW"
            ;;
        F)
            new_name="F_GW_new"
            ;;
        *)
            # If there's no matching rule for the element, we skip the iteration
            echo "No matching rule for element: $element"
            continue
            ;;
    esac

    # Concatenate the POTCAR into the working directory's POTCAR
    cat "/path/to/your/potcar/bank/$new_name/POTCAR" >> POTCAR
done

echo "POTCAR file has been generated/updated."
