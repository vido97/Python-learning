#The task is to write a main and median filter function. 
#The median filter have to handle only one-dimensional signal with window size 3
# the first and the last element of the signal remain unchanged
#list generated by median filter is calculated by taking the median from the corresbonding item in the orginal list and its two adjacent items except the first and the last item.

def find_median(number1, number2, number3):
    if number1 < number2:
        smaller_number = number1
        larger_number = number2
    else:
        smaller_number = number2
        larger_number = number1
    if number3 < smaller_number:
        return smaller_number
    elif number3 > larger_number:
        return larger_number
    else:
        return number3

def median_filter(signal):
    filtered_signal = []
    if len(signal) != 0:
        filtered_signal.append(signal[0])
        if len(signal) ==1:
            return filtered_signal
        for i in range (len(signal)-2):
            first_number= signal[i]
            second_number = signal[i+1]
            third_number = signal[i+2]
            median=find_median(first_number, second_number, third_number)
            filtered_signal.append(median)

        filtered_signal.append(signal[len(signal)-1])
    return filtered_signal

def main():
    original_signal = []
    data_point = input("Enter the data points of the signal. Stop with empty line.\n")
    while data_point != "":
        original_signal.append(float(data_point))
        data_point = input()    

    print("The original signal is",original_signal)
    print("The median filtered signal is", median_filter(original_signal))

main()
