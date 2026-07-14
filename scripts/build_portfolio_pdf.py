from pathlib import Path
from textwrap import shorten

from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "public" / "images"
OUTPUT = ROOT / "output" / "pdf" / "肖雨菲-软件工程个人作品集.pdf"
PAGE_W, PAGE_H = A4
MARGIN = 42
BLUE = HexColor("#e8f0fe")
ACCENT = HexColor("#5275b8")
TEXT = HexColor("#1f2937")
MUTED = HexColor("#64748b")
LINE = HexColor("#dfe5ee")


def register_fonts():
    regular = Path(r"C:\Windows\Fonts\msyh.ttc")
    bold = Path(r"C:\Windows\Fonts\msyhbd.ttc")
    pdfmetrics.registerFont(TTFont("CN", str(regular)))
    pdfmetrics.registerFont(TTFont("CN-Bold", str(bold if bold.exists() else regular)))


def wrap(text, font, size, width):
    lines, current = [], ""
    for char in text:
        candidate = current + char
        if pdfmetrics.stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_text(c, text, x, y, width, size=10, leading=17, color=TEXT, font="CN"):
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_image_fit(c, path, x, y, width, height, background=HexColor("#f8fafc")):
    c.setFillColor(background)
    c.roundRect(x, y, width, height, 6, fill=1, stroke=0)
    with Image.open(path) as image:
        iw, ih = image.size
    scale = min(width / iw, height / ih)
    dw, dh = iw * scale, ih * scale
    c.drawImage(str(path), x + (width - dw) / 2, y + (height - dh) / 2, dw, dh, preserveAspectRatio=True, mask="auto")


def header(c, label, title, subtitle=None):
    c.setFillColor(BLUE)
    c.roundRect(MARGIN, PAGE_H - 112, PAGE_W - MARGIN * 2, 70, 8, fill=1, stroke=0)
    c.setFillColor(ACCENT)
    c.setFont("CN-Bold", 8)
    c.drawString(MARGIN + 18, PAGE_H - 67, label)
    c.setFillColor(TEXT)
    c.setFont("CN-Bold", 20)
    c.drawString(MARGIN + 18, PAGE_H - 91, title)
    if subtitle:
        c.setFillColor(MUTED)
        c.setFont("CN", 8)
        c.drawRightString(PAGE_W - MARGIN - 18, PAGE_H - 88, subtitle)


def footer(c, page):
    c.setStrokeColor(LINE)
    c.line(MARGIN, 31, PAGE_W - MARGIN, 31)
    c.setFillColor(MUTED)
    c.setFont("CN", 7.5)
    c.drawString(MARGIN, 18, "肖雨菲 · 软件工程个人作品集")
    c.drawRightString(PAGE_W - MARGIN, 18, f"{page}")


def pill(c, text, x, y):
    width = pdfmetrics.stringWidth(text, "CN", 8) + 16
    c.setFillColor(BLUE)
    c.roundRect(x, y - 4, width, 19, 6, fill=1, stroke=0)
    c.setFillColor(TEXT)
    c.setFont("CN", 8)
    c.drawString(x + 8, y + 1, text)
    return x + width + 7


def project_page(c, page, title, image, stack, overview, duties, outcome, repo):
    header(c, "PROJECT", title, "独立开发者 · 2026.07 - 至今")
    draw_image_fit(c, image, MARGIN, PAGE_H - 355, PAGE_W - MARGIN * 2, 220, BLUE)
    y = PAGE_H - 382
    x = MARGIN
    for item in stack:
        x = pill(c, item, x, y)
    y -= 34
    c.setFont("CN-Bold", 11)
    c.setFillColor(TEXT)
    c.drawString(MARGIN, y, "项目概述")
    y = draw_text(c, overview, MARGIN, y - 20, PAGE_W - MARGIN * 2, 9.5, 16)
    y -= 5
    c.setFont("CN-Bold", 11)
    c.drawString(MARGIN, y, "核心职责")
    y = draw_text(c, duties, MARGIN, y - 20, PAGE_W - MARGIN * 2, 9.5, 16)
    y -= 5
    c.setFont("CN-Bold", 11)
    c.drawString(MARGIN, y, "项目成果")
    y = draw_text(c, outcome, MARGIN, y - 20, PAGE_W - MARGIN * 2, 9.5, 16)
    c.setFillColor(ACCENT)
    c.setFont("CN", 8.5)
    c.drawString(MARGIN, 48, repo)
    footer(c, page)
    c.showPage()


