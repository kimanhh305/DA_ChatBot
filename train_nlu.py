# Imports
#-----------
# rasa nlu
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

# Ham train NLU
#------------
def train (data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')


# Tien hanh train modul NLU
# Input : File nlu.md
# Output: Model NLU trong thu mục models/nlu
train('data/nlu.md', 'config/config.yml', 'models/nlu')

# Load modul NLU
interpreter = Interpreter.load('./models/nlu/default/chat')

# Ham test NLU
def ask_question(text):
    print(interpreter.parse(text))


ask_question("xin chào")
ask_question("Cảm ơn")
ask_question("Tạm biệt em nhé")
ask_question("Mất thẻ sinh viên")
ask_question("Giấy xác nhận thực tập lấy ở đâu")
ask_question("Dieu kien de lam khoa luan tot nghiep")
ask_question("Cong ty thuc tap do khoa sap xep hay tu tim")
ask_question("Co dang ky HCS trong hoc ky he duoc khong")
ask_question("Hè có mở lớp hcs không")
ask_question("rot mon thi lai")
ask_question("Ky sinh hoat cong dan")
ask_question("Hufi co day toeic khong")
ask_question("Tieu chuan dau ra la tieng anh hay tieng nhat")
ask_question("Luc nao nop cac chung chi lien quan")
ask_question("Phong nao phuc khao diem thi")
ask_question("Xet hoc vu vao thoi gian nao")
ask_question("Xin giay hoan nghia vu quan su")
ask_question("Bi thoi hoc")
ask_question("Gap ai de bao thay doi tam tru")
ask_question("Khi nao xet hoc bong")
ask_question("Sinh vien cai thien dem nhu the nao")
ask_question("Sinh vien muon ru hoc phan da dang ky")
ask_question("Dang ky hoc phan can biet nhung gi")
ask_question("Phong ban giai quyet thac mac hoc phi")
ask_question("Truong co KTX nao khong")
ask_question("Lien he voi CLB nhu the nao")
ask_question("Cap nhat thong tin sinh vien o dau")
ask_question("Can duoc tu van ve viec hoc Anh Van dau vao")
ask_question("Khong xem duoc thoi khoa bieu")
ask_question("Quyen loi khi tham gia BHYT")
ask_question("Thoi gian bieu cac tiet buoi chieu")
ask_question("Phong CTCT - HSSV giai quyet van de gi")
ask_question("Cac hoat dong cua trung tam ngoai ngu")
ask_question("Quy dinh ve tin chi ra truong")
ask_question("So tiet toi da cua mot tin chi")
ask_question("Hoc phan tuong duong quy dinh the nao")
ask_question("Quy dinh xep loai tot nghiep")

