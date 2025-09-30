# def intrev(nums):
#     nums = str(nums)
#     result = ""
#     for ch in nums:
#         result = ch + result
#     return int(result)
# print(intrev(123456))


def intrev(nums):
    return int(str(nums)[::-1])
print(intrev(12343))