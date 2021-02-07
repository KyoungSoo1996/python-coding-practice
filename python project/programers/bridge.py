def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    count = 0
    allSum = 0
    while True:
        if len(truck_weights) > 0:
            if allSum - bridge[0] + truck_weights[0] <= weight:
                allSum += truck_weights[0] - bridge[0]
                bridge.pop(0)
                bridge.append(truck_weights.pop(0))
            else:
                allSum -= bridge[0]
                bridge.pop(0)
                bridge.append(0)
            count += 1
        else:
            count += 1 
            allSum -= bridge[0]
            bridge.pop(0)
            bridge.append(0)
            if allSum == 0:
                return count
        if allSum == 0:
            count -= 1
    return count

testBridge_length = 5
testWeight = 5
testTruck_weights = [1,1,1,1,1,2,2,2,2]

print(solution(testBridge_length, testWeight, testTruck_weights))