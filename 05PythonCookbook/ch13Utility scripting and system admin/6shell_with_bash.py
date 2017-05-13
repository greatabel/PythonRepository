import subprocess

if __name__ == "__main__":
    try:
        out_bytes = subprocess.check_output('ls -la', shell=True)
        
        out_text = out_bytes.decode('utf-8')
        print("####\n"*3,out_text)
    except subprocess.CalledProcessError as e:
        print('It did not work. Reason:', e)
        print('Exitcode:', e.returncode)