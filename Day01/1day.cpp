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
    for (int x: expense_report)
        cout << x << endl;

    cout << "Now iterate through other list"<<endl;

    // Iterate through first list
    for (int i = 0; i < expense_report.size(); ++i)
    {
        // Iterate through second list
        // Search for value of i in second list
        // If it exists ->
        // i is first value and j is second
        for (int j = 0; j < expense_report_difference.size(); ++j)
        {
            if (expense_report[i] == expense_report_difference[j])
            {
                cout << expense_report[i] << "*" << expense_report[j];
                cout << "="<< expense_report[i] * expense_report[j];
                cout << endl;
            }
        }
    }
	return 0;
}