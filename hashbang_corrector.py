#!/usr/bin/env python3

import os

def change_first_line(path):
    for root, directories, files in os.walk(path):
        for name in files:
            full_name = os.path.join(root, name)
            # os.stat checks that file is not empty
            if ".py" in name and os.stat(full_name) != 0:
                f1 = open(full_name)
                list_of_lines = f1.readlines()
                list_of_lines[0] = "#!usr/bin/env python3\n"
                f1.close()

                f2 = open(full_name, "w")
                f2.writelines(list_of_lines)
                f2.close()

        for file in directories:
            change_first_line(name)

# Path to directory where hashbangs are corrected
p = "~/Projects/experimental"
change_first_line(p)


