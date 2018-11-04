import subprocess


def run(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    )
    output, error = process.communicate()
    return output, error

def get_current_dir():
    output, _ = run('pwd')
    return output.decode('ascii').strip('\n')

