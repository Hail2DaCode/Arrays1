//import { removeAt } from "codingProblems";
function removeBlanks(string) {
    let newString = "";
    for(let i = 0; i < string.length; i++) {
        if(string[i] !== " ") {
            newString += string[i];
        }
    }
    console.log(newString);
    return newString;
}
removeBlanks("Pl ayTha tF u nkyM usic");
removeBlanks("I can not BELIEVE it's not BUTTER");

function getDigits(string) {
    let integer = "";
    for(let i = 0; i < string.length; i++) {
        if(!isNaN(string[i])) {
            integer += string[i];
        }
    }
    console.log(Number(integer));
    return Number(integer);
}
getDigits("abc8c0d1ngd0j0!8");
getDigits("0s1a3y5w7j9a2t4?6!8?0");

let word = "B ri-an";
console.log(word.split('-'));

function acronyms(string) {
    let acronym = "";
    for(let i = 0; i < string.length; i++) {
        if (string[i] !== "." && string[i] !== "!" && string[i] !== "?"  && string[i] !== " ") {
            acronym += string[i];
        }
        while(string[i] !== " "  && string[i] !== "," && string[i] !=="-" && i !== string.length - 1 ) {
            i = i + 1;
        }
        //console.log(i);
        
    }
    console.log(acronym.toUpperCase());
    return acronym.toUpperCase();
}
acronyms("there's no free lunch - gotta pay yer way.");
acronyms("Live from New York, it's Saturday Night!");
function countNonSpaces(string) {
    let count = 0;
    for(let i = 0; i < string.length; i++) {
        if(string[i] !== " ") {
            count += 1;
        }
    }
    console.log(count);
    return count;
}
countNonSpaces("Honey pie, you are dirving me crazy");
countNonSpaces("Hello World!");

function removeShorterStrings(arrStr, val) {
    let count = 0;
    for(let i = arrStr.length - 1; i >= 0; i--) {
        if(arrStr[i].length < val) {
            count += 1;
            let j = i;
            const final = arrStr.length - 1;
            while(j < final) {
                let temp = arrStr[j];
                arrStr[j] = arrStr[j+1];
                arrStr[j + 1] = temp;
                j += 1;
            }
        }
    }
    console.log(count);
    console.log(arrStr.length);
    arrStr.length -= count;
    console.log(arrStr);
    return arrStr;
}
removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4);
removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3);
