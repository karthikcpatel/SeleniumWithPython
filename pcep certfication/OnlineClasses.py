kpset = {"kartik","swapan","change","hi"}
kplist = ["in","the","list"]
kptuple = ("got","it")

kpset.update(kplist)
print(kpset)

kpset.update(kptuple)
print(kpset)

# delete the values
kpset.remove("hi")
print(kpset)

kpset.discard("got")
print(kpset)

# list - ordered and it can be changed
# tuple - ordered , but it cannot be changed
# set - unordered, and it can be changed