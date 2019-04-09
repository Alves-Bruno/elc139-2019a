#include <algorithm>
#include <iostream>
#include <string>
#include <thread>
#include <mutex>
#include <omp.h>

int omp_get_thread_num();

class SharedArray {
private:
   char* array;
   int index;
   int size;
   std::mutex mutex;
   bool usemutex;
public:
   SharedArray(int n, bool use) : size(n), index(0), usemutex(use) {
      array = new char[size];
      std::fill(array, array+size, '-');
   }
   ~SharedArray() {
      delete[] array;
   }
   void addChar(char c) {
      if (usemutex) mutex.lock();
      array[index] = c;
      spendSomeTime();
      index++;
      if (usemutex) mutex.unlock();
   }
   int countOccurrences(char c) {
      return std::count(array, array+size, c);
   }
   std::string toString() {
      return std::string(array, size);
   }
private:
   void spendSomeTime() {
      for (int i = 0; i < 10000; i++) {
         for (int j = 0; j < 100; j++) {
            // These loops shouldn't be removed by the compiler
         }
      }
   }
};



class ArrayFiller {
private:
   static const int nThreads = 3;
   static const int nTimes = 20;
   SharedArray* array;
public:
   ArrayFiller(bool usemutex) {
      array = new SharedArray(nThreads * nTimes, usemutex);
   }
   void fillArrayConcurrently() {
      std::thread t[nThreads];
      for (int i = 0; i < nThreads; ++i)
         t[i] = std::thread(&ArrayFiller::run, this, 'A'+i);
      for (int i = 0; i < nThreads; ++i)
         t[i].join();
   }
   void printStats() {
      std::cout << array->toString() << std::endl;
      for (int i = 0; i < nThreads; ++i)
         std::cout << (char) ('A'+i) << "="
                   << array->countOccurrences('A'+i) << " ";
      std::cout << std::endl;
   }
   ~ArrayFiller() {
      delete array;
   }
private:
   void run(char c) {
      for (int i = 0; i < nTimes; i++) {
         array->addChar(c);
      }
   }
};



class ArrayFillerOMP {
private:
   static const int nThreads = 3;
   static const int nTimes = 20;
   SharedArray* array;
   int chunk;
public:
   ArrayFillerOMP(bool usemutex, int chunk) {
      array = new SharedArray(nThreads * nTimes, usemutex);
      this->chunk = chunk;
   }
   void fillArrayConcurrently() {

        #pragma omp parallel for schedule (static)
              for (int i = 0; i < nThreads * nTimes; ++i){
                      #pragma omp critical
                      array->addChar('A'+ omp_get_thread_num());
              }
   }
   void printStats() {
      std::cout << array->toString() << std::endl;
      for (int i = 0; i < nThreads; ++i)
         std::cout << (char) ('A'+i) << "="
                   << array->countOccurrences('A'+i) << " ";
      std::cout << std::endl;
   }
   ~ArrayFillerOMP() {
      delete array;
   }
private:

};


int main(int argc, char const *argv[]) {
   // std::cout << "Each thread should add its char to the array n times (n=20)" << std::endl;
   // std::cout << "Correct results should total exactly nThreads*nTimes chars" << std::endl;
   // std::cout << "Case 1: no mutex, default scheduling (expecting wrong results)" << std::endl;
   // ArrayFiller m1(false);
   // m1.fillArrayConcurrently();
   // m1.printStats();

   // std::cout << "Case 2: using mutex (expecting correct results)" << std::endl;
   // ArrayFiller m3(true);
   // m3.fillArrayConcurrently();
   // m3.printStats();

   std::cout << "```" << std::endl;
   std::cout << "Case : using OpenMP (expecting correct results)" << std::endl;
   // ArrayFillerOMP m4(false, atoi(argv[1]));
   ArrayFillerOMP m4(false, 20);
   m4.fillArrayConcurrently();
   m4.printStats();
   std::cout << "```" << std::endl << std::endl;

}
