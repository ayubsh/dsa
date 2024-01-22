# SORTING

sorting (permutation) refers to bringing a set of items into some well-defined
order. To be able to do this, we first need to specify the notion of order on the items we are
considering [1,4,5 2,1,8] decending => [1,1,2,4,5,8]

## Diffentent ways of sorting
 -  insertion sort
 - bubble sort
 - merge sort
 - quick sort

## insertion sort
It starts by treating the first
entry a[0] as an already sorted array, then checks the second entry a[1] and compares it with
the first. If they are in the wrong order, it swaps the two. That leaves a[0],a[1] sorted.
Then it takes the third entry and positions it in the right place, leaving a[0],a[1],a[2]
sorted, and so on. M

![insertion sort gif](./insertion.gif)

[1,4,5 2,1,8]
[1] 4 => [1,4] => 5 => [1,4,5] => 2 => [1,2,4,5...]

```javascript
function insertion(arr){
    for(i = 2; i < arr.length; i++){
        let key = arr[i]
        let j = i - 1

        while(j >= 0 && arr[j] > key){
            arr[j+1] = arr[j]
            j = j - 1
        }
        arr[j+1] = key
    }
}
```