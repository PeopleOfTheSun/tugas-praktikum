def konvert(mi=0):
    def hari(h=0):
        def jam(j=0):
            def menit(m=0):
                return (mi, h, j, m)
            return menit
        return jam
    return hari

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

int_type = []
str_type = []

for item in data:
    items = item.split()
    minggu = int(items[0])
    hari = int(items[2])
    jam = int(items[4])
    menit = int(items[6])
    
    total = konvert(minggu)(hari)(jam)(menit)
    int_type.append(f"{minggu} {hari} {jam} {menit}")  
          
    if (item in data):
        items = item.split()
        minggu = str(items[1])
        hari = str(items[3])
        jam = str(items[5])
        menit = str(items[7])
        # total = konvert(minggu)(hari)(jam)(menit)
        # str_type.append(total)
        str_type.append(f"{minggu} {hari} {jam} {menit}")
        
print("Data Int:")
print(int_type)
print("\nData String:")
print(str_type)

