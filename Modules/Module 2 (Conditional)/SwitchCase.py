x = input("Masukkan kode plat Anda: ").upper()  # Convert input to uppercase

# Dictionary to map codes to locations
plat_dict = {
    'B': "Bekasi",
    'A': "Banten",
    'D': "Banten",
    'E': "Cirebon"
}

# Get the corresponding location or a default message
print(plat_dict.get(x, "Kode tidak diketahui"))
# Dictionary.get(key, default_value)
