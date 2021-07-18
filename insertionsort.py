import time


def insertion_sort(data, drawData, timeTick):
    #for iter in range(len(data)-1):
        for i in range(1,len(data)):
            key = data[i]
            last = i-1
            while last>=0 and key<data[last]:
                data[last+1]=data[last]
                last = last-1
                data[last+1]=key
            #if data[index]>data[index+1]:
                #data[index],data[index+1]=data[index+1],data[last]

                drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
        drawData(data, ['green' for x in range(len(data))])
