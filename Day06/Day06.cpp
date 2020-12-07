#include <iostream>
#include <fstream>
#include <vector>
#include <string>

const char LETTERS[26] {'a','b','c','d','e','f',
            'g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z'};
std::vector <std::string> getData(std::string fileName);
int getCountOfAnyYes(std::vector <std::string> data);

int main(){
    std::cout << "hello\n";

    std::vector <std::string> data = getData("Day06.txt");
    
    // for(int i=0;i<data.size(); i++){
    //     std::cout << data[i] << "\n";
    // }

    int count = getCountOfAnyYes(data);

    std::cout << "Count of any yes answers: " << count << "\n";
}

std::vector <std::string> getData(std::string fileName) {
    std::fstream myfile;
    std::vector <std::string> data {};
    myfile.open(fileName, std::ios::in);
    if (!myfile){
       std::cout << "No Such File" << std::endl;
       return data;
    } else {
        std::cout << "File found" << std::endl;
    }
    std::string line;
    while(getline(myfile, line)){
        data.push_back(line);
    }
    return data;
}

int getCountOfAnyYes(std::vector <std::string> data){
    int count {0};
    std::string group {""};
    for(int i = 0; i < data.size(); i++){
        if (data[i].length() > 0){
            group += data[i];
        }
        else{
            // std::cout << "Group: " << group << "\n";
            for(int j = 0; j < 26; j++){              
                if (group.find(LETTERS[j]) != std::string::npos){
                    // std::cout << "Letter " << LETTERS[j] << " Group " << group << "\n";
                    count ++;
                }
            }
            group = "";
        }
    }
    return count;
}