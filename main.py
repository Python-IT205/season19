def menu():
    print("1.Hiển thị danh sách công việc")
    print("2.Thêm mới công việc")
    print("3.Cập nhật tiến độ thực tế")
    print("4.Xoá công việc khỏi dự án")
    print("5.Thống kê trạng thái tiến độ")
    print("7.Phân loại tiến độ chương trình")
    print("8.Thoát chương trình")

def validate_input(prompt : str, input_type: str = "str"):
    while True:
        user_input = input(prompt)
        if not user_input:
            print("Không được để trống")
            continue
        if input_type == "int":
            try:
                value = int(user_input)
                if value <= 0 :
                    print("Phải là số dương")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ")
                continue
        if input_type == "match":
            try:
                value = int(user_input)
                if value <= 0:
                    print("Phải lớn 0 và tối thiểu 1 ngày")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ")
                continue
            return user_input

def index_calculation(difference_index):
    if difference_index < 0:
        print("Hoàn thành sớm")
    elif difference_index == 0:
        print("Bình thường")
    elif difference_index > 1 and difference_index < 3:
        print("Cần tăng tốc")
    else :
        print("Quá hạn")
        
def display_job(professions):
    if not professions:
        print("Danh sách rỗng")
        return
    print("===========Danh sách=========")
    print("Mã TS | Tên công việc    | Nhân viên | Ngày dự kiến | Ngày thực tế | Chêch lệch | Trạng thái tiến độ")
    for profession in professions:
        print(f"{profession.get('Mã TS')}  {profession.get('Nhiệm vụ') :<15} {profession.get('Tên nhân viên') :<15} {profession.get('Số ngày dự kiến'):<15} {profession.get('Số ngày thực tế') :<15} {profession.get('Chỉ số chêch lệch','Chưa tính toán') :<15} {profession.get('Trạng thái tiến độ','Chưa tính toán') :<15}")       

def add_job(professions):
    while True:
        code_new = validate_input("Nhập mã ts mới: ")
        for profession in professions:
            if code_new.lower() == profession.get('Mã TS').lower():
                print("Mã TS đã tồn tại")
                break
        else:
            job_new = validate_input("Nhập tên nhiệm vụ mới: ")
            name_new = validate_input("Nhập tên nhân viên mới: ")
            new_expected_date = validate_input("Nhập số ngày dự kiến mới:  ", "int")
            new_reality_date = validate_input("Nhập số ngày thực tế mới: ","int")
            difference_index = new_reality_date - new_expected_date
            
            new_job = {
                "Mã TS" : code_new,
                "Nhiệm vụ" : job_new,
                "Tên nhân viên" : name_new,
                "Số ngày dự kiến" : new_expected_date,
                "Số ngày thực tế" : new_reality_date,
                "Chỉ số chêch lệch" : difference_index,
                "Trạng thái tiến độ" : index_calculation(difference_index)
            }
            professions.append(new_job)
            print("Thêm mới công việc thành công")
            
def update_progress(professions):
    if not professions:
        print("Danh sách rỗng")
        return
    code_update = validate_input("Nhập mã cần cập nhật: ").upper()
    for profession in professions:
        if code_update.lower() == profession.get("Mã TS").lower():
            name_update = validate_input("Nhập tên cần cập nhật: ")
            expected_date_update = validate_input("Số ngày dự kiến cần cập nhật: ","int")
            reality_date_update = validate_input("Số ngày thực tế cần cập nhật: ","int")
            difference_index = new_reality_date - new_expected_date
            
            profession["Tên nhân viên"] = name_update
            profession["Số ngày dự kiến"] = expected_date_update
            profession["Số ngày thực tế"] = reality_date_update
            profession["Chỉ số chêch lệch"] = difference_index
            profession["Trạng thái tiến độ"] = index_calculation(difference_index)
    else:
        print("Không tìm thấy")

def remove_job(professions):
    if not professions:
        print("Danh sách rỗng")
        return
    remove_input = validate_input("Nhập mã công việc mà bạn muốn xoá: ")
    for profession in professions:
        if remove_input.lower() == profession.get("Mã TS").lower():
            confirm = input("Bạn có chắc chắn muốn xoá ? (Y/N) : ").upper()
            if confirm == "Y":
                professions.remove(remove_input)
            elif confirm == "N":
                break
            else:
                print("Chọn Y/N")

def find_job(professions):
    if not professions:
        print("Danh sách rỗng")
        return
    find_input = input("Nhập mã bạn cần tìm: ")
    find_user = []
    if find_input == "":
        print("Không được rỗng")
    for profession in professions:
        if find_input.lower() == profession.get("Mã TS").lower() or find_input.lower() in profession.get("Mã TS").lower():
            find_user.append(profession)
            display_job(professions)
    else:
        print("Không tìm thấy")
   
def statistical_job(difference_index):
    completed_early = 0
    normal = 0
    speed_run = 0
    overdue = 0
    if difference_index < 0:
        completed_early+=1
    elif difference_index == 0:
        normal+=1
    elif difference_index > 1 and difference_index < 3:
        speed_run+=1
    else :
        overdue+=1
    print(f"Hoàn thành sớm có: {completed_early} người")
    print(f"Bình thường có: {normal} người")
    print(f"Cần tăng tốc có: {speed_run} người")
    print(f"Quá hạn có: {overdue} người")

def main():
    professions = [
        {
        "Mã TS" : "TS001",
        "Nhiệm vụ" : "Thiết kế giao diện",
        "Tên nhân viên" : "Nguyễn Văn A",
        "Số ngày dự kiến" : 10,
        "Số ngày thực tế" : 14,
        "Chỉ số chêch lệch" : 4,
        "Trạng thái tiến độ" : "Quá hạn"
        }
    ]
    
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                display_job(professions)
            case "2":
                add_job(professions)
            case "3":
                update_progress(professions)
            case "4":
                remove_job(professions)
            case "5":
                find_job(professions)
            case "6":
                statistical_job(difference_index)
            case "8":
                break
            case _:
                print("Lựa chọn không hợp lệ")
main()