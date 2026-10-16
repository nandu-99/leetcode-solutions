class LRUCache {
    class Node{
        int key, value;
        Node prev, next;
        Node(int key, int value){
            this.key = key;
            this.value = value;
        }
    }

    private int capacity;
    private Map<Integer, Node>map;
    private Node head, tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        map = new HashMap<>();
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
    }

    private void remove(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void insertAtEnd(Node node){
        node.prev = tail.prev;
        node.next = tail;
        tail.prev.next = node;
        tail.prev = node;
    }
    
    public int get(int key) {
        if(!map.containsKey(key)){
            return -1;
        }
        Node node = map.get(key);
        remove(node);
        insertAtEnd(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            Node node = map.get(key);
            remove(node);
            map.remove(key);
        }
        if(map.size()==capacity){
            Node lru = head.next;
            remove(lru);
            map.remove(lru.key);
        }
        Node node = new Node(key, value);
        insertAtEnd(node);
        map.put(key, node);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */