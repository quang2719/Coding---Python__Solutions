class TrieNode:
    def __init__(self):
        # `children` là một dictionary (hoặc mảng) để lưu trữ các node con,
        # key là ký tự và value là node TrieNode tương ứng.
        self.children = {}
        # `is_end_of_word` là một boolean để đánh dấu node này có phải là kết thúc của một từ hay không.
        self.is_end_of_word = False

class Trie(object):

    def __init__(self):
        """
        Khởi tạo Trie với một node gốc (root).
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Chèn một từ vào Trie.
        Duyệt qua từng ký tự của từ, nếu ký tự chưa có trong children của node hiện tại,
        tạo một node con mới. Di chuyển xuống node con tương ứng với ký tự.
        Khi duyệt hết từ, đánh dấu node cuối cùng là `is_end_of_word = True`.
        """
        node = self.root # Bắt đầu từ node gốc
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() # Tạo node con nếu ký tự chưa có
            node = node.children[char] # Di chuyển xuống node con
        node.is_end_of_word = True # Đánh dấu là kết thúc từ

    def search(self, word):
        """
        Tìm kiếm một từ trong Trie.
        Duyệt qua từng ký tự của từ, nếu ký tự không có trong children của node hiện tại,
        từ không tồn tại trong Trie, trả về False.
        Nếu duyệt hết từ, kiểm tra node cuối cùng có được đánh dấu `is_end_of_word` hay không.
        Nếu có, từ tồn tại, trả về True, ngược lại trả về False (ví dụ: tìm "ap" trong khi chỉ có "apple").
        """
        node = self.root # Bắt đầu từ node gốc
        for char in word:
            if char not in node.children:
                return False # Ký tự không tồn tại, từ không có trong Trie
            node = node.children[char] # Di chuyển xuống node con
        return node.is_end_of_word # Trả về True nếu node cuối cùng là kết thúc từ

    def startsWith(self, prefix):
        """
        Kiểm tra xem có từ nào trong Trie bắt đầu bằng tiền tố cho trước hay không.
        Duyệt qua từng ký tự của tiền tố, nếu ký tự không có trong children của node hiện tại,
        không có từ nào bắt đầu bằng tiền tố này, trả về False.
        Nếu duyệt hết tiền tố, trả về True (chỉ cần tiền tố tồn tại, không cần là một từ hoàn chỉnh).
        """
        node = self.root # Bắt đầu từ node gốc
        for char in prefix:
            if char not in node.children:
                return False # Ký tự không tồn tại, không có tiền tố này
            node = node.children[char] # Di chuyển xuống node con
        return True # Tiền tố tồn tại trong Trie


# Your Trie object will be instantiated
# and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)