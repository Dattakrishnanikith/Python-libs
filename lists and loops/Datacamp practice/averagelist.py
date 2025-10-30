
def average(values:list):

    avg_value = sum(values)/ len(values)

    #round the results

    rounded_average = round(avg_value,2)

    return rounded_average

My_list = [2,5,8,11,51,101,46,101]
print (average(My_list))