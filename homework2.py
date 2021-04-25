

class assigment:
    def __init__(self, name, p_num, gender):
        self.name = name
        self.p_num = p_num
        self.gender = gender
    
    def self_name(self):
        print("이름 : " %self.name)

    def self_p_num(self):
        print("전화번호 : " %self.p_num)

    def self_gender(self):
        print("성별 : " %self.gender)

    def __str__(self):
        return "이름은 " + self.name  + " ," + "전화번호는 " + self.p_num + " ," + "성별은 " + self.gender + "입니다."
 

persons = []

while 1:
    name =  input("이름을 입력해 주세요.")
    if ( name == "그만"):
        for i in persons:
            print(i)
        break
        
    else : 
        p_num = input("전화번호를 입력해 주세요.")
        gender = input("성별을 입력해 주세요.")
        if (gender != "female" and gender != "male"):
            gender = "unknown"
                
            
        infor = assigment(name, p_num, gender)
        persons.append(infor)
        print(infor, "")
    

