# 🤖 line_robot – Web-controlled Robot with Raspberry Pi + GPIO + Camera

โปรเจกต์นี้เป็นระบบควบคุมหุ่นยนต์ 2 ล้อผ่านเว็บเบราว์เซอร์ ด้วย Flask + กล้อง USB และการควบคุมมอเตอร์ผ่าน `gpiozero` เหมาะสำหรับนักศึกษาและผู้เริ่มต้นใช้งาน Raspberry Pi

---

## 🚀 การติดตั้งเบื้องต้น

เปิด Terminal แล้วทำตามขั้นตอน:

```bash
1. $ sudo apt-get update
2. $ sudo apt-get upgrade -y
3. $ mkdir line_robot
4. $ cd ~/line_robot
5. $ sudo apt install python3-gpiozero python3-libgpiod
6. $ python3 -m venv venv --system-site-packages
7. $ source venv/bin/activate
```

---

## 📁 สร้างโครงสร้างโปรเจกต์

สร้างไฟล์ตามนี้:

```
line_robot/
├── main.py
├── templates/
│   └── index.html
├── venv/
└── requirements.txt
```

---

## 📦 ติดตั้งไลบรารีที่ใช้

```bash
9. $ pip install -r requirements.txt
```

---

## 🛠 สร้างไฟล์ run.sh สำหรับเรียกโปรแกรมแบบง่าย

```bash
10. $ nano run.sh
```

วางโค้ดต่อไปนี้ลงในไฟล์ `run.sh`:

```bash
#!/bin/bash
cd /home/pi/line_robot
source venv/bin/activate
sudo venv/bin/python main.py  # ← เปลี่ยนชื่อไฟล์ตรงนี้ถาชื่อไม่ใช่ main.py
```

บันทึกไฟล์ แล้วสั่งให้สามารถรันได้:

```bash
11. $ chmod +x run.sh
12. $ ./run.sh
```

---

## 🌐 การใช้งาน

1. เปิดโปรแกรมด้วยคำสั่ง `./run.sh`
2. บนเว็บเบราว์เซอร์ ไปที่:

```
http://<IP_ADDRESS ของ Raspberry Pi>:5000
```

เช่น `http://192.168.1.100:5000`

---

## 🔀 เส้นทางการใช้งาน (Router Path)

| URL Path   | Method | คำอธิบาย                                  |
|------------|--------|---------------------------------------------|
| `/`        | GET    | หน้าเว็บแสดงกล้อง + ปุ่มควบคุมหุ่นยนต์    |
| `/video`   | GET    | สตรีมกล้อง USB แบบ MJPEG                   |
| `/move`    | POST   | รับคำสั่งจากปุ่ม (เดินหน้า/ถอย/เลี้ยว/หยุด) |

---

## 📚 หมายเหตุเพิ่มเติม

- ใช้กล้อง USB (เช่น Logitech) ผ่าน `cv2.VideoCapture(0)`
- รองรับ Raspberry Pi OS รุ่นใหม่ (Bookworm) ด้วย `gpiozero`
- อย่าลืมต่อ GND ของไดรเวอร์มอเตอร์ร่วมกับ RPi
- ต้องรันด้วย `sudo` หากใช้ PWM/ควบคุม GPIO จริง

---
