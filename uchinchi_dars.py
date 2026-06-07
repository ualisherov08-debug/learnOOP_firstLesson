# class email:
    
#     def send(self, massege):
        
#         print(f"Email orqali yuborildi: {massege}")
        
# class sms:
    
#     def send(self, massege):
#         print(f"SMS orqali yuborildi: {massege}")
          
# class telegram:
    
#     def send(self, massege):
#         print(f"Telegram orqali yuborildi: {massege}")
        
# a1=email()
# a2=sms()
# a3=telegram()

 
# lst=[a1,a2,a3]  
# for i in  lst:
#     i.send("Kurs ertaga boshlanadi")

# ............................................................................
# class google:
#     def login(self,username):
#         print(f"google orqali {username} tizimga kirdi: ")
        
# class telegram:
#     def login(self,username):
#         print(f"telegram orqali {username} tizimga kirdi: ")

# class emaillogin:
#     def login(self,username):
#         print(f"emaillogin orqali {username} tizimga kirdi: ")
        
# a1=google()
# a2=telegram()
# a3=emaillogin()

# lst=[a1,a2,a3]
# for i in lst:
#     i.login("Ali")


# ...................................................................................................

# class shape:
#     def __init__(self):
#         self.symbol="*"
#         self.length=5
        
#     def setSymbol(self,symbol):
#         if symbol:
#             self.symbol=symbol
    
#     def setLength(self,length):
#         if length:
#             self.length=length
    
#     def show(self):
#         return ""
    
# class Line(shape):
#     def show(self):
#         return self.symbol * self.length
    
# class Triangle(shape):
#     def show(self):
#         lines = [self.symbol * i for i in range(1, self.length + 1)]
#         return "\n".join(lines)    
    
# class Rectangle(shape):
#     def show(self):
#         lines = [self.symbol * self.length for _ in range(self.length)]
#         return "\n".join(lines)

# class NullShape(shape):
#     def show(self):
#         return "Bo'sh shakl"

# a1= Line()
# a2=Triangle()
# a3=Rectangle()
# a4=NullShape()
# shapes=[a1,a2,a3,a4]
# for i in shapes:
#     print(i.show())
#     print("___________________________________")


# ..........................................................................................

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< uyga vazifa >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class MyDate:
    def __init__(self, kun, oy, yil):
        self.day = kun
        self.month = oy
        self.year = yil
        self.MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun","Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
        self.DAY_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def isLeapYear(self, yil):
        if yil % 4 == 0:
            return True
        else:
            return False

    def isValidDate(self, kun, oy, yil):
        if yil < 1 or yil > 9999:
            return False
        if oy < 1 or oy > 12:
            return False
        
        if oy == 2 and self.isLeapYear(yil):
            max_kun = 29
        else:
            max_kun = self.DAY_IN_MONTHS[oy - 1]
            
        if kun < 1 or kun > max_kun:
            return False
            
        return True

    def setDate(self, kun, oy, yil):
        if self.isValidDate(kun, oy, yil):
            self.day = kun
            self.month = oy
            self.year = yil
        else:
            print("Notogri sana kiritdingiz")

    def nextDay(self):
        if self.month == 2 and self.isLeapYear(self.year):
            max_kun = 29
        else:
            max_kun = self.DAY_IN_MONTHS[self.month - 1]
        self.day = self.day + 1

        if self.day > max_kun:
            self.day = 1        
            self.month = self.month + 1  

        if self.month > 12:
            self.month = 1       
            self.year = self.year + 1
            
        return self

    def previousDay(self):
        self.day = self.day - 1
        if self.day < 1:
            self.month = self.month - 1
            if self.month < 1:
                self.month = 12          
                self.year = self.year - 1  
            
            if self.month == 2 and self.isLeapYear(self.year):
                self.day = 29
            else:
                self.day = self.DAY_IN_MONTHS[self.month - 1]
                
        return self

    def __str__(self):
        oy_nomi = self.MONTHS[self.month - 1]
        return f"{self.day}-{oy_nomi} {self.year} yil"

sana1 = MyDate(15, 6, 2023)
sana1.nextDay()
print(sana1) 
sana2 = MyDate(30, 4, 2023)
sana2.nextDay()
print(sana2) 
sana3 = MyDate(31, 12, 2023)
sana3.nextDay()
print(sana3)  
sana4 = MyDate(1, 5, 2023)
sana4.previousDay()
print(sana4) 
