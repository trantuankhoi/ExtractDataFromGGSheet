CREDENTIAL_PATH = "/Users/KhoiTT/FTECH/02_Datasets/Tools/ExtractData/client_secret_567159421126-ho30t3hkj6i8s9ak8c6jdhf9hjj0suel.apps.googleusercontent.com.json"
SCOPES = ['https://www.googleapis.com/auth/drive']

SHEET_DIR = "/Users/KhoiTT/FTECH/02_Datasets/Tools/ExtractData/sheets" # folder chứa các file sheets cần extract 
FOLDER_IDS = ["1C71jFb04hf56z5yM8r7PLMw2vgyW9mfN"] # folder id lấy trong đường dẫn của folder trên drive

COLUMN_INSTANCE_ID = 0 
COLUMN_IMG_ID = 2
COLUMN_GT_ID = 4
CONFUSE_COLUMN_ID = 7

IMAGE_DIR = "/Users/KhoiTT/FTECH/02_Datasets/Tools/ExtractData/task_3" # folder chứa ảnh instances đã được extract
GT_NAME = "test.txt" # tên file ground truth, lưu trong IMAGE_DIR