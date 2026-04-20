import os
import subprocess

def get_all_mdoc_files(directory):
    """获取目录下所有的mdoc文件"""
    result = subprocess.run(
        ['find', directory, '-name', '*.mdoc', '-type', 'f'],
        capture_output=True,
        text=True
    )
    files = result.stdout.strip().split('\n')
    return [f for f in files if f]

def get_relative_path(full_path):
    """获取相对路径"""
    if '/content/docs/' in full_path:
        return full_path.split('/content/docs/')[1]
    elif '/content_cn/docs/' in full_path:
        return full_path.split('/content_cn/docs/')[1]
    elif '/content/' in full_path:
        return full_path.split('/content/')[1]
    elif '/content_cn/' in full_path:
        return full_path.split('/content_cn/')[1]
    return full_path

def main():
    content_dir = '/Users/lichangsheng/Workspace.localized/Others/ag-grid/documentation/ag-grid-docs/src/content'
    content_cn_dir = '/Users/lichangsheng/Workspace.localized/Others/ag-grid/documentation/ag-grid-docs/src/content_cn'

    # 获取所有mdoc文件
    content_files = get_all_mdoc_files(content_dir)
    content_cn_files = get_all_mdoc_files(content_cn_dir)

    # 创建相对路径集合
    content_relative = {get_relative_path(f) for f in content_files}
    content_cn_relative = {get_relative_path(f) for f in content_cn_files}

    # 找出已翻译和未翻译的文件
    translated = content_relative & content_cn_relative
    untranslated = content_relative - content_cn_relative

    # 生成markdown报告
    report = []
    report.append("# AG Grid 文档翻译状态报告\n")
    report.append(f"生成时间: {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}\n\n")
    report.append("## 统计信息\n\n")
    report.append(f"- 总文件数: **{len(content_relative)}**\n")
    report.append(f"- 已翻译: **{len(translated)}** ✅\n")
    report.append(f"- 未翻译: **{len(untranslated)}** ❌\n")
    report.append(f"- 翻译进度: **{len(translated) / len(content_relative) * 100:.1f}%**\n\n")

    # 已翻译文件表格
    report.append("## 已翻译文件\n\n")
    report.append("| 序号 | 文件路径 | 状态 |\n")
    report.append("|------|----------|------|\n")
    for i, file_path in enumerate(sorted(translated), 1):
        report.append(f"| {i} | `{file_path}` | ✅ |\n")

    # 未翻译文件表格
    report.append("\n## 未翻译文件\n\n")
    report.append("| 序号 | 文件路径 | 状态 |\n")
    report.append("|------|----------|------|\n")
    for i, file_path in enumerate(sorted(untranslated), 1):
        report.append(f"| {i} | `{file_path}` | ❌ |\n")

    # 保存报告
    report_path = '/Users/lichangsheng/Workspace.localized/Others/ag-grid/translation_status.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.writelines(report)

    print(f"翻译状态报告已保存到: {report_path}")

if __name__ == "__main__":
    main()
