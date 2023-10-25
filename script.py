import subprocess

def run_scripts():
    subprocess.call(["python3", "main.py", str(42)])

if __name__ == "__main__":
    run_scripts()