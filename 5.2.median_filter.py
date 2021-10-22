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
    if len(signal) ==1:
        filtered_signal.append(signal[0])
    else:
        filtered_signal.append(signal[0])
        i = 0
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
    print("Enter the data points of the signal. Stop with empty line.")
    data_point = input()
    if data_point != "":
        original_signal.append(data_point)
    while data_point != "":
        data_point = input()
        original_signal.append(data_point)
    original_signal.remove("")

    print("The original signal is",original_signal)
    print("The median filtered signal is", median_filter(original_signal))

main()