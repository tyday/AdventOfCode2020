/*************************
/https://adventofcode.com/2020/day/1
Day 1 of Advent of Code

Need to learn all the things in C++

How to open a file
/https://www.guru99.com/cpp-file-read-write-open.html
**************************/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool inList(vector <int> data, int subject){
    for(auto i : data){
        if (subject == i)
            return true;
    }
    return false;
}

int main() {
	fstream my_file;
    vector <int> expense_report;
    vector <int> expense_report_difference;
	
    my_file.open("1day.txt", ios::in);
    if (!my_file){
        cout << "No such file\n";
    } else {
        string line;
        while (getline(my_file, line)){
            expense_report.push_back(stoi(line));
            int difference;
            difference = 2020 - stoi(line);
            expense_report_difference.push_back(difference);
        }
    }
    my_file.close();

    // Iterate through first list
    // Part One
    // for (auto i: expense_report){
    //     int difference;
    //     difference = 2020 - i;
    //     if (inList(expense_report, difference)){
    //         cout << i << " * " << difference;
    //         cout << " = " << i * difference << endl;
    //     }
    // }

    // Part Two
    for (auto i: expense_report){
        int bc;
        bc = 2020 - i;

        for(auto j: expense_report){
            int difference;
            difference = bc - j;
            if (inList(expense_report, difference)){
                cout << i << " * " << j << " * " << difference << " = ";
                cout << i * j * difference << endl;
            }
        }
    }
    
	return 0;
}