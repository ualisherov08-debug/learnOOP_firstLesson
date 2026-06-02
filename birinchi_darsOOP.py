# class salom:
#     def show(self):
#         print("salom")
# s1=salom()
# s1.show()

# .............................................................

# class animal:
#     def __init__(self,nom,turi):
#         self.nom=nom
#         self.tur=turi
#     def info(self):
#         print(f"""
# hayvon nomi : {self.nom}
# hayvon turi : {self.tur}
# """)
# h1=animal("sher","yovvoyi")
# h2=animal("mushuk","uy hayvoni")
# h1.info()
# h2.info()
    
# ........................................................................

# class telefon:
#     def __init__(self,brand,narx,yumkost,tezlik,kamera,nechta_sim,rang):
#         self.brand=brand
#         self.cost=narx
#         self.battery=yumkost
#         self.speed=tezlik
#         self.camera=kamera
#         self.simcard=nechta_sim
#         self.colour=rang
        
#     def really_cost(self,real_cost):
#         if real_cost < self.cost:
#             self.cost=real_cost
            
#     def collour(self,need_colour):
#         if self.colour == need_colour:
#             self.colour = need_colour
    
#     def kamera(self,kamera_s):
#         if 1 <= kamera_s <=3:
#             self.camera +=1
        
#     def batarya (self,quvvat):
#         if 3000 <= quvvat <= 5000:
#             self.battery +=1000
            
#     def info(self):
#         print(f"""
# Telefon brandi : {self.brand}
# Telefon narxi  : {self.cost}
# Telefon quvvati  : {self.battery} 
# Telefon tezligi  : {self.speed}   
# Telefon kamerasi  : {self.camera}
# Telefon simkartasi   : {self.simcard}
# Telefon rangi  : {self.colour}
#         """)
        
# T1=telefon("iphone",1200,3000,"5 secund",3,2,"black")
# T2=telefon("redmi",200,6000,"12 secund",3,2,"white")
# T3=telefon("samsung",500,5000,"8 secund",4,2,"dark")

# T1.info()
# T2.info()
# T3.info()

# T1.really_cost(int(input("Asl narxini kiriting: ")))
# T1.collour(input("kerak rangni kiriting: "))
# T1.kamera(int(input("kamera sonini kiriting: ")))
# T1.batarya(int(input("baterya necha amper ekanligini kiriting: ")))

# T2.really_cost(int(input("Asl narxini kiriting: ")))
# T2.collour(input("kerak rangni kiriting: "))
# T2.kamera(int(input("kamera sonini kiriting: ")))
# T2.batarya(int(input("baterya necha amper ekanligini kiriting: ")))

# T3.really_cost(int(input("Asl narxini kiriting: ")))
# T3.collour(input("kerak rangni kiriting: "))
# T3.kamera(int(input("kamera sonini kiriting: ")))
# T3.batarya(int(input("baterya necha amper ekanligini kiriting: ")))

# T1.info()
# T2.info()
# T3.info()

# ............................................................................................

# class car:
#     def __init__(self,name,year,speed):
#         self.nom=name
#         self.yil=year
#         self.tezlik=speed
    
#     def start(self,tezlik_start):
#         if 5 <= tezlik_start <= 20:
#             print("mashina yurdi ")
            
#     def stop(self,tezlik_stop):
#         if 10 <= tezlik_stop <= 20:
#             print("mashina tohtadi ")
    
#     def turn_right(self,ongga_burilish):
#         if 40 <= ongga_burilish <= 90:
#             print("mashina onga burildi ")
    
#     def turn_back(self,orqaga):
#         if 10 <= orqaga <=30:
#             print("mashina orqaga  yurdi ")
            
#     def info(self):
#         print(f"""
# mashina nomi : {self.nom}  
# mashina yili : {self.yil}
# mashina tezligi: {self.tezlik}       
#           """)
        
# M1=car("BMW",2020,300)
# M2=car("Mers",1990,200)
# M3=car("Audi",2010,180)
# M4=car("Ferrari",2018,280)
# M5=car("Toyota",2025,150)

# M1.info()
# M2.info()
# M3.info()
# M4.info()
# M5.info()



# print("birinchi mashina\n")
# M1.start(int(input("boshlangich uchun tezlikni kiriting: ")))
# M1.stop(int(input("toxtatish uchun  tezlikni kiriting: ")))
# M1.turn_right(int(input("onga burilish uchun tezlikni kiriting: ")))
# M1.turn_back(int(input("orqaga harakat uchun tezlikni kiriting: ")))


