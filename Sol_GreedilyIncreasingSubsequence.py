def secuencia(orden):
    sec = [orden[0]] 
    for num in orden:
        if num > sec[-1]:  
            sec.append(num)
    return sec

def main():
    N = int(input())
    orden = list(map(int, input().split()))
    
    if len(orden) != N or len(set(orden)) != N or min(orden) < 1 or max(orden) > N:
        return
    
    sec = secuencia(orden)
    
    print(len(sec))
    print(' '.join(map(str, sec)))

def orden():
    return orden

if __name__ == "__main__":
    main()