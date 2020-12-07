const { group } = require("console");
var fs = require("fs");



function ascii_lowercase () { // eslint-disable-line camelcase
//   original by: Yury Shapkarin (https://shapkarin.me)
//   example 1: ascii_lowercase()
//   returns 1: 'abcdefghijklmnopqrstuvwxyz'
const length = 26
let i = 65 + length + 6
return [...Array(length)]
    .reduce(function (accumulator) {
    return accumulator + String.fromCharCode(i++)
    }, '')
}

const LETTERS = ascii_lowercase()


let any_yes_answer = (data) => {
    let count = 0
    let group = ''
    data.forEach((item)=>{
    if(item.length > 0)
        group += item;
    else{
        for(i=0; i < LETTERS.length; i++){
            if (group.indexOf(LETTERS[i]) > -1)
                count ++; 
        }
        group = ''
    }
})}

let letter_in_all_lists = (letter, lists) => {
    letter_in_all = true;
    lists.forEach((l) => {
        if (!l.includes(letter)){
            letter_in_all = false;
            return false;
        }
    })
    return letter_in_all;
}

let get_any_yes = (data) => {
    let count = 0;
    let group = ''
    data.forEach((item)=>{
        if(item.length > 0)
            group += item
        else {
            for(let i = 0; i < LETTERS.length; i++){                
                if(group.indexOf(LETTERS[i])> -1){
                    count ++;
                }                
            }
            group = ''
        }
    })
    return count
}

let get_all_yes = (data) => {
    let group_list = [];
    let count = 0;
    data.forEach((line)=>{
        if(line.length > 0)
            group_list.push(line);
        else{
            let local_count = 0;
            first_item = group_list[0];
            for(let i=0; i < first_item.length; i++){
                if(letter_in_all_lists(first_item[i],group_list)){
                    local_count += 1;
                }
            }
            // console.log(group_list, local_count)
            count += local_count;

            local_count = 0;
            group_list = [];
        }
    })
    return count;
}
var data = fs.readFileSync('Day06.txt');
data = data.toString().split('\n')

// console.log(data)
console.log(get_any_yes(data))
console.log(get_all_yes(data))