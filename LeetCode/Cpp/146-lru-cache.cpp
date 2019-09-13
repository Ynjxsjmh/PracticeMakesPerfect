// 标签：链表

/*
  主要实现storage中O(1)的Remove
  遍历大家所学过的数据结构，能够满足删除O(1)并且有顺序机制的恐怕只有Linked List了。
  但链表的局限性是，我要删除特定节点确实是O(1)，但通过头结点遍历到需要删除的节点，是O(N)的操作。这时候我们自然会思考有没有办法用O(1)的时间找到节点。答案是我们完全可以把链表中节点的reference存储在字典的value里，这样我们可以用O(1)的时间寻找到节点，并且用O(1)的时间进行删除。
 */

class LRUCache {
private:
    int _cap;
    list<pair<int, int>> _data;  // 前面的是最少使用的
    unordered_map<int, list<pair<int, int>>::iterator> _pos;

public:
    LRUCache(int capacity) {
        _cap = capacity;
    }

    int get(int key) {
        if (!_pos.count(key)) {
            return -1;
        }

        int value = _pos[key]->second;

        _data.erase(_pos[key]);
        _data.push_back({key, value});
        _pos[key] = --_data.end();

        return value;
    }

    void put(int key, int value) {
        if (_pos.count(key) > 0) {
            _data.erase(_pos[key]);
        }

        if (_data.size() == _cap) {
            _pos.erase(_data.front().first);
            _data.pop_front();
        }

        _data.push_back({key, value});
        _pos[key] = --_data.end();
    }
};