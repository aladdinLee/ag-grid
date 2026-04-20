import os

# 读取content文件列表
with open('/tmp/content_mdoc_files.txt', 'r') as f:
    content_files = set(line.strip() for line in f if line.strip())

# 读取content_cn文件列表
with open('/tmp/content_cn_mdoc_files.txt', 'r') as f:
    content_cn_files = set(line.strip() for line in f if line.strip())

# 创建相对路径映射
def get_relative_path(full_path):
    # 从完整路径中提取相对路径（相对于content或content_cn）
    if '/content/docs/' in full_path:
        return full_path.split('/content/docs/')[1]
    elif '/content_cn/docs/' in full_path:
        return full_path.split('/content_cn/docs/')[1]
    elif '/content/' in full_path:
        return full_path.split('/content/')[1]
    elif '/content_cn/' in full_path:
        return full_path.split('/content_cn/')[1]
    return full_path

# 创建已翻译文件的相对路径集合
translated_relative_paths = set()
for cn_file in content_cn_files:
    rel_path = get_relative_path(cn_file)
    translated_relative_paths.add(rel_path)

# 找出未翻译的文件
untranslated_files = []
for content_file in sorted(content_files):
    rel_path = get_relative_path(content_file)
    if rel_path not in translated_relative_paths:
        untranslated_files.append(content_file)

# 输出统计信息
print(f"总文件数: {len(content_files)}")
print(f"已翻译文件数: {len(content_cn_files)}")
print(f"未翻译文件数: {len(untranslated_files)}")
print()

# 输出前50个未翻译的文件
print("前50个未翻译的文件:")
for i, file in enumerate(untranslated_files[:50], 1):
    print(f"{i}. {file}")

# 保存未翻译文件列表
with open('/tmp/untranslated_files.txt', 'w') as f:
    for file in untranslated_files:
        f.write(file + '\n')

print(f"\n未翻译文件列表已保存到 /tmp/untranslated_files.txt")
