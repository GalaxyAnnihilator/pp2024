import os
import subprocess
import shlex

def main():
    while True:
        try:
            command = input("shell> ")
            if command.lower() in ["exit", "quit"]:
                print("Exiting shell...")
                break

            if '|' in command:
                commands = [shlex.split(cmd.strip()) for cmd in command.split('|')]
                prev_proc = None
                for cmd in commands:
                    if prev_proc is None:
                        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                    else:
                        proc = subprocess.Popen(cmd, stdin=prev_proc.stdout, stdout=subprocess.PIPE)
                        prev_proc.stdout.close()
                    prev_proc = proc
                output, _ = prev_proc.communicate()
                print(output.decode())
                
            elif '>' in command:
                cmd, out_file = command.split('>', 1)
                cmd = shlex.split(cmd.strip())
                out_file = out_file.strip()
                with open(out_file, 'w') as f:
                    subprocess.run(cmd, stdout=f)
                    
            elif '<' in command:
                cmd, in_file = command.split('<', 1)
                cmd = shlex.split(cmd.strip())
                in_file = in_file.strip()
                try:
                    with open(in_file, 'r') as input_file:
                        result = subprocess.run(cmd, stdin=input_file, capture_output=True, text=True)
                        print(result.stdout)
                except FileNotFoundError:
                    print(f"Error: File '{in_file}' not found.")
            else:
                subprocess.run(shlex.split(command))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
