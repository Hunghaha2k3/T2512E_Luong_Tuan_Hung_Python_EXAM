# Bài 2: Làm việc với file CSV bằng pandas
import pandas as pd

# Chỉ định trực tiếp tên file dưới dạng chuỗi
CSV_FILE = "products.csv"

# Bước 1: Tạo DataFrame với 4 cột id, name, price, quantity
def create_dataframe():
    data = {
        "id":[1, 2, 3, 4, 5],
        "name": ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"],
        "price": [25.0, 50.0, 75.0, 100.0, 125.0],
        "quantity": [100, 70, 180, 30, 90]
    }
    return pd.DataFrame(data)

# Hàm main
def main():
    # 1. Tạo DataFrame
    df = create_dataframe()
    # 2. Lưu ra products.csv (index=False: không ghi cột chỉ số 0,1,2...)
    df.to_csv(CSV_FILE, index=False)
    print(f"Saved data to {CSV_FILE}")
    # 3. Đọc lại file CSV vào DataFrame mới
    products = pd.read_csv(CSV_FILE)
    # 4. Hiển thị tất cả sản phẩm
    print("\n===== ALL PRODUCTS =====")
    print(products.to_string(index=False))
    # 5. Lọc sản phẩm có price > 100
    print("\n===== PRODUCTS WITH PRICE > 100 =====")
    expensive = products[products["price"] > 100]
    print(expensive.to_string(index=False))
    # 6. Tính tổng giá trị tồn kho = tổng (price * quantity) của mọi sản phẩm
    total_value = (products["price"] * products["quantity"]).sum()
    print("\n===== TOTAL INVENTORY VALUE =====")
    print(f"Total inventory value: {total_value:.2f}")
    # 7. Thêm cột mới total = price * quantity
    products["total"] = products["price"] * products["quantity"]
    print("\n===== PRODUCTS WITH NEW COLUMN 'total' =====")
    print(products.to_string(index=False))
    # 8. Lưu đè lại products.csv (đã có thêm cột total)
    products.to_csv(CSV_FILE, index=False)
    print(f"\nUpdated {CSV_FILE} with column 'total'")

if __name__ == "__main__":
    main()
