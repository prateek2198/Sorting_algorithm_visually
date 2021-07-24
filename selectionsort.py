import time
def selection_Sort(data,drawData,timeTick):

    for i in range(len(data)):
        min_x = i

        for item in range(i+1, len(data)):
            if data[item] < data[min_x]:
                min_x = item

        data[i], data[min_x] = data[min_x], data[i]
        drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))] )
        time.sleep(timeTick)
