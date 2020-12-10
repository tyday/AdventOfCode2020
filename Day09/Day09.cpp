// Does not work

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::vector <long long> getData(std::string fileName);
long long findWeakPoint(std::vector<long long> &data, long long preambleLength);
bool cantFindMatch(std::vector <long long> &data, long long target);

int main(){

    std::vector <long long> data = getData("/home/pi/Programming/AdventOfCode/2020/Day09/input.txt");
    long long response = findWeakPoint(data,25);
    std::cout << "Answer: " << response << "\n";
}

std::vector <long long> getData(std::string fileName){
    std::ifstream myfile;
    std::vector<long long> data{};
    myfile.open(fileName, std::ios::in);
    if(!myfile){
        std::cout << "Cannot find file: " << fileName << "\n";
        return data;
    }
    std::string line;
    while(getline(myfile, line)){
        data.push_back(std::stoll(line));
    }
    std::cout << "File loaded: " << fileName << "\n";
    myfile.close();
    return data;
}

bool cantFindMatch(std::vector <long long> &data, long long target){
    for(int i = 0; i < data.size(); i++){
        std::vector <long long> sub_data = data;
        long long val = sub_data[i];
        sub_data.erase(sub_data.begin()+i);
        for(int j=0; j<sub_data.size(); j++){
            if (val +sub_data[j] == target)
                return false;
        }  
    }
    return true;
}

long long findWeakPoint(std::vector<long long> &data, long long preambleLength){
    int i = preambleLength;
    while( i <data.size()){
        long long target_value = data[i];
        std::vector<long long> sub_list{};
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