#  Uyga vazifa

# class Student:
#     def __init__(self, name: str, student_id: str):
#         self.name = name
#         self.student_id = student_id
#         self.__grades = []

#     def add_grade(self, grade: int):
#         if 0 <= grade <= 100:
#             self.__grades.append(grade)
#         else:
#             print("Notogri baho")

#     def calculate_average(self) -> float:
#         if len(self.__grades) == 0:
#             return 0.0
#         return sum(self.__grades) / len(self.__grades)

#     def get_status(self) -> str:
#         avg = self.calculate_average()

#         if 90 <= avg <= 100:
#             return "Alo"
#         elif 80 <= avg < 90:
#             return "Yaxshi"
#         elif 70 <= avg < 80:
#             return "Qoniqarli"
#         else:
#             return "Qoniqarsiz"

# student = Student("Nodira", "S123")

# student.add_grade(85)
# student.add_grade(90)

# print(student.calculate_average())
# print(student.get_status())

# student.add_grade(150)

# ....................................................................................

# class ishchilar:
#     def __init__(self,name:str,ischi_Id:str,kun_soat:float=12.0):
#         self.name=name
#         self.id=ischi_Id
#         self.ish_soati=[]
#         self.ishlagan_soat=kun_soat
        
#     def I_soat(self,soat):
#         if 0 <= soat <= 24:
#             self.ish_soati.append(soat)
#             return True
#         return False
    
#     def U_soat(self):
#         return sum(self.ish_soati)
    
#     def oylik(self):
#         return self.U_soat() * self.ishlagan_soat
    
# ishchi=ishchilar("asror","a001")

# print(ishchi.I_soat(8))
# print(ishchi.I_soat(12))
# print(ishchi.U_soat())
# print(ishchi.oylik())

# ............................................................................

class Playlist:
    def __init__(self, owner: str):
        self.owner = owner
        self.tracks = []

    def add_track(self, title: str, artist: str):
        self.tracks.append((title, artist))

    def remove_last(self):
        if self.tracks:
            return self.tracks.pop()

    def total_tracks(self):
        return len(self.tracks)

    def unique_tracks(self):
        unique = []
        for track in self.tracks:
            if track not in unique:
                unique.append(track)
        return unique

    def search_by_title(self, title: str):
        natija = []
        for track in self.tracks:
            if track[0] == title:
                natija.append(track)
        return natija

    def filter_by_artist(self, artist: str):
        natija = []
        for track in self.tracks:
            if track[1] == artist:
                natija.append(track)
        return natija

playlist = Playlist("Ulug'bek")

playlist.add_track("Bolaveradi", "Xurshid Rasulov")
playlist.add_track("Tulki", "Xurshid Rasulov")
playlist.add_track("Eni xotin boqmasin", "Xurshid Rasulov")
playlist.add_track("Alida u 2", "Doxxim")

print(playlist.total_tracks())
print(playlist.unique_tracks())
print(playlist.search_by_title("Bolaveradi"))
print(playlist.filter_by_artist("Xurshid Rasulov"))
print(playlist.remove_last())
print(playlist.total_tracks())