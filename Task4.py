import random

def write_polynomial(k):
    File_object = open(r"Task4_text.txt","w")

    for i in range (k, -1, -1):
        random_num = random.randint(0,100)
        if (i > 0):
            File_object.write(f"{random_num}x^{i} + ")
        else:
            File_object.write(f"{random_num} = 0")
    File_object.close()

k = 4
write_polynomial(k)