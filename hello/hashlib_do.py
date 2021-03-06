# hashlib 摘要算法

# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
# 常见的摘要算法，如MD5，SHA1,更安全的算法SHA256和SHA512, 越安全的算法不仅越慢，而且摘要长度更长
import hashlib

md5 = hashlib.md5()
md5.update('sea'.encode('utf-8'))
md5.hexdigest() # 804f743824c0451b2f60d81b63b6a900   ,md5生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示


# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”
def cal_md5(password):
  return get_md5(password + 'the-Salt')

# 要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。


# hmac, Keyed-Hashing for Message Authentication 
# 利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。
# 准备待计算的原始消息message，随机key，哈希算法. 如采用MD5，使用hmac的代码如下：
import hmac
messeage = b'sea'
key = b'secret'
h = hmac.new(key, messeage, digestmod='md5')
h.hexdigest() # d9e8b7be1a490e559577a8df3d45785e





