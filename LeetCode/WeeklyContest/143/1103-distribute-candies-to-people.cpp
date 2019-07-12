vector<int> distributeCandies(int candies, int num_people) {
    vector<int> result(num_people, 0);
    int i = 1;
    int id = 0;

    while (candies >= 0) {
        if (candies - i < 0) {
            result[id] += candies;
        } else {
            result[id] += i;
        }
        candies -= i;

        i++;
        id = (id+1) % num_people;
    }

    return result;
}