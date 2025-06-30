# 豆瓣电影Top250爬虫

本项目用于爬取豆瓣电影Top250的电影名称和评分，并保存为CSV文件。

## 推荐使用虚拟环境

### 使用 venv 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate   # Windows
```

### 或使用 uv（更快的包管理器）

```bash
uv venv
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows
```

## 使用方法

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   # 或
   uv pip install -r requirements.txt
   ```
2. 运行爬虫：
   ```bash
   python main.py
   ```

3. 结果会保存在 `douban_top250.csv` 文件中。

## 视频预览

你可以在下方直接观看项目运行效果视频：

<video src="https://github.com/user-attachments/assets/91eec5e1-3842-408a-a5e0-6cc809a69806" controls width="600"></video>

> 如无法播放，请前往 [issue 页面](https://github.com/dqymd/crawl/issues/1#issue-3187035468) 查看。