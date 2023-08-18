import random
from time import process_time

def find_h(k):
    h = 0
    for i in range(len(k)):
        for j in range(i+1, len(k)):
            if k[i] == k[j] or abs(k[i]-k[j]) == abs(i-j):
                h += 1
    
    return h

# h degerinin asgari duzeyde olmasi icin dizinin her indeksindeki deger farkli olacak 
# sekilde calisan metod
def random_restart(): 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    location_list = []
    
    for i in range(len(numbers)):
        rnd_index = random.randint(0, len(numbers)-1)
        location_list.append(numbers[rnd_index])
        numbers.remove(numbers[rnd_index])
        
    return location_list

def hill_climb():
    random_restart_c = 0
    swap_c = 0
    t_start = process_time()
        
    location_list = random_restart() # konum listesinin olusturulmasi
    
    h = find_h(location_list)
    new_location_list = []
    min_h = 1000
    while h != 0:  
        stuck = 1 # h'nin degisip degismedigini kontrole eden bayrak
        for i in range(8):
            original = location_list[i] # konum listesindeki orijinal degerin kaybolmamasi icin
            for j in range(8):
                location_list[i] = j+1
                current_h = find_h(location_list)
                if current_h < min_h:
                    stuck = 0
                    min_h = current_h
                    new_location_list = location_list[:] # daha iyi h degerli konum listesi
                    
            location_list[i] = original
        
        swap_c += 1
        location_list = new_location_list[:]
        h = find_h(location_list)
        
        if stuck == 1:
            swap_c -= 1
            random_restart_c += 1
            new_location_list = []
            min_h = 1000
            location_list = random_restart()
    
    t_end = process_time()
    return [random_restart_c, swap_c, t_end - t_start]

def main():
    print("Random Restart Count, Swap Count, Time")
    for i in range(15):
        print(hill_climb())

main()
