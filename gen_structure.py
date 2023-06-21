""" Boilerplate generator """

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="{'time':'%(asctime)s', 'message': '%(message)s'}",
    datefmt="%Y%m%d %H:%M:%S",
)


def generate_structure(prefix):
    """Generates boilerplate project structure.
    Creates main.py / readme.md in a subfolder only if they don't exist.
    """
    for i in range(100):
        index = i + 1
        subfolder = f"{prefix}_{index:02}"
        print(subfolder)
        os.makedirs(subfolder, exist_ok=True)
        try:
            with open(f"{subfolder}/main.py", mode="x") as file:
                text = f'"""Day {index} solution"""'
                file.write(text)
        except FileExistsError:
            logging.info(f"main.py already exists at .\{subfolder}")

        try:
            with open(f"{subfolder}/README.md", mode="x") as file:
                text = f"# Day {index} solution"
                file.write(text)
        except FileExistsError:
            logging.info(f"README.md already exists at .\{subfolder}.")


if __name__ == "__main__":
    # generate_structure(prefix="Day")

    for root, folders, files in os.walk("."):
        for folder in folders:
            from pathlib import Path

            st = Path(folder).stem
            if len(st) == 6 and st.startswith("Day"):
                new_name = os.path.join(root, st[:3] + "_" + "0" + st[4:])
                print(new_name)
                os.rename(os.path.join(root, folder), new_name)
