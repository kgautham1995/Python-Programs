import speedtest
# print("Testing your internet speed please wait..................")
test=speedtest.Speedtest()
down=test.download()
up=test.upload()
print("Download speed is",down)
print("Upload Speed is", up)
print("Thanks")