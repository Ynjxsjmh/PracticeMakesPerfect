string PrintMinNumber(vector<int> numbers) {
    string result = "";

    sort(numbers.begin(), numbers.end(), compare);

    for (int num : numbers) {
        result += to_string(num);
    }

    return result;
}

static bool compare(int a, int b) {
    string m = to_string(a) + to_string(b);
    string n = to_string(b) + to_string(a);

    return m < n;
}