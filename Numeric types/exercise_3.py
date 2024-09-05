#run timing
def run_timing():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input("Enter 10 km run time: ")
        
        #if run is empty, the loop stops
        if not one_run:
            break

        number_of_runs += 1
        total_time = float(one_run)

    try:
        average_time = total_time/number_of_runs
        print(f'Average of {average_time} over {number_of_runs}')
    except ZeroDivisionError:
        print('no entry made, exiting')

run_timing()