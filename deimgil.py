from PIL import Image
import sys

def deinterlace_images(img1_path, img2_path):
    try:
        # 開啟圖片
        img1 = Image.open(img1_path).convert("RGBA")
        img2 = Image.open(img2_path).convert("RGBA")

        # 確保兩張圖片大小相同
        if img1.size != img2.size:
            raise ValueError("兩張圖片大小不一致，無法解交錯。")

        width, height = img1.size

        # 建立輸出圖片
        img1_deil = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        img2_deil = Image.new("RGBA", (width, height), (0, 0, 0, 0))

        # 解交錯
        for y in range(height):
            for x in range(width):
                if y % 2 == 0:  # 偶數行
                    img1_deil.putpixel((x, y), img2.getpixel((x, y)))
                    img2_deil.putpixel((x, y), img1.getpixel((x, y)))
                else:  # 奇數行
                    img1_deil.putpixel((x, y), img1.getpixel((x, y)))
                    img2_deil.putpixel((x, y), img2.getpixel((x, y)))

        # 輸出結果
        base_name1 = img1_path.rsplit('.', 1)[0]
        base_name2 = img2_path.rsplit('.', 1)[0]
        img1_deil.save(f"{base_name1}-deil.png", "PNG")
        img2_deil.save(f"{base_name2}-deil.png", "PNG")

        print(f"輸出完成：{base_name1}-deil.png, {base_name2}-deil.png")

    except Exception as e:
        print(f"處理時出現錯誤：{e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：python3 deimgil.py <圖片1> <圖片2>")
    else:
        deinterlace_images(sys.argv[1], sys.argv[2])

