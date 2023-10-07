import os 
os.system("python pip install pedalboard")
shell_script = './install_Applio.sh'
os.system(f'chmod +x {shell_script}')
try:
    return_code = os.system(shell_script)
    if return_code == 0:
        print("Shell script executed successfully.")
    else:
        print(f"Shell script failed with return code {return_code}")
except Exception as e:
    print(f"An error occurred: {e}")



os.system("python -m sklearnex infer-web.py --pycmd python --port 7897 --theme dark")