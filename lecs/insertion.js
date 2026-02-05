function insertion(arr) {
    
    for (let i = 2; i < arr.length; i++) {
        const key = arr[i]        
        let j = i - 1
        while(j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j]
            j = j - 1
        }
        arr[j+1] = key
    }

}
const unsorted = [5, 8, 1, 3, 7, 2]
insertion(unsorted)
console.log(unsorted)