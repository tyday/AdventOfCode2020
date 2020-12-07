#include <iostream>
#include <fstream>
// #include <string>
#include <vector>

using namespace std;

// int count_tree_encounters(char toboggan_map[2][2], int rise, int run, int height, int width){
//     int tree_encounters {0};


//     return tree_encounters;
// }

void get_width_height(fstream &myfile, int &width, int &height){
    string line;
    width = 0;
    height = 0;
    while (getline(myfile,line)){
        height ++;
        width = line.size();
    }
}
int main(){
    fstream myfile;
    myfile.open("3Day.txt", ios::in);
    if (!myfile){
        cout << "No file found\n";
        return 0;
    }
    else {
        cout << "File found\n";
    }
    

    int width, height;
    get_width_height(myfile, width, height);
    cout << width << " x " << height;

    string toboggan_map[height][width];

    string line;
    int i {0};
    // myfile.open("3Day.txt", ios::in);
    while (getline(myfile, line)){
        cout << "words" << line;
        for (int j = 0; j < line.size(); j++){
            toboggan_map[i][j] = line[j];
            
        }
        i++;
    } 

    int tree_encounters {0};
    int position_x {0};
    int position_y {0};
    int rise {1};
    int run{3};

    while(position_y < height){
        cout << toboggan_map[position_y][position_x] << endl;
        if (toboggan_map[position_y][position_x] == ".")
            tree_encounters ++;
        position_y += rise;
        position_x += run;
        while (position_x > width)
            position_x -= width;
    }
    cout << tree_encounters << endl;


    myfile.close();
    return 0;
}