def award_block(c, y, image, title, award, date, description):
    height = 258
    c.setStrokeColor(LINE)
    c.roundRect(MARGIN, y - height, PAGE_W - MARGIN * 2, height, 8, fill=0, stroke=1)
    draw_image_fit(c, image, MARGIN + 14, y - height + 14, 220, height - 28, BLUE)
    tx = MARGIN + 252
    ty = y - 30
    c.setFillColor(TEXT)
    c.setFont("CN-Bold", 12)
    ty = draw_text(c, title, tx, ty, PAGE_W - tx - MARGIN - 15, 12, 20, TEXT, "CN-Bold")
    c.setFillColor(ACCENT)
    c.setFont("CN-Bold", 11)
    c.drawString(tx, ty - 8, award)
    c.setFillColor(MUTED)
    c.setFont("CN", 8.5)
    c.drawString(tx, ty - 30, date)
    draw_text(c, description, tx, ty - 58, PAGE_W - tx - MARGIN - 15, 9, 16, MUTED)
    return y - height - 18


def build():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("肖雨菲 - 软件工程个人作品集")

    # Page 1: profile
    c.setFillColor(BLUE)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(HexColor("#ffffff"))
    c.roundRect(MARGIN, MARGIN, PAGE_W - MARGIN * 2, PAGE_H - MARGIN * 2, 12, fill=1, stroke=0)
    draw_image_fit(c, IMAGES / "profile-photo.jpg", MARGIN + 28, PAGE_H - 310, 155, 205, BLUE)
    c.setFillColor(ACCENT)
    c.setFont("CN-Bold", 9)
    c.drawString(MARGIN + 215, PAGE_H - 122, "SOFTWARE ENGINEERING PORTFOLIO")
    c.setFillColor(TEXT)
    c.setFont("CN-Bold", 28)
    c.drawString(MARGIN + 215, PAGE_H - 160, "肖雨菲")
    c.setFont("CN", 12)
    c.setFillColor(MUTED)
    c.drawString(MARGIN + 215, PAGE_H - 188, "中山大学 · 软件工程专业")
    draw_text(c, "面向软件开发、后端开发与 AI 辅助开发实习岗位。计划向 AI 与算法方向持续发展，具备较强的学习主动性、责任意识和代码实践能力。", MARGIN + 215, PAGE_H - 225, 300, 10, 18, TEXT)
    c.setFillColor(TEXT)
    c.setFont("CN-Bold", 13)
    c.drawString(MARGIN + 28, PAGE_H - 355, "教育背景")
    draw_text(c, "中山大学 · 软件工程 · 2025.08 - 至今", MARGIN + 28, PAGE_H - 382, 480, 10, 18)
    c.setFont("CN-Bold", 13)
    c.setFillColor(TEXT)
    c.drawString(MARGIN + 28, PAGE_H - 452, "核心技能")
    x, y = MARGIN + 28, PAGE_H - 482
    for item in ["C / C++", "Python", "Git / GitHub", "算法基础", "Node.js", "AI 辅助开发"]:
        x = pill(c, item, x, y)
        if x > PAGE_W - 120:
            x, y = MARGIN + 28, y - 28
    c.setFont("CN-Bold", 13)
    c.setFillColor(TEXT)
    c.drawString(MARGIN + 28, PAGE_H - 548, "个人优势")
    advantages = [
        "熟练使用 C/C++，能够独立完成编码、运行调试与常见问题排查。",
        "掌握 Python 基础，可编写实用脚本并应用于基础 Web 项目。",
        "熟练使用 Codex、GitHub Copilot 辅助开发，并主动核验代码逻辑与运行结果。",
        "具有程序设计与数学竞赛经历，具备良好的逻辑分析和持续学习能力。",
    ]
    y = PAGE_H - 578
    for item in advantages:
        c.setFillColor(ACCENT)
        c.circle(MARGIN + 34, y + 3, 2.5, fill=1, stroke=0)
        y = draw_text(c, item, MARGIN + 46, y, PAGE_W - MARGIN * 2 - 55, 9.5, 17)
        y -= 5
    c.setFillColor(MUTED)
    c.setFont("CN", 8.5)
    c.drawString(MARGIN + 28, 76, "GitHub: https://github.com/xiaoyf-debug")
    c.drawString(MARGIN + 28, 58, "Email: xiaoyf66@mail2.sysu.edu.cn｜3868085823@qq.com")
    footer(c, 1)
    c.showPage()

    project_page(
        c, 2, "AI 学习规划与复盘助手", IMAGES / "project-ai-study-coach.png",
        ["Node.js", "JavaScript", "LocalStorage", "学习路径"],
        "面向软件工程学习规划场景，根据知识点重要度、掌握程度、难度和前置依赖生成有依据的学习路径。",
        "独立实现知识点优先级、依赖排序、间隔复习和进度统计，并设计 8 周、56 天暑期学习计划；每天包含学习主题、动手任务、产出要求、资料链接和复盘问题。",
        "形成可直接执行的长期学习计划工具，支持按周查看、每日打卡和复习状态管理；在线版本使用本地规则运行，不依赖模型密钥。",
        "https://github.com/xiaoyf-debug/ai-study-coach",
    )
    project_page(
        c, 3, "个人学习知识库", IMAGES / "project-study-notes.png",
        ["HTML", "CSS", "JavaScript", "LocalStorage", "资料检索"],
        "面向大学课程复习、知识整理和资料检索需求，开发无需服务器即可运行的个人学习档案。",
        "在笔记、错题和学习统计基础上新增课程资料中心，实现课程分类、资料类型识别、关键词搜索、组合筛选、课程概览及深浅色主题切换。",
        "形成集知识记录、错题复盘、课程资料检索和学习统计于一体的本地工具，并将第三方课程资料与公开代码仓库隔离。",
        "https://github.com/xiaoyf-debug/study_notes_web",
    )

    # Awards pages
    header(c, "AWARDS", "竞赛荣誉", "程序设计 · 数学竞赛")
    y = PAGE_H - 140
    y = award_block(c, y, IMAGES / "award-programming-gold.jpg", "中山大学程序设计新手赛（NVCPC26）", "金牌", "2026.04.18", "以团队成员身份参赛，完成算法分析、代码实现和程序调试，提升限时环境下的问题解决与协作能力。")
    award_block(c, y, IMAGES / "award-lanqiao-cpp-public.jpg", "第十七届蓝桥杯全国大学生软件和信息技术大赛", "C/C++ 程序设计大学 A 组广东赛区二等奖", "2026.05.08", "参加软件赛 C/C++ 程序设计大学 A 组比赛，锻炼算法应用、编程实现和限时调试能力。")
    footer(c, 4)
    c.showPage()

    header(c, "AWARDS", "数学竞赛与联系方式")
    award_block(c, PAGE_H - 140, IMAGES / "award-math-competition-public.jpg", "第十七届全国大学生数学竞赛（非数学 A 类）", "二等奖", "2025.11", "通过竞赛训练数学基础、逻辑推理、计算分析和复杂问题拆解能力。")
    c.setFillColor(TEXT)
    c.setFont("CN-Bold", 14)
    c.drawString(MARGIN, 300, "在线作品集")
    c.setFillColor(ACCENT)
    c.setFont("CN", 10)
    c.drawString(MARGIN, 276, "https://xiaoyf-debug.github.io/software-engineering-portfolio/")
    c.setFillColor(TEXT)
    c.setFont("CN-Bold", 14)
    c.drawString(MARGIN, 228, "联系方式")
    draw_text(c, "GitHub｜https://github.com/xiaoyf-debug", MARGIN, 202, 480, 10, 18)
    draw_text(c, "中大邮箱｜xiaoyf66@mail2.sysu.edu.cn", MARGIN, 180, 480, 10, 18)
    draw_text(c, "QQ 邮箱｜3868085823@qq.com", MARGIN, 158, 480, 10, 18)
    c.setFillColor(MUTED)
    c.setFont("CN", 8.5)
    c.drawString(MARGIN, 104, "感谢阅读，期待参与软件开发、后端开发或 AI 应用相关实习工作。")
    footer(c, 5)
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
