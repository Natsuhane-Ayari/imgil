from PIL import Image
import sys

def split_image(input_file):
    try:
        # 開啟圖片
        img = Image.open(input_file).convert("RGBA")
        width, height = img.size

        # 建立透明背景的圖片
        img_odd = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        img_even = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        # 逐行處理
        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                if y % 2 == 0:  # 偶數行
                    img_even.putpixel((x, y), pixel)
                else:  # 奇數行
                    img_odd.putpixel((x, y), pixel)

        # 輸出結果
        base_name = input_file.rsplit('.', 1)[0]
        img_odd.save(f"{base_name}-1top.png", "PNG")
        img_even.save(f"{base_name}-2bottom.png", "PNG")
        print(f"輸出完成：{base_name}-1top.png, {base_name}-2bottom.png")

    except Exception as e:
        print(f"處理時出現錯誤：{e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法：python3 imgil.py <圖片檔案>")
    else:
        split_image(sys.argv[1])
