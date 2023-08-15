
//Push Front

function pushFront(arr, val) {
    arr.push(val);
    for (let i = arr.length - 1; i > 0; i--) {
        arr[i] = arr[i - 1];
        arr[i-1] = val;
    }
    console.log(arr);
    return arr;
}
pushFront([5,7,2,3], 8);
pushFront([99], 7);

function popFront(arr) {
    let temp = arr[0];
    for(let i = 1; i < arr.length; i++) {
        arr[i-1] = arr[i];
    }
    arr.length = arr.length -1;
    console.log(arr);
    console.log(temp);
    return temp;
}
popFront([0,5,10,15]);
popFront([4,5,7,9]);

var insertAt = function(arr, inx, val) {
    arr[arr.length] = val;
    for(let i = arr.length-1; i > inx; i--) {
        arr[i] = arr[i-1];
        arr[i-1] = val;
    }
    console.log(arr);
    return arr;
}
insertAt([100,200,5],2,311);
insertAt([9,33,7],1,42);

var removeAt = function(arr, inx) {
    let temp = arr[inx];
    for(let i = inx + 1; i <arr.length; i++) {
        arr[i-1] = arr[i];
    }
    arr.length = arr.length -1;
    console.log(arr);
    console.log(temp);
    return temp;
}
removeAt([1000,3,204,77],1);
removeAt([8,20,55,44,98],3);

function swapPairs(arr) {
    if (arr.length % 2 == 0) {
        for(let i = 0; i < arr.length; i += 2) {
            let temp = arr[i + 1];
            arr[i + 1] = arr[i];
            arr[i] = temp;
        }
        
    }
    else {
        for(let i = 0; i < arr.length - 1; i += 2) {
            let temp = arr[i + 1];
            arr[i + 1] = arr[i];
            arr[i] = temp;
        }
    }
    console.log(arr);
    return arr;
}
swapPairs([1,2,3,4]);
swapPairs(["Brendan", true, 42]);

function removeDupes(sortArr) {
    let memObject = {}
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === arr[i + 1]) {
            memObject[i] = i;
        }
    }
}