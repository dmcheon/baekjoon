import copy

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    time_bridge = []
    
    while truck_weights:
        answer += 1
        time_bridge = [x + 1 for x in time_bridge]
        copy_time_truck_on_bridge = copy.deepcopy(time_bridge)
        
        for i, time in enumerate(copy_time_truck_on_bridge):
            if time > bridge_length:
                time_bridge.pop(i)
                bridge.pop(i)
                
        truck = truck_weights[0]        
        if sum(bridge) + truck <= weight and len(bridge) + 1 <= bridge_length:
            bridge.append(truck)
            time_bridge.append(1)
            truck_weights.pop(0)
    
    answer += bridge_length         
    return answer