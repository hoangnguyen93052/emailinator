import hashlib
from typing import Any, List, Optional, Tuple

class Node:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, key: Any, value: Any) -> None:
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert_rec(self.root, key, value)

    def _insert_rec(self, node: Node, key: Any, value: Any) -> None:
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._insert_rec(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._insert_rec(node.right, key, value)

    def search(self, key: Any) -> Optional[Any]:
        return self._search_rec(self.root, key)

    def _search_rec(self, node: Optional[Node], key: Any) -> Optional[Any]:
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)

    def delete(self, key: Any) -> None:
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node: Optional[Node], key: Any) -> Optional[Node]:
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_rec(node.left, key)
        elif key > node.key:
            node.right = self._delete_rec(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children, get the inorder successor
            temp_value = self._min_value_node(node.right)
            node.key, node.value = temp_value.key, temp_value.value
            node.right = self._delete_rec(node.right, temp_value.key)
        return node

    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

class DatabaseIndex:
    def __init__(self) -> None:
        self.index: BinarySearchTree = BinarySearchTree()

    def insert(self, key: Any, value: Any) -> None:
        hashed_key = self._hash_key(key)
        self.index.insert(hashed_key, value)

    def search(self, key: Any) -> Optional[Any]:
        hashed_key = self._hash_key(key)
        return self.index.search(hashed_key)

    def delete(self, key: Any) -> None:
        hashed_key = self._hash_key(key)
        self.index.delete(hashed_key)

    def _hash_key(self, key: Any) -> str:
        return hashlib.sha256(str(key).encode()).hexdigest()

    def display(self) -> None:
        self._in_order_display(self.index.root)

    def _in_order_display(self, node: Optional[Node]) -> None:
        if node is not None:
            self._in_order_display(node.left)
            print(f'Key: {node.key}, Value: {node.value}')
            self._in_order_display(node.right)

def main() -> None:
    db_index = DatabaseIndex()

    # Sample data insertion
    db_index.insert('user1', {'name': 'Alice', 'age': 30})
    db_index.insert('user2', {'name': 'Bob', 'age': 25})
    db_index.insert('user3', {'name': 'Charlie', 'age': 35})

    print("Database Index:")
    db_index.display()

    # Searching for records
    search_key = 'user2'
    result = db_index.search(search_key)
    print(f'\nSearch Result for {search_key}:', result)

    # Deleting a record
    db_index.delete('user1')
    print("\nAfter deleting user1:")
    db_index.display()

    # Search for deleted record
    deleted_result = db_index.search('user1')
    print(f'\nSearch Result for deleted user1:', deleted_result)

if __name__ == '__main__':
    main()