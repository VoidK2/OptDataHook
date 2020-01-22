import csv
import subprocess
# import threading
# import queue
#线程优先级队列


def load_parameters(file_name):
    result = ' -m CE -p Kmedian -f ' + file_name
    return result


def write_in_csv(row_write_in, file_name):
    file_path_tmp = file_name.split('.')
    file_path = file_path_tmp[0]
    with open(file_path, 'a+', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(row_write_in)

# def sub_process_thread():


if __name__ == '__main__':
    cnt = 0
    # threading_limit = int(input("运行数据集"))
    dataset_list = ['appendicitis.dat', 'banana.dat', 'phoneme.dat', 'ring.dat']
    sample_size_list = [106, 5300, 5404, 7400]
    column_name_list = ['id', 'fileName', 'sampleSize', 'eliteSize', 'smoothParameter', 'iterationNumber',
                        'consumesTimes', 'optimalValue']
    interation_list = [1,10,100,500,1000]
    for sample_count in range(len(dataset_list)):
        # sample_count = threading_limit
        sample_size_now = sample_size_list[sample_count]
        for elite_ratio in range(1, 11):
            elite_size_now = int(sample_size_now) * int(elite_ratio * 0.1)
            for smooth_ratio in range(1, 10):
                smooth_parameter_now = smooth_ratio * 0.1
                for iteration_ratio in range(1, 101):
                    iteration_number_now = iteration_ratio * 10
                    full_execute_parameters = '.\\OptCoreExecutable\\Opt.exe' + load_parameters(dataset_list[sample_count])
                    print(full_execute_parameters)
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
                            iteration_number_now) + ' '+str(consume_time)+ ' '+str(optimal_value))
                    cnt = cnt+1
                    row_write = [cnt, dataset_list[sample_count], sample_size_now, elite_size_now, smooth_parameter_now,
                                 iteration_number_now, consume_time, optimal_value]
                    file_name = str(dataset_list[sample_count])
                    write_in_csv(row_write,file_name)