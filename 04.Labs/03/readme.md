# COMP9021 Lab03

> [!NOTE]
>
> 相关内容仅供大家学习交流之用，均属个人整理

## 主要涉及知识点

- 字符串-加法运算

视频讲解: https://sfugl.xetlk.com/s/2KkyGE（仅限班课）

- 字符串-乘法运算

视频讲解: https://sfugl.xetlk.com/s/4xrYfx（仅限班课）

- 字符串-join 函数

视频讲解: https://sfugl.xetlk.com/s/1iZ0EE（仅限班课）

- 列表-列表生成式

视频讲解: https://sfugl.xetlk.com/s/48EvYS（仅限班课）

## 参考代码

### Exercise 1

```python
def f1(m, n):
     # return ''
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    return " * ".join('|'.join('_' * n) for _ in range(m))
```

### Exercise 2

```python
def f2(n):
    # return ''
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    print("".join("⬛" if int(e) % 2 == 1 else "⬜" for e in str(n)))

```

### Exercise 3

```python
def f3(n):
    # pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
    for i in range(max(int(max(str(n))) + 1, 2), 11):
        print(f"{n} is {int(str(n), i)} in base {i}")
```

### Exercise 4

```python
def f4(n, base):
    # return {}
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    result = {0: (0, )}
    for i in range(1, n + 1):
        # 进制转换
        base_result = []
        m = i
        # 判断大于0
        while m > 0:
            # 获取余数和除数
            m, b = divmod(m, base)
            base_result.append(b)
        # 处理结果集
        result[i] = tuple(base_result[::-1])
    # 将结果返回
    return result

```

### Exercise 5

```python
def f5(integral_part, fractional_part):
    # pass
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
    # 构造浮点数
    fraction = f"{integral_part}.{fractional_part}"
    #  需要多少个digits
    number_of_digits = len(str(fractional_part)) * 2
    # 完整的整数是多少
    decemal = f"{float(fraction):.{number_of_digits}f}"
    # 尾部需要几个 0
    nubmer_of_trailing_zero = len(decemal) - len(fraction)
    print(f"With {number_of_digits} digits after the decimal point, ", end="")
    if fraction + nubmer_of_trailing_zero * '0' == decemal:
        # 判断个数
        if nubmer_of_trailing_zero ==1:
            print(f"{fraction} prints out with {nubmer_of_trailing_zero} trailing zero, ", end="")
        else:
            print(f"{fraction} prints out with {nubmer_of_trailing_zero} trailing zeroes, ", end="")
        print(f"namely, as {decemal}")
    else:
        print(f"{fraction} prints out as {decemal}")
```

### Exercise 6

```python
def f6(L, fields):
    # return []
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    return sorted(L, key = lambda e: tuple(e[i - 1] for i in fields))
```
