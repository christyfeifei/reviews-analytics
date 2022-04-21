data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))  # 每讀一筆留言，印出數字

print(len(data))  # 印出總共幾筆留言

print(data[0])  # 印出第一筆留言
