import shutil

def main():
    shutil.copy("from/test.txt", "to")
    shutil.copy2("from/test1.txt", "to")
    
if __name__ == "__main__":
    main()