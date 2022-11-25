from pathlib import Path


def line_break(nb):
    print("\n" * nb)


# Creation of a dictionary
dictionary = {".jpeg": "Images",
              ".png": "Images",
              ".jpg": "Images",
              ".gif": "Images",
              ".mp4": "Movies",
              ".mov": "Movies",
              ".zip": "Archives",
              ".pdf": "Documents",
              ".docx": "DocumentsDow",
              ".txt": "Documents",
              ".json": "Documents",
              ".mp3": "Musics",
              ".wav": "Musics",
              }

print("  ╔═══════════════════════════════════════╗")
print("  ║             List of Direct            ║")
print("  ╚═══════════════════════════════════════╝")
line_break(2)

# Display only the folders that don't represent a danger to it's proper functioning
path = Path.home()
for f in path.iterdir():
    path_OK = any([i for i in f.name if i == "."])
    if not path_OK:
        path_list = [f.name]
        print(str(path_list))

# File Storage
sort = input("Where do you want to sort out ?")
line_break(1)
tri_dir = Path.home() / sort
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = tri_dir / dictionary.get(f.suffix, "Others")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)

# Verification if one folder is empty, if is right -> folder will be deleted
folders = [f for f in tri_dir.iterdir() if f.is_dir()]
for f in folders:
    var = 0
    for i in f.iterdir():
        if i.stem:
            var += 1
    if var == 0:
        f.rmdir()
