import time

def bubble_sort(data, drawData, timeTick):
    for iter in range(len(data)-1):
        for index in range(len(data)-1):
            if data[index]>data[index+1]:
                data[index],data[index+1]=data[index+1],data[index]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)




    #for _ in range(len(data)-1):
        #for j in range(len(data)-1):
            #if data[j] > data[j+1]:
                #data[j], data[j+1] = data[j+1], data[j]
                #drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))] )

    drawData(data, ['green' for x in range(len(data))])
