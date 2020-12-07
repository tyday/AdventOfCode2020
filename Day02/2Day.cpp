#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int getFirstNumber(string data){
    string output;
    for (string::size_type i = 0; i < data.size(); i++){
        // cout << data[i] << " " << typeid(data[i]).name() << endl;
        if (data[i] != '-'){
            output.push_back(data[i]);
        }
        else {
            i = data.size();
        }
    }
    return stoi(output);
}

int getSecondNumber(string data){
    string output;
    bool record {false};
    for (string::size_type i = 0; i < data.size(); i++){
        if (record){
            if (data[i] == ' '){
                return stoi(output);
            }
            else {
                output.push_back(data[i]);
            }
        } 
        else {
            if (data[i] == '-'){
                record = true;
            }
        }
    }
    return 0;
}

char getLetter(string data){
    string output;
    bool record {false};
    for (string::size_type i = 0; i < data.size(); i++){
        if (record){
            return data[i];
        }
        else {
            if (data[i] == ' '){
                record = true;
            }
        }
    }
    return ' ';
}

string getPassword(string data){
    string output;
    bool record {false};
    int space_count {0};
    for (string::size_type i = 0; i < data.size(); i++){
        if (record){
            output.push_back(data[i]);
        } else {
            if (data[i] == ' ')
                space_count ++;
            if (space_count == 2)
                record = true;
        }
    }
    return output;
}

bool password_check_one(int min, int max, char target, string password){
    int target_count {0};
    for (int i = 0; i < password.size(); i++){
        if (password[i] == target)
            target_count ++;
    }
    if( min <= target_count && target_count <= max){
        // cout << min << " " << max << "target count: " << target_count << endl;
        return true;
    }
    return false;
}

bool password_check_two(int min, int max, char target, string password){
    int target_count {0};
    if (password[min-1] == target)
        target_count ++;
    if (password[max-1] == target)
        target_count ++;
    if (target_count == 1)
        return true;
    return false;
}

int count_password_successes(vector <string> passwords){
    int success_count {0};
    for (auto i: passwords){
        int a,b;
        string password;
        char target;
        bool pass_check;

        a = getFirstNumber(i);
        b = getSecondNumber(i);
        target = getLetter(i);
        password = getPassword(i);
        pass_check = password_check_two(a,b,target,password);
        if (pass_check)
            success_count ++;

    }
    return success_count;
}

int main(){
    fstream myfile;
    vector <string> passwords;

    myfile.open("2Day.txt", ios::in);
    if (!myfile){
        cout << "No Such File" << endl;
    } else {
        cout << "File found" << endl;
    }
    
    // Iterate through file
    // Add each password to vector passwords
    string line;
    while(getline(myfile, line)){
        passwords.push_back(line);
    }

    // for (auto pw: passwords)
    //     cout << pw << endl;
    // int a,b;
    // string password;
    // char target;
    // a = getFirstNumber(passwords[0]);
    // b = getSecondNumber(passwords[0]);
    // target = getLetter(passwords[0]);
    // password = getPassword(passwords[0]);
    // cout << passwords[1]<< " " << a << " " << b << " " << target;
    // cout << " " << password << endl;
    // cout << "test: " << password_check_one(a,b,target,password) << endl;
    cout << "Successful passwords: " << count_password_successes(passwords) << endl;
}