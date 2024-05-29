"""
số hoàng thiện ( hay còn được gọi là sô hoàn hảo hoặc sô hoàn thành) là một số nguyên dương mà tổng sô các ước nguyên dương chính thức của nó
(số nguyên dương của nó bị chia hết cho ngoại phạm vi trừ của nó. Tìm tât cả những số hoàn thien từ phạm vi từ 1-1000
"""
n=int(input("mời bạn nhập vào số hoàn thien"))
s=0
for i in range(1,n,1):
     if n%i ==0:
        s=s+i
if s==n:
     print(f"Số{n}là số hoàn thiện ")
else:
    print(f"số{n}không phải là số hoàn thiện")
