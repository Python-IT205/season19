def display_orders(orders_list):
    if not orders_list:
        print("\n[THÔNG BÁO]: Danh sách đơn hàng hiện đang trống.")
        return
    print("\n" + "="*70)
    print(f"{'MÃ ĐH':<10} | {'TÊN ĐẠI LÝ':<25} | {'GIÁ TRỊ (VND)':<15} | {'TRẠNG THÁI':<12}")
    print("-" * 70)
    for order in orders_list:
        print(f"{order['id']:<10} | {order['name']:<25} | {order['price']:>14,} | {order['status']:<12}")
    print("="*70)

def add_order(orders_list):
    print("\n--- THÊM MỚI ĐƠN HÀNG ĐẠI LÝ ---")    
    while True:
        order_id = input("Nhập mã đơn hàng: ").strip()
        if not order_id:
            print("Lỗi: Mã đơn hàng không được để trống. Vui lòng nhập lại.")
            continue
        is_duplicate = False
        for order in orders_list:
            if order['id'].upper() == order_id.upper():
                is_duplicate = True
                break
        if is_duplicate:
            print(f"\n[MÃ LỖI ERR-01]: Mã đơn hàng '{order_id}' đã tồn tại trên hệ thống. Hủy thao tác!")
            return
        break
    while True:
        agent_name = input("Nhập tên đại lý: ").strip()
        if not agent_name:
            print("Lỗi: Tên đại lý không được để trống. Vui lòng nhập lại.")
            continue
        break

    while True:
        try:
            price = int(input("Nhập giá trị đơn hàng (VND): "))
            if price <= 0:
                print("Lỗi: Giá trị đơn hàng phải là số nguyên lớn hơn 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Lỗi: Giá trị đơn hàng phải là số nguyên hợp lệ. Vui lòng nhập lại.")

    new_order = {
        'id': order_id,
        'name': agent_name,
        'price': price,
        'status': 'Unpaid'
    }
    orders_list.append(new_order)
    print(f"\n[THÀNH CÔNG]: Đã thêm mới đơn hàng {order_id} thành công!")


def update_payment_status(orders_list):
    print("\n--- CẬP NHẬT TRẠNG THÁI THANH TOÁN ---")
    order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip()
    
    if not order_id:
        print("Lỗi: Mã đơn hàng không được để trống.")
        return

    for order in orders_list:
        if order['id'].upper() == order_id.upper():
            if order['status'] == 'Unpaid':
                order['status'] = 'Paid'
                print(f"\n[THÀNH CÔNG]: Đơn hàng {order['id']} đã chuyển sang trạng thái 'Paid'.")
                return
            elif order['status'] == 'Paid':
                print(f"\n[MÃ LỖI ERR-04]: Đơn hàng {order['id']} đã ở trạng thái 'Paid' từ trước.")
                return

    print(f"\n[MÃ LỖI ERR-03]: Không tìm thấy mã đơn hàng '{order_id}' trên hệ thống.")


def calculate_revenue(orders_list):
    total_revenue = 0
    
    for order in orders_list:
        if order['status'] == 'Paid':
            total_revenue += order['price']
            
    if total_revenue >= 100000000:
        discount_percentage = 5
    else:
        discount_percentage = 0
        
    discount_amount = int(total_revenue * (discount_percentage / 100))
    
    return total_revenue, discount_percentage, discount_amount


def main():
    orders = [
        {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
        {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
    ]
    
    while True:
        print("\n" + "="*15 + " QUÂN LÝ ĐƠN HÀNG - AGENT ORDER " + "="*15)
        print("1. Xem danh sách đơn hàng hiện có")
        print("2. Tạo mới đơn hàng đại lý")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & Chiết khấu")
        print("5. Thoát chương trình")
        print("=" * 62)
        
        try:
            choice = int(input("Nhập lựa chọn của bạn (1-5): "))
        except ValueError:
            print("\nLỗi: Vui lòng chỉ nhập số từ 1 đến 5!")
            continue
            
        if choice == 1:
            display_orders(orders)
        elif choice == 2:
            add_order(orders)
        elif choice == 3:
            update_payment_status(orders)
        elif choice == 4:
            revenue, discount_p, discount_v = calculate_revenue(orders)
            print("\n" + "-"*20 + " BÁO CÁO DOANH THU " + "-"*20)
            print(f"Tổng doanh thu thực tế (Paid): {revenue:,} VND")
            print(f"Mức chiết khấu áp dụng    : {discount_p}%")
            print(f"Số tiền chiết khấu         : {discount_v:,} VND")
            if discount_p > 0:
                print("-> Hệ thống đạt mốc chiết khấu (đạt từ 100,000,000 VND).")
            else:
                print("-> Hệ thống chưa đạt mốc chiết khấu (dưới 100,000,000 VND).")
            print("-" * 59)
        elif choice == 5:
            print("\nCảm ơn bạn đã sử dụng hệ thống. Tạm biệt và hẹn gặp lại!")
            break
        else:
            print("\nLỗi: Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 5.")

if __name__ == "__main__":
    main()