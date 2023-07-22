#ifndef MOLIB
#define MOLIB
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
namespace mo{
    const long double PI=3.141592653589793238;
    const long double E=2.718281828459045235;
    const long double GOLDEN_RATIO=1.618033988749894848;
    const long double EULER_CONSTANT=0.577215664901532860;
    const long double sqrt1=1.000000000000000;
    const long double sqrt2=1.414213562373095;
    const long double sqrt3=1.732050807568877;
    const long double sqrt4=2.000000000000000;
    const long double sqrt5=2.236067977499790;
    const long double sqrt6=2.449489742783178;
    const long double sqrt7=2.645751311064591;
    const long double sqrt8=2.828427124746190;
    const long double sqrt9=3.000000000000000;
    const long double sqrt10=3.162277660168380;
    const long double sqrt11=3.316624790355400;
    const long double sqrt12=3.464101615137750;
    const long double sqrt13=3.605551275463990;
    const long double sqrt14=3.741657386773940;
    const long double sqrt15=3.872983346207420;
    struct kv {
        string value;
        string name;
    };
    struct Vector2D {
        double x;
        double y;
    };
    struct Vector3D {
        double x;
        double y;
        double z;
    };
    struct Date {
        int year;
        int month;
        int day;
    };
    void print(string param) {
        cout << param << endl;
    }
    int add(int a,int b) {
        return a+b;
    }
    int sub(int a,int b) {
        return a-b;
    }
    int mul(int a,int b) {
        return a*b;
    }
    double div(int a,int b) {
        if(b==0) {
            throw runtime_error("Division by zero is not allowed.");
        }
        return static_cast<double>(a)/b;
    }
    int mod(int a,int b) {
        return a%b;
    }
    bool isPrime(int n) { 
        if(n<=1) {
            return false;
        }
        for(int i=2;i*i<=n;++i) {
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
    template<typename T>
    void swap(T&a,T&b) {
        T temp=a;
        a=b;
        b=temp;
    }
    string input(string q) {
        string get;
        cout<<q;
        getline(cin,get);
        return get;
    }
    unsigned long long factorial(unsigned int n) {
        unsigned long long result=1;
        for(unsigned int i=1;i<=n;++i) {
            result*=i;
        }
        return result;
    }
    double sqrt(double x) {
        if(x>=0) {
            double guess=x;
            double epsilon=1e-7;
            while((guess*guess-x)>epsilon) {
                guess=(guess+x/guess)/2;
            }
            return guess;
        } else {
            throw runtime_error("Square root of negative number is not allowed.");
        }
    }
    double abs(double x) {
        if(x>=0){
            return x;
        } else { 
            return-x; 
        }
    }
    int strlen(const char*str) {
        int len=0;
        while(str[len]!='\0') {
            ++len;
        }
        return len;
    }
    void strcpy(char*dest,const char*src){
        int i=0;
        while(src[i]!='\0'){
            dest[i]=src[i];
            ++i;
        }
        dest[i]='\0';
    }
    void strcat(char*dest,const char*src){
        int destLen=strlen(dest);
        int i=0;
        while(src[i]!='\0'){
            dest[destLen+i]=src[i];
            ++i;
        }
        dest[destLen+i]='\0';
    }
#endif