# print("ikkinchi mashina\n")
# M2.start(int(input("boshlangich uchun tezlikni kiriting: ")))
# M2.stop(int(input("toxtatish uchun  tezlikni kiriting: ")))
# M2.turn_right(int(input("onga burilish uchun tezlikni kiriting: ")))
# M2.turn_back(int(input("orqaga harakat uchun tezlikni kiriting: ")))


# print("uchinchi mashina\n")
# M3.start(int(input("boshlangich uchun tezlikni kiriting: ")))
# M3.stop(int(input("toxtatish uchun  tezlikni kiriting: ")))
# M3.turn_right(int(input("onga burilish uchun tezlikni kiriting: ")))
# M3.turn_back(int(input("orqaga harakat uchun tezlikni kiriting: ")))


# print("tortinchi mashina\n")
# M4.start(int(input("boshlangich uchun tezlikni kiriting: ")))
# M4.stop(int(input("toxtatish uchun  tezlikni kiriting: ")))
# M4.turn_right(int(input("onga burilish uchun tezlikni kiriting: ")))
# M4.turn_back(int(input("orqaga harakat uchun tezlikni kiriting: ")))


# print("beshinchi mashina\n")
# M5.start(int(input("boshlangich uchun tezlikni kiriting: ")))
# M5.stop(int(input("toxtatish uchun  tezlikni kiriting: ")))
# M5.turn_right(int(input("onga burilish uchun tezlikni kiriting: ")))
# M5.turn_back(int(input("orqaga harakat uchun tezlikni kiriting: ")))

# M1.info()
# M2.info()
# M3.info()
# M4.info()
# M5.info()


# .......................................................................................................................................


# class Talaba:
#     def __init__(self,ism,familiya,baho):
#         self.first_name=ism
#         self.last_name = familiya
#         self.baho=baho
# T1 = Talaba("aziz","azimov",90)
# T2 = Talaba("azim","azizov",95)
# T3 = Talaba("adiz","adimov",80)

# if T1.baho > T2.baho  and T1.baho > T3.baho:
#     print(T1.baho)
# elif T2.baho > T1.baho and T2.baho > T3.baho:
#     print(T2.baho)
# else:
#     print(T3.baho)


# .............................................................................................

# class human:
#     def __init__(self,first_name,last_name,age):
#         self.ism=first_name
#         self.familya=last_name
#         self.yosh=age
        
#     def full_name(self):
#         print(f"{self.ism} {self.familya}")
# H1=human("ulug'bek","Alisherov",23)
# H1.full_name()

# ..............................................................................................
# class Bino:
#     def __init__(self, baland, rang):
#         self.balandlik = baland
#         self.rang = rang
    
# b1 = Bino(50,"qora")
# b2 = Bino(40,"qizil")
# b3 = Bino(90,"oq")
# b4 = Bino(10,"sariq")
# b5 = Bino(70,"yashil")


# lst = [b1, b2, b3, b4, b5]

# for i in lst:
#     if i.balandlik > 50:
#         print(i.rang)

# ..............................................................................................

# class human:
#     def __init__(self,name,age,job,height,weight,single):
#         self.name=name
#         self.yosh=age
#         self.ish=job
#         self.boy=height
#         self.vazn=weight
#         self.turmush=single
#     def get_name(self):
#         return self.name
    
#     def get_yosh(self):
#         return self.yosh
    
#     def get_ish(self):
#         return self.ish
    
#     def get_boy(self):
#         return self.boy
    
#     def get_vazn(self):
#         return self.vazn
    
#     def get_turmush(self):
#         return self.turmush

# H1=human("Ulugbek Alisherov",23,"Cybersecurity engineer",183,73,"single")
# print(H1.get_name())
# print(H1.get_yosh())
# print(H1.get_ish())
# print(H1.get_boy())
# print(H1.get_vazn())
# print(H1.get_turmush())

# .................................................................................

# class market:
#     def __init__(self,name:str,price:float = 0.0):
#         self.name = name
#         self.price = price
#         self.products = []
       
#     def addproduct(self,product : dict):
#         if isinstance(product,dict):
#             self.products.append(product)
#             print(f"mahsulot qoshildi : {product.get('name','nomsiz')}")
#         else:
#             print("xatolik ")
            
#     def removeproduct(self,product_name:str):
#         for product in self.products:
#             if product.get("name") == product_name:
#                 self.products.remove(product)
#                 print(f"maxsulot ochirildi: {product_name}")
#                 return
#         print(f"maxsulot topilmadi")
    
    
#     def get_all_price(self) ->float:
#         total_price = 0.0
#         for product in self.products:
#             total_price += product.get('price',0)
#         return total_price
    
# dokon=market(name="Korzinka",price=100000.0)

