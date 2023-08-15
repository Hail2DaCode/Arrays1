// Two Sums

var twoSums = function (nums, target) {
    let sum = 0;
    let idx = [];
    for (let i = 0; i <= nums.length-2; i++) {
        sum = nums[i] + nums[i+1];
        idx = [i, i+1];
        if (sum == target) {
            return idx;
        }
    }
    return "There is no sum";
};
var twoSums2 = function (nums, target) {
    for(let i = 0; i < nums.length; i++) {
        for(let j = i + 1; j < target.nums.length; j++) {
            if()
        }
    }
}
var nums = [2,7,11,15];
var target = 9;
let nums2=[3,2,4];
let target2 = 6;
let nums3 = [3,3];
let target3 = 6;
twoSums(nums, target);
console.log(twoSums(nums,target))
console.log(twoSums(nums2,target2))
console.log(twoSums(nums3,target3))

// Palindrome
let word1 ='123'
let word2 = '' + '3'
console.log(word2)
let num = 123
let word3 = `${num}`
console.log(word3)
console.log(typeof(word3))
console.log(word.length)
let word ='123'
for (let i = word.length - 1; i >=0; i--) {
    console.log(word[i]);
}

var isPalindrome = function(x) {
    let word = `${x}`;
    let word2 = '';
    for (let i = word.length - 1; i >= 0; i--) {
        word2 = word2 + word[i];
    };
    // console.log(word2);
    if (word2 === word) {
        return true
    }
    else {return false}
}
console.log(isPalindrome(121))
console.log(isPalindrome(10))
console.log(isPalindrome(-121))

// Roman to Integer

var romanToInt = function(s) {
    let roman = {
        I:1, V:5, X:10, L: 50, C: 100, D: 500, M:1000
    }
    let sum = 0;
    for (let i = 0; i < s.length; i++) {
        for (key in roman) {
            if (key === s[i]) {
                sum += roman[key];
            }
        }
    }
    for (let j = 0; j<s.length-1; j++) {
        if (s[j]=="I" && s[j+1]=="V") {
            sum -= 2;
        }
        if (s[j]=="I" && s[j+1]=="X") {
            sum -= 2;
        }
        if (s[j]=="X" && s[j+1]=="L") {
            sum -= 20;
        }
        if (s[j]=="X" && s[j+1]=="C") {
            sum -= 20;
        }
        if (s[j]=="C" && s[j+1]=="D") {
            sum -= 200;
        }
        if (s[j]=="C" && s[j+1]=="M") {
            sum -= 200;
        }
    }
    return sum;
}
let s = "MMXXIII"
console.log(romanToInt(s));

var longestCommonPrefix = function(strs) {
    let loop = true;
    let phrase = "";
    let word2 = "No matches"
    while (loop) {
    let letter = strs[0][0];
    console.log(letter);
    if (strs[0].length === 0 ){
        return phrase;
    }
    for (var i = 0; i < strs.length; i++) {
        if (letter === strs[i][0]) {
            let result = strs[i].slice(1, strs[i].length);
            strs[i] = result;
            console.log(strs[i])
            continue
        }
        else {return phrase}
    }
    phrase = phrase + letter;
    }
};
let arr1=["flow", "flow", "flower"]
let arr2 = ["dog", "racecar", "car"]
console.log(longestCommonPrefix(arr1))

let name1 = "Brian";
let name2 = "";
console.log(name2.length)
let result = name1.slice(1, name1.length);
console.log(result);
console.log(name1[0]);
console.log(name1.length);

// 20. Valid Parenthese--Leet Code

var is_valid = function(s) {
    if (s[0] === ')' || s[0] === ']' || s[0] === '}' || s.length % 2 !== 0) {
        return false
    }
    else {
        for (var i = 0; i < s.length; i = i + 2 ) {
            if (s[i] === '(' && s[i+1] === ')') {
                continue;
            }
            else if (s[i] === '[' && s[i+1] === ']' ) {
                continue;
            }
            else if (s[i] === '{' && s[i+1] === '}' ) {
                continue;
            }
            else {
                return false
            }
        }
        return true;
    }
}
var bracket = '(]'
console.log(bracket[1]);
console.log(is_valid(bracket));

// 21.  Research Nodes //

var needle = "needle";
var arr = [];
for (let i = 0; i < needle.length; i++) {
    console.log(needle[i]);
    arr.push(needle[i]);
    
}
console.log(arr);
let testArr = [];
console.log(testArr[0]);
var strStr =  function(haystack, needle) {
    var candidateIndex = [];
    var index = 0;
    var word = "";
    for (var j = 0; j < needle.length; j ++) {
        var num = 0;
        if (index != 0) {
            num += index;
        }
        for(var i = num; i  < haystack.length; i ++) {
            
            if (needle[j] === haystack[i]) {
                candidateIndex.push(i);
                index = i + 1;
                console.log(index);
                word += haystack[i];
                console.log(word);
                if (word == needle) {
                    console.log("success");
                    return candidateIndex[0];
                }
                break;
            }
            else {
                word = "";
                candidateIndex  = [];
            }
            
        }
    }
    // console.log(word);
    // if (word == needle) {
    //     console.log(candidateIndex[0]);
    //     return candidateIndex[0];
    // }
    
        console.log(-1);
        return -1;
    
}
strStr("Shine", "in");
strStr("sadbutsad", "sad");
strStr("leetcode", "leeto");
strStr("Sihine", "in");
// Algo for Easy 28; Above 1 does not work for last case
var strStr2 =  function(haystack, needle) {
    var candidateIndex = [];
    var index = 0;
    var word = "";
    for(var i = 0; i  < haystack.length; i ++) {
            
        if (needle[index] === haystack[i]) {
            candidateIndex.push(i);
            console.log(index);
            index += 1;
            word += haystack[i];
            console.log(word);
            if (word == needle) {
                console.log("success");
                return candidateIndex[0];
            }
            continue;
        }
        else {
            word = "";
            candidateIndex  = [];
            if (index > 0) {
                index -= 1;
            }
        }
        
    }
    console.log(-1);
    return -1;
}
strStr2("Shine", "in");
strStr2("sadbutsad", "sad");
strStr2("leetcode", "leeto");
strStr2("Sihine", "in");

