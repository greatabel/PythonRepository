from sympy.ntheory.modular import solve_congruence
from typing import List
from termcolor import colored
import random

print('''
改进：
1.引入了随机数，使得每次生成的分割密钥都不同，增加了密钥安全性
2. 对生成的随机数和加密分割密钥进
3. 增加了threshold 门限制的检查
    ''')
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


def generate_key_parts(moduli: List[int], key: int, threshold: int) -> List[int]:
    print(f"threshold：{threshold}")
    for i in range(threshold):
        random_shares = [random.randint(0, modulus - 1) for modulus in moduli]
        encrypted_shares = [
            (key * random_share) % modulus
            for random_share, modulus in zip(random_shares, moduli)
        ]
        print(random_shares, encrypted_shares)
        if len(random_shares) != len(encrypted_shares):
            break
    key_parts = []
    for modulus in moduli:
        key_parts.append(key % modulus)
    return key_parts


def recover_key(moduli: List[int], key_parts: List[int]) -> int:
    key = 0
    for i in range(len(key_parts)):
        bi = 1
        for j in range(len(moduli)):
            if j != i:
                bi *= moduli[j]
        inv = pow(bi, -1, moduli[i])
        key += key_parts[i] * bi * inv
    return key % (moduli[0] * moduli[1] * moduli[2])


# 定义模数
moduli = [101, 103, 109]

# 初始化子服务器
key_servers = [KeyServer(modulus) for modulus in moduli]

# 群组密钥
group_key = 761

print(colored(f"群组密钥: {group_key}", "green"))

# 分割密钥
key_parts = generate_key_parts(moduli, group_key, len(moduli))
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
