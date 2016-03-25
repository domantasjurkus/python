def GasStation(strArr):
    # how many stations do we have?
    station_num = int(strArr[0])

    # check wheter argument is valid
    if len(strArr)-1 != station_num:
        print "invalid argument"
        return -1
    
    # make a simplified array contaning the fuel values
    array = []
    for element in strArr[1:]:
        data = element.split(":");
        fuel = int(data[0])
        road = int(data[1])
        array.append(fuel - road)

    print "Checking variant", array

    # start from each station
    for start_ind in range(station_num):
        
        # if we can't make it to the next station - don't check this one
        if array[start_ind] < 0:
            continue
        
        # how much fuel we have from the start
        fuel = array[start_ind]
        
        # next station index - if it's the last station + 1, make is station 0
        next_ind = (start_ind+1) % station_num
        out_of_fuel = False
        
        # while we haven't reached the station from which we started
        # start the journey!
        while next_ind != start_ind:
            fuel += array[next_ind]
            if fuel < 0:
                out_of_fuel = True
                # end the journey...
                break

            # check the next station
            next_ind = (next_ind+1) % station_num
            
        if not out_of_fuel:
            #print "Starting from", start_ind, "works!"
            return start_ind

    # if we haven't found a good station
    return "impossible"


s1 = ["4", "3:1", "2:2", "1:2", "0:1"]
s2 = ["6", "0:1", "0:2", "30:2", "0:1", "3:2", "3:2"]
s3 = ["5", "0:6", "1:2", "0:1", "0:1", "30:6"]
s4 = ["2", "3:1", "2:2", "1:2", "0:1"]
s5 = ["4", "2:3", "3:4", "1:2", "0:1"]

print GasStation(s1)
print GasStation(s2)
print GasStation(s3)
print GasStation(s4)
print GasStation(s5)
