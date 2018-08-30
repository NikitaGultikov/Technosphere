#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <array>
#include <cstdlib>
#include <algorithm>

bool is_file_exists(const char* path)
{
    bool is_exist = false;
    std::ifstream file(path);

    if(file.is_open())
        is_exist = true;

    file.close();
    return is_exist;
}

std::string get_new_file_path(const char* path)
{
    int max_num = 57;
    std::string s(path);
    std::string new_s;
    for(int i = 49; i <= max_num; i++){
        new_s = s + char(i);
        if(!is_file_exists(new_s.c_str()))
            return new_s;
    }
    new_s = s + '1';
    return get_new_file_path(new_s.c_str());
}

///true == std::less(<), false == std::greater(>)
template<bool sign>
bool comp_func(const std::string& a, const std::string& b)
{
    return sign ? a < b: a > b;
}

///true == std::less(<), false == std::greater(>)
template<bool sign>
bool comp_func_int(const std::string& a, const std::string& b)
{
    return sign ? (atoi(a.c_str()) < atoi(b.c_str())):
                  (atoi(a.c_str()) > atoi(b.c_str()));
}

int main(int argc, char *argv[])
{
    const char* brief_doc = "Program for sorting lines in a file in C++.\n"
                            "Input data comes from a file, the result of sorting is written to another_file.\n"
                            "Provide two additional arguments:\n"
                            "    -n - the data in the file will be interpreted as numbers and sorted as numbers.\n"
                            "    -r - sorting will be done in the reverse order.\n\n"
                            "Samples:   ./sort_lines file_name -r\n"
                            "           ./sort_lines file_name -n\n"
                            "           ./sort_lines file_name -n -r\n";

    std::vector<int> command_nums;  /// "-n" == 0 ; "-r" == 1

    ///input validation
    {
        const size_t num_of_add_args = 2;
        const std::array<std::string, num_of_add_args> args_list = {"-n", "-r"};
                                                              /// "-n" == 0 ; "-r" == 1
        if(argc < 2 || argc > 4){
            std::cerr << "Invalid arguments.\n\n"<<brief_doc;
            return 1;
        }

        bool is_it_find = false;
        int prev_command = -1;
        for(int i = 2; i < argc; i++){
            is_it_find = false;
            for(int j = 0; j < int(num_of_add_args); j++){
                if(argv[i] == args_list[j]){
                    is_it_find = true;
                    if(prev_command != j){
                        command_nums.push_back(j);
                        prev_command = j;
                    }
                    break;
                }
            }
            if(!is_it_find){
                std::cerr << "Invalid arguments.\n\n"<<brief_doc;
                return 1;
            }
        }
    }

    std::ifstream file(argv[1]);
    if(!file.is_open()){
        std::cerr << "Can't open file.\n\n"<<brief_doc;
        return 1;
    }

    ///write lines from file to container
    std::vector<std::string> container;
    while(file.good()){
        std::string s;
        file >> s;
        container.push_back(s);
    }
    file.close();

    ///command processing
    bool val = true;
    bool sign = true;
    for(auto i = command_nums.begin(); i != command_nums.end(); i++){
        switch(*i){
            case 0: ///"-n"
                val = false;
                break;
            case 1: ///"-r"
                sign = false;
                break;
        }
    }



    ///find new file path for new_file and open it
    std::string new_path = get_new_file_path(argv[1]);
    std::cout << "New file_name: " << new_path << std::endl;
    std::ofstream new_file(new_path.c_str());
    if(!new_file.is_open()){
        std::cerr << "Can't open new_file.\n\n"<<brief_doc;
        return 1;
    }

    ///sort lines
    if(sign){
        if(val)
            std::sort(container.begin(), container.end(), comp_func<true>);
        else
            std::sort(container.begin(), container.end(), comp_func_int<true>);
    }
    else{
        if(val)
            std::sort(container.begin(), container.end(), comp_func<false>);
        else
            std::sort(container.begin(), container.end(), comp_func_int<false>);
    }

    ///write sorted lines in new_file
    for(auto i = container.begin(); i != container.end(); i++){
        new_file << *i << std::endl;
    }
    new_file.close();

    return 0;
}
