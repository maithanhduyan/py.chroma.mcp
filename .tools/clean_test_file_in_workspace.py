import os
import sys


def main():
    # Xác định thư mục gốc (workspace) - thư mục cha của thư mục chứa script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.dirname(script_dir)

    # Kiểm tra sự tồn tại
    if not os.path.exists(workspace_dir):
        print(f"Thư mục workspace không tồn tại: {workspace_dir}")
        return

    print("=" * 50)
    print(f"[Thông tin hệ thống]")
    print(f"File script    : {os.path.abspath(__file__)}")
    print(f"Thư mục script : {script_dir}")
    print(f"Thư mục làm việc: {os.getcwd()}")
    print(f"Đang quét đệ quy: {workspace_dir}")
    print("=" * 50)

    # Quét đệ quy và xóa file
    deleted_count = 0
    error_count = 0

    for foldername, subfolders, filenames in os.walk(workspace_dir):
        # Bỏ qua thư mục .venv
        if ".venv" in foldername.split(os.sep):
            continue
        for filename in filenames:
            if filename.startswith("test_") and filename.endswith(".py"):
                file_path = os.path.join(foldername, filename)
                try:
                    os.remove(file_path)
                    print(f"✅ Đã xóa: {file_path}")
                    deleted_count += 1
                except Exception as e:
                    print(f"❌ Lỗi khi xóa {file_path}: {str(e)}")
                    error_count += 1

    # Báo cáo kết quả
    print("\n" + "=" * 50)
    print(f"✨ Tổng kết:")
    print(f"- Số file đã xóa: {deleted_count}")
    print(f"- Số file gặp lỗi: {error_count}")
    print("=" * 50)


if __name__ == "__main__":
    main()
