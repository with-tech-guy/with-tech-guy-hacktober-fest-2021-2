def removeDuplicate(arr): 
    result = []
    for i in arr:
        if i in result:
            continue
        else:
            result.append(i) 
    return result     

def main():
    arr = [1, 1, 3, 2, 1, 4, 5, 4]
    result = removeDuplicate(arr)
    print(" ".join([str(res) for res in result]))    
    
if __name__ == "__main__":
    main()
