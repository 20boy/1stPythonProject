store = {
    0.5: "green",
    1.0: "greenish Yellow",
    1.5: "Yellowish Green",
    2.0: "Fucking Black",
}
def maClean(size,color):
    for x,y in store.items():
        if size == y:
         print(color + " is available")
        else:
         print("Not Available Baby")
maClean("gree", "blue")


