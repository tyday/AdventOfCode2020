var fs = require("fs");



 





var data = fs.readFileSync('test_input.txt');
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