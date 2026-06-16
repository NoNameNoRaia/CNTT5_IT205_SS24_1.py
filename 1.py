# Hệ thống quản lý hóa đơn Rikkei Coffee - Refactored
class CoffeeOrder:
    _vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0  

    @property
    def total_amount(self):
        return self.__total_amount

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    # Tính tổng tiền khách phải trả (đã cộng VAT)
    def calculate_final_bill(self):
        return self.__total_amount + (self.__total_amount * self._vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        if 0 <= new_rate <= 1: # Đảm bảo tỷ lệ thuế hợp lệ
            cls._vat_rate = new_rate

    @property
    def vat_rate(self):
        return self._vat_rate


order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

# Khách gọi món
order_table1.add_item(50000) 
order_table2.add_item(30000) 

print("--- THỬ NGHIỆM TẤN CÔNG & CẬP NHẬT HỆ THỐNG ---")

try:
    order_table1.total_amount = 0
except AttributeError:
    print("[Hệ thống bảo mật]: Từ chối hành vi can thiệp/ghi đè trực tiếp vào tổng tiền hóa đơn!")

order_table1.__total_amount = 0 

CoffeeOrder.update_vat_rate(0.08)


print("\n--- KẾT QUẢ HIỂN THỊ TRÊN CONSOLE ---")
print(f"Tổng tiền Bàn 1 (sau VAT): {order_table1.calculate_final_bill()} VNĐ")

print(f"Thuế VAT đang áp dụng cho Bàn 1: {order_table1.vat_rate * 100}%")
print(f"Thuế VAT đang áp dụng cho Bàn 2: {order_table2.vat_rate * 100}%")
'''
1.Việc gán trực tiếp order_table1.total_amount = 0 từ bên ngoài đang vi phạm tính đóng gói (encapsulation). Tính đóng gói yêu cầu rằng các thuộc tính của một đối 
tượng nên được bảo vệ khỏi việc truy cập và sửa đổi trực tiếp từ bên ngoài lớp. Điều này giúp bảo vệ dữ liệu và duy trì tính nhất quán của trạng thái đối tượng.
2.Để kích hoạt cơ chế Name Mangling, ta cần đổi tên thuộc tính total_amount thành __total_amount. Việc thêm hai dấu gạch dưới (__) ở đầu tên thuộc tính sẽ khiến 
Python tự động biến đổi tên thuộc tính thành _CoffeeOrder__total_amount, giúp bảo vệ nó khỏi việc truy cập trực tiếp từ bên ngoài.
3.Để cho phép các phần khác của chương trình xem được tổng tiền mà không được sửa, ta cần sử dụng decorator @property. Decorator này cho phép ta định nghĩa một phương 
thức như một thuộc tính, từ đó có thể truy cập mà không cần phải gọi phương thức.
4.Tại dòng lệnh self.vat_rate = new_rate, Python đang thực hiện việc gán giá trị new_rate cho thuộc tính vat_rate của đối tượng hiện tại (instance). Tuy nhiên, nếu 
vat_rate không được định nghĩa là một thuộc tính của đối tượng, Python sẽ tạo một thuộc tính mới cho đối tượng đó.
5.Để phương thức update_vat_rate có thể thay đổi biến vat_rate cho toàn bộ các hóa đơn, ta cần sử dụng decorator @classmethod
'''