#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::vector <int> getData(std::string fileName);
int findWeakPoint(std::vector<int> data, int preambleLength);

int main(){

    std::vector <int> data = getData("/home/pi/Programming/AdventOfCode/2020/Day09/input.txt");
    int response = findWeakPoint(data,25);
    std::cout << "Answer: " << response << "\n";
}

std::vector <int> getData(std::string fileName){
    std::fstream myfile;
    std::vector<int> data{};
    myfile.open(fileName, std::ios::in);
    if(!myfile){
        std::cout << "Cannot find file: " << fileName << "\n";
        return data;
    }
    std::string line;
    while(getline(myfile, line)){
        data.push_back(std::stoi(line));
    }
    std::cout << "File loaded: " << fileName << "\n";
    myfile.close();
    return data;
}

bool cantFindMatch(std::vector <int> data, int target){
    for(int i = 0; i < data.size(); i++){
        std::vector <int> sub_data = data;
        int val = sub_data[i];
        sub_data.erase(sub_data.begin()+i);
        for(int j=0; j<sub_data.size(); j++){
            if (val +sub_data[j] == target)
                return false;
        }  
    }
    return true;
}

int findWeakPoint(std::vector<int> data, int preambleLength){
    int i = preambleLength;
    while( i <data.size()){
        int target_value = data[i];
        std::vector<int> sub_list{};
        // sub_list = data[i-preamble_length:i]
        for(int j=i-preambleLength; j<i; j++){
            sub_list.push_back(data[j]);
        }
        // for (auto i: sub_list)
        //     std::cout << i << ' ';
        // std::cout<< "\n";
        if (cantFindMatch(sub_list,target_value))
            return data[i];
        i++;
    }
    return -1;
}