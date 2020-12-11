var fs = require("fs");

let adapter_dict = {}
let search_adapters = (index) => {
    if (adapter_dict[index] !== undefined){
        return adapter_dict[index];
    }
    else if (index === data.length-1){
        // Success! We've hit the last node
        return 1;
    }
    else if (index >= data.length){
        // We've gone too far
        return 0;
    }
    else {
        // We take the next three indexes on the list
        let a = index +1;
        let b = index +2;
        let c = index +3;
        current_targets = [data[index] +1,data[index] +2,data[index] +3]
        let val_a = 0;
        let val_b = 0;
        let val_c = 0;

        if(current_targets.includes(data[a])){
            val_a = search_adapters(a);
        }
        if((index+2 < data.length) && (current_targets.includes(data[b]))){
            val_b = search_adapters(a);
        }
        if((index+3 < data.length) && (current_targets.includes(data[c]))){
            val_c = search_adapters(a);
        }
        let current_values = val_a + val_b + val_c;
        adapter_dict[index] = current_values;
        return current_values;
    }
}

 





var data = fs.readFileSync('/home/pi/Programming/AdventOfCode/2020/Day10/test_input.txt');
data = data.toString().split('\n')
data.push('0');
data = data.map(x => Number(x));
data = data.sort((a,b)=> a-b)

let volt_dict = {1:0,3:1};
previous_voltage = 0;

data.forEach(adapter =>{
    let volt_difference = adapter - previous_voltage;
    previous_voltage = adapter

    if (volt_dict[volt_difference] !== undefined){
        volt_dict[volt_difference] += 1;
    }
    else {
        volt_dict[volt_difference] =1;
    }
})

data.push(data.slice(-1)[0]+ 3);
console.log(data)
console.log(volt_dict)

let start = Date.now();
console.log(search_adapters(0));
console.log(adapter_dict);
let time = Date.now() - start;
console.log(time);