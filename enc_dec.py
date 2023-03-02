def decimal_to_binary(number):

    bin_list = []
    quotient = number
    while quotient >= 1:
        rem =  quotient%2
        bin_list.append(str(rem))
        quotient = quotient//2
    return bin_list


def slicing_of_binary_list(binary_list):

    if len(binary_list) % 6 != 0:
        rem = len(binary_list) % 6
        num_of_zeroes = 6 - rem
        binary_list = binary_list + [str(0)] * num_of_zeroes
        binary_list = binary_list

    else:
         binary_list = binary_list

    bits_list = []
    start_cur = 0
    end_cur = 6
    for bits in  binary_list :
        slice_result = binary_list[start_cur:end_cur]
        if end_cur > len(binary_list):
            break

        start_cur += 6
        end_cur +=6
        bits_list.append(slice_result)

    return bits_list


def binary_to_decimal(bin_array):

    count = 0
    decimal_num = 0
    for i in bin_array[::-1]:
        decimal_con = int(i) * 2**count
        decimal_num += decimal_con
        count = count+1
    return decimal_num


def encode_characters(decimal_arr):

    charac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    encoded_chars = ''
    for number in decimal_arr:
        char_index_val = charac[number]
        encoded_chars += char_index_val
    return encoded_chars


def decode_char(stng):

    charac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    decimal_lis = []
    for stn in stng:
        decimal_num = charac.index(stn)
        decimal_lis.append(decimal_num)
    return decimal_lis


def truncate_bits_by_slicing(binary_list):

    if len(binary_list) % 8 != 0:
        rem = len(binary_list) % 8
        num_of_zeroes = 8 - rem
        binary_list = binary_list + [str(0)] * num_of_zeroes
        binary_list = binary_list

    else:
         binary_list = binary_list

    bits_list = []
    start_cur = 2
    end_cur = 8
    for bits in  binary_list :
        slice_result = binary_list[start_cur:end_cur]
        if end_cur > len(binary_list):
            break

        start_cur += 8
        end_cur +=8
        bits_list+= slice_result

    return bits_list


def slicing_of_binary_list_into_8bits(bin_array):

    binary_lis = []
    start_cur = 0
    end_cur = 8
    for bits in bin_array:
        slice_res = bin_array[start_cur:end_cur]
        if end_cur > len(bin_array):
            break
        start_cur += 8
        end_cur +=8

        binary_lis.append(slice_res)
    return binary_lis


if __name__ == '__main__':
    lis_of_bin = []
    stng = 'Ma'
    for char in stng:
        unicode_val = ord(char)
        binary_num = decimal_to_binary(unicode_val)
        binary_num = binary_num + [str(0)] * (8-len(binary_num))
        lis_of_bin += binary_num[::-1]
    result1 = lis_of_bin
    result2 = slicing_of_binary_list(result1)
    result3 =[binary_to_decimal(binary_array) for binary_array in result2]
    encoded_characters = encode_characters(result3)
    print(encoded_characters)
    result5 = decode_char(encoded_characters)
    lis_of_bin = []
    for num in result5:
        binary_num = decimal_to_binary(num)
        binary_num = binary_num + [str(0)] * (8-len(binary_num))
        lis_of_bin += binary_num[::-1]
    result6 = lis_of_bin
    result7 = truncate_bits_by_slicing(result6)
    result8 = slicing_of_binary_list_into_8bits(result7)
    result9 = [binary_to_decimal(binary_array) for binary_array in result8]
    decoded_characters = ''
    for ele in result9:
        decoded_characters += chr(ele)
    print(decoded_characters)




