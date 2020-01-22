import csv
import subprocess


def load_parameters(file_name):
    result = ' -m CE -p Kmedian -f ' + file_name
    return result


def write_in_csv(row_write_in):
    with open('.\out\data.csv', 'a+', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(row_write_in)


if __name__ == '__main__':
    cnt = 0
    dataset_list = ['banana.dat', 'phoneme.dat', 'ring.dat']
    sample_size_list = [5300, 5404, 7400]
    column_name_list = ['id', 'fileName', 'sampleSize', 'eliteSize', 'smoothParameter', 'iterationNumber',
                        'consumesTimes', 'optimalValue']
    for sample_count in range(len(dataset_list)):
        sample_size_now = sample_size_list[sample_count]
        for elite_ratio in range(1, 10):
            elite_size_now = int(sample_size_now * elite_ratio * 0.1)
            for smooth_ratio in range(1, 10):
                smooth_parameter_now = smooth_ratio * 0.1
                for iteration_ratio in range(1, 101):
                    iteration_number_now = iteration_ratio * 10
                    full_execute_parameters = '.\\OptCoreExecutable\\Opt.exe' + load_parameters(dataset_list[sample_count])
                    # print(full_execute_parameters)
                    cmd_process = subprocess.Popen(full_execute_parameters, shell=True,
                                                   stdin=subprocess.PIPE,
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE)
                    cmd_process.stdin.write((str(sample_size_now) + '\n').encode('utf-8'))
                    cmd_process.stdin.write((str(elite_size_now) + '\n').encode('utf-8'))
                    cmd_process.stdin.write((str(smooth_parameter_now) + '\n').encode('utf-8'))
                    cmd_process.stdin.write((str(iteration_number_now) + '\n').encode('utf-8'))
                    info, err = cmd_process.communicate()
                    print(err.decode('gbk'))
                    tmp1 = info.decode('gbk').split('\r\n')
                    consume_time = tmp1[0]
                    optimal_value = tmp1[1]
                    print(
                        str(sample_size_now) + ' ' + str(elite_size_now) + ' ' + str(smooth_parameter_now) + ' ' + str(
                            iteration_number_now)+ ' '+str(consume_time)+ ' '+str(optimal_value))
                    cnt = cnt+1
                    row_write = [cnt, dataset_list[sample_count], sample_size_now, elite_size_now, smooth_parameter_now,
                                 iteration_number_now, consume_time, optimal_value]
                    write_in_csv(row_write)