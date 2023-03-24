import os # ใช้ในการค้นหาไฟล์ .lua
import fnmatch # ใช้ในการค้นหาไฟล์ .lua
import re # ใช้ในการค้นหาข้อความ

# กำหนด path ของโฟลเดอร์ที่ต้องการค้นหา
folder_path = "" # ตัวอย่าง "C:\Users\user\Desktop\lua"
output_file = open("result.txt", "w") # สร้างไฟล์ result.txt เพื่อเก็บผลลัพธ์

# สร้าง list เก็บชื่อไฟล์ .lua ทั้งหมด
lua_files = [] # สร้าง list เก็บชื่อไฟล์ .lua ทั้งหมด

# วน loop เพื่อค้นหาไฟล์ .lua ในโฟลเดอร์
for root, dir, files in os.walk(folder_path): # ค้นหาไฟล์ .lua ทั้งหมดในโฟลเดอร์
    for file in files: # วน loop เพื่อค้นหาไฟล์ .lua
        if fnmatch.fnmatch(file, "*.lua"): # ค้นหาไฟล์ .lua
            lua_files.append(os.path.join(root, file)) # เพิ่มชื่อไฟล์ .lua ลงใน list

# วน loop เพื่อค้นหาข้อความในไฟล์ .lua
for file in lua_files: # วน loop เพื่อค้นหาข้อความในไฟล์ .lua
    with open(file, 'r', encoding='utf-8') as f: # อ่านไฟล์ .lua
        lines = f.readlines() # อ่านข้อความในไฟล์ .lua
        for line in lines: # วน loop เพื่อค้นหาข้อความในไฟล์ .lua
            if re.search("TriggerServerEvent", line): # ค้นหาข้อความ "TriggerServerEvent" ในไฟล์ .lua
                #output_file.write("{}: {}\n".format(file, line.strip())) #แสดงทั้งชื่อไฟล์และ TriggerServerEvent
                output_file.write("{}\n".format(line.strip())) #แสดงแค่ TriggerServerEvent
                print("{}\n".format(line.strip())) #แสดงแค่ TriggerServerEvent ใน cmd , console
