extern "C" {
    int add(int a, int b){
    return a + b;
  }
  
    int subtract(int a, int b){
      return a-b;
    }
    int multiply(int a, int b){
      return a * b;
    }
    int divide(int a, int b){
      if (b == 0) return 0; // avoid division by zero
      return a / b;
    }
    int modulo(int a, int b) {
      if (b == 0) return 0; // avoid division by zero
      return a % b;
    }
    int power(int a, int b) {
      return power(a, b);
    }
     int square(int a) {
       return a * a;
     }
  }