def konvert(mi=0):
    def hari(h=0):
        def jam(j=0):
            def menit(m=0):
                return (mi + h * 24 * 60 + j * 60 + m)
            return menit
        return jam
    return hari

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

output = []

for item in data:
    items = item.split()
    minggu = int(items[0])
    hari = int(items[2])
    jam = int(items[4])
    menit = int(items[6])
    
    total = konvert(menit)(jam)(hari)(minggu)
    output.append(total)

print("Output =", output)