# dokon.addproduct({"name":"uzum","price":35000.0})
# dokon.addproduct({"name":"tarvuz","price":20000.0})
# dokon.addproduct({"name":"qovun","price":35000.0})

# print(f"\njami mahsulotlar narxi: {dokon.get_all_price()} so'm")

# dokon.removeproduct("qovun")

# print(f"jami : {dokon.get_all_price()} so'm")


# ..................................................................................................

# <<<<<<<<<<<<<<<<<<<<<<<< UYGA VAZIFA  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ...................................................................................................

# 1 masala

# class kitob:
#     def __init__(self,nomi,mualiflar,narxi,nashriyot):
#         self.name=nomi
#         self.writer=mualiflar
#         self.price=narxi
#         self.publish=nashriyot
        
           
# B1=kitob("Otkan kunlar","Abdulla Qodiriy",35000,2000)
# B2=kitob("Sariq devni minib","Xudoyberdi Tohtaboyev",20000,2010)
# B3=kitob("Bolakay,tullki,tulpor,korsichqon","Charli Makkizi",25000,2026)
# B4=kitob("Oxi evron","Fotix Duman",30000,2022)
# B5=kitob("Fotimani bolalari","Josom Al-umron",50000,2018)

# lst=[B1,B2,B3,B4,B5]
# harflar = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# for i in lst:
#         if i.name.startswith(harflar):
#             print(f"""
# kitob haqida malumot\n
# nomi: {i.name}\nmualiflari: {i.writer}\nnarxi: {i.price}\nnashr qilingan yil: {i.publish}        
# """)

# .............................................................................................................

# 2 masala

# class kompyuter:
#     def __init__(self,name,Ram,narx,protsessor):
#         self.name=name
#         self.ram=Ram
#         self.price=narx
#         self.xotira=protsessor
    
#     def info(self):
#         print(f"""
# kompyuter brandi : {self.name}
# kompyuter rami   : {self.ram}
# kompyuter narxi  : {self.price}
# kompyuter protsessori : {self.xotira}         
#         """)

        
# laptop1=kompyuter("Macbook",32,1200,1024)
# laptop2=kompyuter("Lenovo",8,600,256)
# laptop3=kompyuter("Asus",2,200,128)
# laptop4=kompyuter("hp",16,800,512)


# laptop1.info()
# laptop2.info()
# laptop3.info()
# laptop4.info()

# lst=[laptop1,laptop2,laptop3,laptop4]
# for i in lst:
#     if 4 <= i.ram <= 16:
#         print(f"""
# kompyuter haqida malumot\n
# nomi: {i.name}\nRAM: {i.ram}\nnarxi: {i.price}\nProtsessori: {i.xotira}             
#               """)
    
    
    
# .............................................................................................

# 3 masala

# class users:
#     def __init__(self,ism,familiya,yosh,email,jinsi):
#         self.first_name=ism
#         self.last_name=familiya
#         self.age=yosh
#         self.email=email
#         self.jins=jinsi
        
#     def info(self):
#         print(f"""
# Foydalanuvchi ismi: {self.first_name}
# Foydalanuvchi familiyasi: {self.last_name}
# Foydalanuvchi yoshi: {self.age}
# Foydalanuvchi E-pochtasi: {self.email}
# Foydalanuvchi jinsi: {self.jins}             
#               """)


# F1=users("Ali","Aliyev",22,"aliyev@gmail.com","Erkak")
# F2=users("Madina","Karimova",18,"madina@2008.com","Ayol")
# F3=users("Vali","Valiyev",23,"valiyev@69.com","Erkak")
# F4=users("Gulchiroy","Ganiyeva",23,"Ganiyeva@12.com","Ayol")
# F5=users("Islombek","Shokirov",24,"shokirov2001@mail.com","Erkak")

# F1.info()
# F2.info()
# F3.info()
# F4.info()
# F5.info()


# lst=[F1,F2,F3,F4,F5]
# for i in lst:
#     if i.jins == "Erkak":
#                 print(f"""
# Erkaklar
# Foydalanuvchi ismi: {i.first_name}
# Foydalanuvchi familiyasi: {i.last_name}
# Foydalanuvchi yoshi: {i.age}
# Foydalanuvchi E-pochtasi: {i.email}
# Foydalanuvchi jinsi: {i.jins}             
#               """)
#     else:
#                         print(f"""
# Ayollar
# Foydalanuvchi ismi: {i.first_name}
# Foydalanuvchi familiyasi: {i.last_name}
# Foydalanuvchi yoshi: {i.age}
# Foydalanuvchi E-pochtasi: {i.email}
# Foydalanuvchi jinsi: {i.jins}             
#               """) 


            
        
    
    




