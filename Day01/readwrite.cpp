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

using namespace std;
int main() {
	fstream my_file;
	my_file.open("myfile", ios::app);
	if (!my_file) {
		cout << "File not created!\n";
	}
	else {
		cout << "File created successfully!\n";
        my_file << "This is some text\n";
		my_file.close(); 
	}

    my_file.open("myfile", ios::in);
    if (!my_file)
    {
        cout << "No such file";
    } 
    else
    {
        char ch;
        while(1) {
            my_file >> ch;
            if (my_file.eof())
            break;
            cout << ch;
        }
    }

    my_file.close();
    cout << "\nNext section\n";
    my_file.open("myfile", ios::in);
    if (!my_file){
        cout << "No such file\n";
    } else {
        string line;
        int i {0};
        while (getline(my_file, line)){
            cout << i << " ";
            cout << line;
            cout << "\n";
            i++;
        }
    }
    my_file.close();
	return 0;
}