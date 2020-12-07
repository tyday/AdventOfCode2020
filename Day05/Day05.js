const { SSL_OP_SSLEAY_080_CLIENT_DH_BUG } = require("constants");
var fs = require("fs");

let getRow = (rowCode) => {
    rowCode = rowCode.replace(/F/g, "0");
    rowCode = rowCode.replace(/B/g, "1");
    return parseInt(rowCode,2);
}

let getColumn = (columnCode) => {
    columnCode = columnCode.replace(/L/g, "0");
    columnCode = columnCode.replace(/R/g, "1");
    return parseInt(columnCode,2);

}

let getSeatCode = (seatInfo) => {
    let row = getRow(seatInfo.substr(0,7));
    let column = getColumn(seatInfo.substr(7,9));
    return row * 8 + column;
}

let getMaximumValue = (seat_list) => {
    let maxValue = 0;
    for (let seat of seat_list) {
        const val = getSeatCode(seat);
        // console.log(val)
        if (val > maxValue) {maxValue = val};
    }
    return maxValue;
}

let getOccupiedSeats = (seat_list) => {
    let occupied_seats = []
    for (let seat of seat_list){
        occupied_seats.push(getSeatCode(seat))
    }
    return occupied_seats;
}
let getSeat = (seat_list) => {
    let maxValue = getMaximumValue(seat_list)
    let initialSeats = Array.from(Array(maxValue).keys())
    // let occupied_seats = getOccupiedSeats(seat_list)
    // console.log(occupied_seats)
    let count = 0;
    console.log("Init Seats ", initialSeats.length);
    for (let seat of seat_list){
        count +=1;
        let seatCode = getSeatCode(seat)
        let index = initialSeats.indexOf(seatCode);
        // console.log(seat, initialSeats[pos])
        if (index > -1)  {initialSeats.splice(index,1);}
        else {console.log('fuck')}
    }
    console.log("Reported seats ", count)
    return initialSeats;
}

let getSeat2 = (seatList) => {
    let maxValue = getMaximumValue(seat_list)
    let initialSeats = Array.from(Array(maxValue).keys())
    let occupied_seats = getOccupiedSeats(seat_list)

    initialSeats = initialSeats.filter((item)=>{
        return !occupied_seats.includes(item)
    })
    return initialSeats
}
// console.log(getRow('FBFBBFF'));
// console.log(getColumn('RLR'));
// console.log(getSeatCode('FBFBBFFRLR'));

// console.log(getMaximumValue(['FBFBBFFRLR','FBFBBFFRLR','FBFBBFFRLR']))

var data = fs.readFileSync('Day05.txt');
var seat_list = data.toString().split('\n')

console.log(getSeat(seat_list))