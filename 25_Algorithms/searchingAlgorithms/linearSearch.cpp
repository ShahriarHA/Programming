#include<iostream>
using namespace std;

int main() {
    int n, key;
    cout << "Enter the total number of elements in the array: ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements of the array: ";
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << "Enter the target element to be searched: ";
    cin >> key;
    int flag = 0;
    for(int i = 0; i < n; i++) {
        if(arr[i] == key) {
            cout << "Element found at index " << i << endl;
            flag = 1;
            break;
        }
    }
    if(flag == 0) {
        cout << "Element not found in the array." << endl;
    }
    return 0;
}