//38 Easy Search Insert Position: O(log n)

var searchInsert = function(nums, target) {
    let firstIndex = 0;
    let lastIndex = nums.length - 1;
    if (target < nums[0]) {
        return 0;
    }
    if (target > nums[nums.length -1]) {
        return nums.length;
    }
    while (firstIndex <= lastIndex) {
        let middleIndex = Math.floor((firstIndex + lastIndex) / 2);

        if (nums[middleIndex] === target) {
            return middleIndex
        }
        else if (nums[middleIndex] < target & target < nums[middleIndex + 1]) {
            return middleIndex + 1
        }
        else if (nums[middleIndex] > target & target > nums[middleIndex -1]) {
            return middleIndex;
        }
        
        if (nums[middleIndex] > target) {
            lastIndex = middleIndex -1;
        }
        else {
            firstIndex = middleIndex + 1;
        }
    }
    return -1;
}
let numbers = [1,3,5,6];

console.log(searchInsert(numbers, 5));
console.log(searchInsert(numbers, 2));
console.log(searchInsert(numbers, 7));

// 58. Length of Last Word

var lengthOfLastWord = function(s) {
    var candidate = false;
    var count = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        
        if (s[i] != " " & count === 0) {
            candidate = true;
            count += 1;
        }
        else if (s[i] != " " & candidate) {
            count +=1;
        }
        else if (s[i] === " " & candidate) {
            return count;
        }
        
        }
        return count;
    }
console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord("  fly me  to  the moon  "));
console.log(lengthOfLastWord("luffy is still joyboy"));
// 66. Plus One

var plusOne = function(digits) {
    //let string = "";
    var array = [];
    for (var i = 0; i < digits.length; i++) {
        if (i === digits.length & i ===9) {
            for (var j = digits.length -1; j >= 0; j--) {
                if (digits[j] === 9 & j === 0) {
                    digits.splice(0,1, 1, 0 )
                }
                else if (digits.length)
            }
        }
        else if (i === digits.length - 1) {
            let num = digits[i];
            num += 1;
            array.push(num);
            console.log("first");
        }
        else {
            let num2 = digits[i];
            console.log("second");
            console.log(num2);
            array.push(num2);
        }
    }
    console.log(array);
    return array;
}
var plusOne2 = function(digits) {
    let array = [];
    let carry = false;
    for (var i = digits.length - 1; i >= 0; i--) {
        if (digits[digits.length -1] === 9) {
            while(digits[i] === 9) {
                if (i === 0) {
                    array.unshift(0);
                    array.unshift(1);
                    i -=1;
                }
                else {
                    array.unshift(0);
                    i -= 1;
                }
            }
        }
        else {
            if (i === digits.length - 1) {
                let num = digits[i];
                num += 1;
                array.unshift(num);
            }
            else if (carry) {
                let num = digits[i];
                num += 1;
                array.unshift(num);
                carry = false;
            }
            else {
                let num = digits[i];
                array.unshift(num);
            }
            

        }
    }
    console.log(array);
    return array;
}

plusOne2([1,2,3]);
plusOne2([4,3,2,1]);
plusOne2([9]);
plusOne2([9,9]);

function countMultiplesOf5() {
    let count = 0;
    for (let i = 512; i <= 4096; i++) {
        if (i % 5 === 0)  {
            console.log(i);
            count += 1;
        }
    }
    return count;
}

console.log(countMultiplesOf5());

function birthday(num1, num2) {
    const birthmonth = 12;
    const birthday = 1;
    if ((num1 === birthmonth && num2 === birthday) || (num1 === birthday && num2 === birthmonth)) {
        console.log("How did you know?");
    }
    else {
    console.log("Just another day....");
    }
}

birthday(10,15);
birthday(1,12);
birthday(12,1);

let firstName = "Brian";
let secondName = "Michael";
console.log(firstName.length);
console.log(secondName.length);

//67. Add Binary

var addBinary = function(a,b) {
    let size = 0;
    let string = "";
    let carry = false;
    let diff = Math.abs(a.length - b.length);
    if(a.length <= b.length) {
        size = a.length
        for(let i = size - 1; i >= 0; i--) {
            if(a[i] === 0 && b[i + diff] === 0) {
                if(carry && )
                string += 0;
            }
            else if (a[i] === 0 || b[i + diff] === 0) {
                string += 1;
            }
            else { 
                carry = true;
                string += 0;
            }
        }
    }
    else {
        size = b.length;
        for(let i = size - 1; i >= 0; i--) {
            if(a[i + diff] === 0 && b[i] === 0) {
                string += 0;
            }
            else if (a[i + diff] === 0 || b[i] === 0) {
                string += 1;
            }
            else { 
                carry = true;
                string += 0;
            }
        }
    }
}
var newName = "Brian";
newName = "M" + newName;
console.log(newName);
function double(arr){
    for(let i=0; i<arr.length; i++){
        arr[i]*=2
    }
    return arr
}
let arr=[1,2,3,4,5]
double(arr)
console.log(arr) //What gets console logged here?

function revArray(arr) {
    if(arr.length % 2 === 0) {
        let size = arr.length;
        let mid = arr.length / 2 - 1;
        for(let i = 0; i <= mid; i++)
    }
    else {

    }
}
