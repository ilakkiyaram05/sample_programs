bool checkGoodInteger(int n) {
    int s1 = 0; // To store digitSum
    int s2 = 0; // To store squareSum
    int n1;     // To store the current digit

    // We use a temporary variable so we don't modify 'n' 
    // (though in this specific case, modifying n is usually fine)
    long tempN = n;

    while (tempN > 0) {
        n1 = tempN % 10;      // Get the last digit
        tempN = tempN / 10;   // Remove the last digit
        s1 += n1;             // Add to digitSum
        s2 += (n1 * n1);      // Add to squareSum
    }

    // Return true if the difference is 50 or more, else return false
    if (s2 - s1 >= 50) {
        return true;
    } else {
        return false;
    }
}
