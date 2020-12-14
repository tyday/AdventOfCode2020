#include <iostream>
#include <fstream>
#include <vector>

int main(){
    // std::cout<< "Hello"<< "\n";
    std::ifstream inputFile("/home/pi/Programming/AdventOfCode/2020/Day13/13.in", std::ios::in);
    std::string line;
    std::string busInfo;
    int timestamp;
    if(getline(inputFile,line))
        timestamp = std::stoi(line);
    if(getline(inputFile,line))
        busInfo = line;
    size_t pos{0};
    std::string element;
    size_t i {0};
    std::vector<std::string> busInfoList {};
    while((pos = busInfo.find(",")) != std::string::npos){
        busInfoList.push_back(busInfo.substr(i,pos));
        busInfo.erase(0, pos+1);
    }
    busInfoList.push_back(busInfo);
    std::cout << timestamp << "\n" << busInfo << "\n";

    for(auto i : busInfoList){
        std::cout << i<< "::";
    }
    std::cout << "\n";

    bool running = true;
    // int interval = -1;
    int earliest_time {-1};
    std::string busNumb{};
    for (std::string bus : busInfoList){
        if(bus != "x"){
            int j {0};
            while(j < timestamp){
                j += std::stoi(bus);
            }
            if(earliest_time == -1){
                earliest_time = j;
                busNumb = bus;
            }
            else if (j < earliest_time){
                earliest_time = j;
                busNumb = bus;
            }
            else {

            }

        }
    }
    std::cout << "Earliest time is: " << earliest_time << "\n";
    std::cout << "Bus number is: " << busNumb << "\n";
    std::cout << "Part One answer is: " <<( stoi(busNumb) * (earliest_time-timestamp))<< "\n";

}