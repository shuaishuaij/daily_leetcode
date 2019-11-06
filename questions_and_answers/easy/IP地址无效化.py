'''
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。

所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/defanging-an-ip-address
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"
'''


class Solution:
        def defangIPaddr(self, address: str) -> str:
                def reform(str):
                        if str == '.':
                                return '[.]'
                        else:
                                return str
                add_lst = [char for char in address]
                out = map(reform, add_lst)

                return ''.join(out)

if __name__ == '__main__':
    address = "255.100.50.0"
    a = Solution()
    print(a.defangIPaddr(address))