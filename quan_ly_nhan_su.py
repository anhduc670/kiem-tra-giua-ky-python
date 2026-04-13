import json
import os

class NhanVien:
    def __init__(self, ma_nv, ten, chuc_vu, du_an=None):
        self.ma_nv = ma_nv
        self.ten = ten
        self.chuc_vu = chuc_vu
        self.du_an = du_an if du_an else []

    def so_luong_du_an(self):
        return len(self.du_an)

    def to_dict(self):
        return {
            "ma_nv": self.ma_nv,
            "ten": self.ten,
            "chuc_vu": self.chuc_vu,
            "du_an": self.du_an
        }

    def __str__(self):
        return f"[{self.ma_nv}] {self.ten:25} | Chức vụ: {self.chuc_vu:15} | Dự án: {self.so_luong_du_an()}"


class QuanLyCongTy:
    FILE_DATA = "du_lieu_nhan_vien.json"

    def __init__(self):
        self.danh_sach_nhan_vien = {}
        # Mình đã vô hiệu hóa việc đọc file cũ ở đây. 
        # Nó sẽ luôn tạo mới danh sách 12 người này mỗi khi bạn chạy lại code!
        self.tao_du_lieu_mau()

    def tao_du_lieu_mau(self):
        print("⏳ Đang nạp danh sách nhân viên mới nhất từ code...")
        danh_sach = [
            NhanVien("NV01", "Nguyễn Văn A", "Developer", ["Dự án 1", "Dự án 2", "Dự án 3"]),
            NhanVien("NV02", "Trần Thị B", "Tester", ["Dự án 1"]),
            NhanVien("NV03", "Lê Văn C", "Manager", ["Dự án 1", "Dự án 2"]),
            NhanVien("NV04", "Phạm Văn D", "Designer", []),
            NhanVien("NV05", "Vũ Thị E", "Developer", ["Dự án 2"]),
            NhanVien("NV06", "Nguyễn Đức Cường", "Manager", ["Dự án 1", "Dự án 2", "Dự án 3", "Dự án 1", "Dự án 2"]),
            NhanVien("NV07", "Liêu Hoài Sơn", "Manager", ["Dự án 1", "Dự án 2", "Dự án 3", "Dự án 1", "Dự án 2", "Dự án 1", "Dự án 2"]),
            NhanVien("NV08", "Nguyễn Minh Triều", "Manager", ["Dự án 1", "Dự án 2"]),
            NhanVien("NV09", "Nguyễn Quý An", "Manager", ["Dự án 1", "Dự án 2", "Dự án 3", "Dự án 1", "Dự án 2"]),
            NhanVien("NV10", "Nguyễn Hữu Thắng", "Manager", []),
            NhanVien("NV11", "Nguyễn Nhất Linh", "Manager", ["Dự án 1", "Dự án 2", "Dự án 3", "Dự án 1", "Dự án 2", "Dự án 1"]),
            NhanVien("NV12", "Bùi Quang Huy", "Manager", ["Dự án 1", "Dự án 2", "Dự án 3"])
        ]
        for nv in danh_sach:
            self.danh_sach_nhan_vien[nv.ma_nv] = nv
        self.save_data() # Nạp xong thì lưu đè luôn vào file JSON mới

    def save_data(self):
        try:
            with open(self.FILE_DATA, 'w', encoding='utf-8') as f:
                data = [nv.to_dict() for nv in self.danh_sach_nhan_vien.values()]
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            pass # Bỏ qua lỗi hiển thị nếu có

    def them_nhan_vien(self, nv):
        if nv.ma_nv in self.danh_sach_nhan_vien:
            print(" Mã nhân viên đã tồn tại!")
        else:
            self.danh_sach_nhan_vien[nv.ma_nv] = nv
            self.save_data()

    def top_10_du_an(self, reverse=True):
        danh_sach = list(self.danh_sach_nhan_vien.values())
        danh_sach.sort(key=lambda x: x.so_luong_du_an(), reverse=reverse)
        return danh_sach[:10]

    def nhan_vien_1_du_an(self):
        return [nv for nv in self.danh_sach_nhan_vien.values() if nv.so_luong_du_an() == 1]

    def cat_giam_nhan_su(self, ma_nv):
        if ma_nv in self.danh_sach_nhan_vien:
            deleted_nv = self.danh_sach_nhan_vien.pop(ma_nv)
            self.save_data()
            print(f" Đã cho nghỉ việc: {deleted_nv.ten}")
        else:
            print(" Không tìm thấy mã nhân viên này.")

def menu():
    ql = QuanLyCongTy()
    
    while True:
        print("\n" + "="*50)
        print("     HỆ THỐNG QUẢN LÝ DỰ ÁN & NHÂN SỰ")
        print("="*50)
        print("1. Xem danh sách tất cả nhân viên")
        print("2. Thêm nhân viên mới")
        print("3. Top 10 nhân viên tham gia NHIỀU dự án nhất")
        print("4. Top 10 nhân viên tham gia ÍT dự án nhất")
        print("5. Danh sách nhân viên tham gia ĐÚNG 1 dự án")
        print("6. Cắt giảm nhân sự (Xóa nhân viên)")
        print("0. Thoát chương trình")
        print("-" * 50)
        
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            print("\nDANH SÁCH NHÂN VIÊN:")
            if not ql.danh_sach_nhan_vien:
                print("Danh sách đang trống!")
            else:
                for nv in ql.danh_sach_nhan_vien.values():
                    print(nv)
        elif choice == '2':
            ma = input("Nhập mã NV: ")
            ten = input("Nhập tên NV: ")
            cv = input("Nhập chức vụ: ")
            ds_da = input("Nhập các dự án (cách nhau bởi dấu phẩy, để trống nếu không có): ").split(',')
            ds_da = [d.strip() for d in ds_da if d.strip()]
            ql.them_nhan_vien(NhanVien(ma, ten, cv, ds_da))
            print(" Thêm nhân viên thành công.")
        elif choice == '3':
            print("\n TOP 10 NHIỀU DỰ ÁN NHẤT:")
            for nv in ql.top_10_du_an(reverse=True):
                print(nv)
        elif choice == '4':
            print("\n TOP 10 ÍT DỰ ÁN NHẤT:")
            for nv in ql.top_10_du_an(reverse=False):
                print(nv)
        elif choice == '5':
            print("\n NHÂN VIÊN CHỈ THAM GIA 1 DỰ ÁN:")
            danh_sach_1_du_an = ql.nhan_vien_1_du_an()
            if not danh_sach_1_du_an:
                print("Không có nhân viên nào tham gia đúng 1 dự án.")
            else:
                for nv in danh_sach_1_du_an:
                    print(f"Tên: {nv.ten:25} | Chức vụ: {nv.chuc_vu}")
        elif choice == '6':
            ma = input("Nhập mã nhân viên cần cắt giảm: ")
            ql.cat_giam_nhan_su(ma)
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()