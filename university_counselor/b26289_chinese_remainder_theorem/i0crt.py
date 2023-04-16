from sympy.ntheory.modular import solve_congruence
from typing import List
from termcolor import colored

import os

# os.system('color')


class KeyServer:
    def __init__(self, modulus: int):
        self.modulus = modulus
        self.member_key_parts = {}

    def register_member(self, member_id: str, key_part: int):
        self.member_key_parts[member_id] = key_part
        print(
            colored(
                f"子服务器模数 {self.modulus}: 注册会员 {member_id}, 密钥部分: {key_part}", "cyan"
            )
        )

    def get_key_part(self, member_id: str) -> int:
        return self.member_key_parts.get(member_id)


def generate_key_parts(moduli: List[int], key: int) -> List[int]:
    return [key % modulus for modulus in moduli]


def recover_key(moduli: List[int], key_parts: List[int]) -> int:
    key = solve_congruence(*zip(key_parts, moduli))
    return key


# 定义模数
moduli = [101, 103, 109]

# 初始化子服务器
key_servers = [KeyServer(modulus) for modulus in moduli]

# 群组密钥
group_key = 761

print(colored(f"群组密钥: {group_key}", "green"))

# 分割密钥
key_parts = generate_key_parts(moduli, group_key)
print(colored(f"密钥分割: {key_parts}", "yellow"))

# 为每个成员分配密钥
member_id = "member_001"
for server, key_part in zip(key_servers, key_parts):
    server.register_member(member_id, key_part)

# 成员加入群组时从子服务器获取密钥
retrieved_key_parts = [server.get_key_part(member_id) for server in key_servers]
print(colored(f"从子服务器检索的密钥部分: {retrieved_key_parts}", "blue"))

# 使用中国剩余定理恢复群组密钥
recovered_key = recover_key(moduli, retrieved_key_parts)
print(colored(f"恢复的群组密钥: {recovered_key}", "magenta"))
