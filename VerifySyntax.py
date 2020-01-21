import subprocess

if __name__ == '__main__':
    full_execute_parameters = '.\\OptCoreExecutable\\Opt.exe -m CE -p Kmedian -f ring.dat'
    # print(full_execute_parameters)
    cmd_process = subprocess.Popen(full_execute_parameters, shell=True,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
    cmd_process.stdin.write('100\n'.encode('utf-8'))
    cmd_process.stdin.write('100\n'.encode('utf-8'))
    cmd_process.stdin.write('0.1\n'.encode('utf-8'))
    cmd_process.stdin.write('3\n'.encode('utf-8'))
    info, err = cmd_process.communicate()

    print(info.decode('gbk').split('\r\n'))
    print(err.decode('gbk').split('\r\n'))
