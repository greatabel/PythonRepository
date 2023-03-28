from sympy.ntheory.modular import solve_congruence
from typing import List

class KeyServer:
    def __init__(self, modulus: int):
        self.modulus = modulus
        self.member_key_parts = {}

    def register_member(self, member_id: str, key_part: int):
        self.member_key_parts[member_id] = key_part

    def get_key_part(self, member_id: str) -> int:
        return self.member_key_parts.get(member_id)

def generate_key_parts(moduli: List[int], key: int) -> List[int]:
    return [key % modulus for modulus in moduli]

def recover_key(moduli: List[int], key_parts: List[int]) -> int:
    key = solve_congruence(*zip(key_parts, moduli))
    return key

# 定义模数
moduli = [3, 5, 7]

# 初始化子服务器
key_servers = [KeyServer(modulus) for modulus in moduli]

# 群组密钥
group_key = 97

# 分割密钥
key_parts = generate_key_parts(moduli, group_key)

# 为每个成员分配密钥
member_id = "member_001"
for server, key_part in zip(key_servers, key_parts):
    server.register_member(member_id, key_part)

# 成员加入群组时从子服务器获取密钥
retrieved_key_parts = [server.get_key_part(member_id) for server in key_servers]

# 使用中国剩余定理恢复群组密钥
recovered_key = recover_key(moduli, retrieved_key_parts)
print("恢复的群组密钥:", recovered_key)

