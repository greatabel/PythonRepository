from random import randint
from sympy.ntheory.modular import solve_congruence
from typing import List, Tuple


def generate_coefficients(degree: int, key: int, modulus: int) -> List[int]:
    coefficients = [randint(0, modulus - 1) for _ in range(degree)]
    coefficients.append(key)
    return coefficients

def lagrange_interpolation(x_values: List[int], y_values: List[int], modulus: int) -> int:
    result = 0
    for i in range(len(x_values)):
        product = y_values[i]
        for j in range(len(x_values)):
            if i != j:
                product *= (0 - x_values[j]) * mod_inverse(x_values[i] - x_values[j], modulus)
                product %= modulus
        result += product
        result %= modulus
    return result

class KeyServer:
    def __init__(self, modulus: int):
        self.modulus = modulus
        self.member_key_parts = {}

    def register_member(self, member_id: str, key_part: int):
        self.member_key_parts[member_id] = key_part

    def get_key_part(self, member_id: str) -> int:
        return self.member_key_parts.get(member_id)

    def register_member(self, member_id: str, key_part: int, x_value: int):
        self.member_key_parts[member_id] = (key_part, x_value)

    def get_key_part(self, member_id: str) -> Tuple[int, int]:
        return self.member_key_parts.get(member_id)

def generate_key_parts(moduli: List[int], key: int) -> List[int]:
    return [key % modulus for modulus in moduli]

def recover_key(moduli: List[int], key_parts: List[int]) -> int:
    key = solve_congruence(*zip(key_parts, moduli))
    return key


def mod_inverse(a: int, m: int) -> int:
    """
    计算 a 模 m 的逆元
    """
    r0, r1 = a, m
    x0, x1 = 1, 0
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        x0, x1 = x1, x0 - q * x1
    if r0 == 1:
        return x0 % m
    else:
        raise ValueError("逆元不存在")


# 定义模数
moduli = [3, 5, 7]

# 初始化子服务器
key_servers = [KeyServer(modulus) for modulus in moduli]

# 群组密钥
group_key = 97

# 分割密钥
key_parts = generate_key_parts(moduli, group_key)

# 为每个成员分配密钥
# 为每个成员分配密钥
# 为每个成员分配密钥
t = 2  # 门限值
member_ids = ["member_001", "member_002", "member_003"]
x_values = [i + 1 for i in range(len(member_ids))]
for server, modulus in zip(key_servers, moduli):
    coefficients = generate_coefficients(t - 1, group_key, modulus)
    for member_id, x_value in zip(member_ids, x_values):
        key_part = sum(coefficients[i] * x_value ** i for i in range(t)) % modulus
        server.register_member(member_id, key_part, x_value)  # Pass three arguments here

# 成员加入群组时从子服务器获取密钥
retrieved_key_parts = [server.get_key_part(member_id) for server in key_servers]
retrieved_key_parts = list(zip(*retrieved_key_parts))  # Transpose the list

# 使用拉格朗日插值计算多项式



def lagrange_interpolation(x_values: List[int], y_values: List[int], modulus: int) -> int:
    result = 0
    for i in range(len(x_values)):
        product = y_values[i]
        for j in range(len(x_values)):
            if i != j:
                product *= (0 - x_values[j]) * mod_inverse(x_values[i] - x_values[j], modulus)
                product %= modulus
        result += product
        result %= modulus
    return result

# ...（与之前相同）

# 使用拉格朗日插值计算多项式的常数项
constant_terms = [lagrange_interpolation(x_values[:t], key_parts[:t], modulus) for key_parts, modulus in zip(retrieved_key_parts, moduli)]

# 使用中国剩余定理恢复群组密钥
recovered_key = recover_key(moduli, constant_terms)
print("恢复的群组密钥:", recovered_key)


