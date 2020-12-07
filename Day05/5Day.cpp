#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
// using namespace std;
int getRow(std::string row_code);
int getColumn(std::string column_code);
int getSeatCode(std::string seat_code);
int getMaximumCode(std::vector <std::string> seat_codes);

int main() {
    std::fstream myfile;
    std::vector <std::string> seat_codes;

    std::string seat_code = "FBFBBFFRLR";
    // std::cout << seat_code.substr(0,7) << std::endl;

    myfile.open("Day05.txt", std::ios::in);
    if (!myfile){
        std::cout << "No Such File" << std::endl;
    } else {
        std::cout << "File found" << std::endl;
    }

    std::string line;
    while(getline(myfile, line)){
        seat_codes.push_back(line);
    }
    // std::cout << getRow(seat_code.substr(0,7));
    // std::cout << getColumn(seat_code.substr(7,9))<<std::endl;
    std::cout << getSeatCode(seat_code)<<std::endl;
    std::cout << "Maximum seat code: " << getMaximumCode(seat_codes) << std::endl;
    return 0;
}

int getRow(std::string row_code){
    for(int i = 0; i < row_code.size(); i ++){
        std::replace(row_code.begin(), row_code.end(), 'F', '0');
        std::replace(row_code.begin(), row_code.end(), 'B', '1');
        // std::cout << row_code[i] << std::endl;
    }
    return std::stoi(row_code, nullptr, 2);
}

int getColumn(std::string column_code){
    for(int i=0; i < column_code.size(); i++){
        std::replace(column_code.begin(), column_code.end(), 'R', '1');
        std::replace(column_code.begin(), column_code.end(), 'L', '0');
        // std::cout << column_code[i] << std::endl;
    }
    return std::stoi(column_code, nullptr,2);
}

int getSeatCode(std::string seat_code){
    // std::cout << getRow(seat_code.substr(0,7));
    // std::cout << getColumn(seat_code.substr(7,9))<<std::endl;
    int column_code = getRow(seat_code.substr(0,7));
    int row_code = getColumn(seat_code.substr(7,9));
    return column_code * 8 + row_code;
}

int getMaximumCode(std::vector <std::string> seat_codes){
    // for(auto i= seat_codes.begin(); i < seat_codes.end(); ++i){
    int max_value = 0;
    for(auto i : seat_codes){
        int current_value = getSeatCode(i);
        if (current_value > max_value)
            max_value = current_value;
        
    }
    return max_value;
}