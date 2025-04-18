import zipfile

def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(dest_dir,'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)

if __name__ == "__main__":
    make_archive(filepaths=["weather.csv"], dest_dir="dest")





