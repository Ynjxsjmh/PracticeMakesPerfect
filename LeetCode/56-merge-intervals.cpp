vector<Interval> merge(vector<Interval>& intervals) {
    sort(intervals.begin(), intervals.end(), judge);
    vector<Interval> result;

    if (intervals.size() >= 1) {
        result.push_back(intervals[0]);
    }

    for (int i = 1; i < intervals.size(); i++) {
        if (result.back().end < intervals[i].start) {
            result.push_back(intervals[i]);
        } else {
            result.back().end = max(result.back().end, intervals[i].end);
        }
    }

    return result;
}

static bool judge(Interval a, Interval b) {
    return (a.start < b.start);
}