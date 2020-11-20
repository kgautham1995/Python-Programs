import pafy
u="https://www.youtube.com/watch?v=3LJjc1Yy4FE&t=35s"
v=pafy.new(u)
s=v.streams
for i in s:
    print(i)
best=v.getbest()
print(best.resolution, best.extension)
best.download()
print("Video Downloaded Successfully")