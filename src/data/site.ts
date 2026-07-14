/** 集中维护站点内容，替换此文件即可填充个人素材。 */
export const siteConfig = {
  title: '肖雨菲 · 软件工程作品集',
  description: '肖雨菲的软件工程求职、项目作品与竞赛荣誉个人作品集。',
  profile: {
    avatar: '/images/avatar-alternate.jpg',
    name: '肖雨菲',
    summary: '中山大学软件工程专业学生，关注程序设计、算法与软件项目实践。',
    skills: ['C / C++', 'Python', 'Git / GitHub', '算法基础', 'AI 辅助开发'],
    githubUrl: 'https://github.com/xiaoyf-debug',
    emails: [
      { label: 'QQ 邮箱', address: '3868085823@qq.com' },
      { label: '中大邮箱', address: 'xiaoyf66@mail2.sysu.edu.cn' },
    ],
  },
  highlights: [
    { value: '3 项', label: '竞赛荣誉' },
    { value: '2 个', label: '实践项目' },
  ],
  navigation: [
    { label: '首页', href: '/' },
    { label: '关于我', href: '/about' },
    { label: '竞赛荣誉', href: '/awards' },
    { label: '项目作品', href: '/projects' },
  ],
  footerText: '保持学习，持续实践，用可靠的代码解决真实问题。',
};

/** 荣誉数据可直接追加对象，由页面批量循环渲染。 */
export const awards = [
  {
    image: '/images/award-programming-gold.jpg',
    title: '2026 年中山大学程序设计新手赛（NVCPC26）',
    award: '金牌',
    date: '2026 年 4 月 18 日',
    role: '团队成员',
    description: '参加中山大学计算机学院举办的程序设计新手赛并取得金牌。',
  },
  {
    image: '/images/award-lanqiao-cpp-public.jpg',
    title: '第十七届蓝桥杯全国大学生软件和信息技术大赛',
    award: '广东赛区二等奖',
    date: '2026 年 5 月 8 日',
    role: '个人参赛',
    description: '参加软件赛 C/C++ 程序设计大学 A 组比赛，获得广东赛区二等奖。',
  },
  {
    image: '/images/award-math-competition-public.jpg',
    title: '第十七届全国大学生数学竞赛（非数学 A 类）',
    award: '二等奖',
    date: '2025 年 11 月',
    role: '个人参赛',
    description: '参加全国大学生数学竞赛非数学 A 类比赛并获得二等奖。',
  },
] satisfies Array<{
  image: string;
  title: string;
  award: string;
  date: string;
  role: string;
  description: string;
}>;

/** “关于我”页面内容；空字符串会显示为待填写提示。 */
export const aboutConfig = {
  portrait: '/images/profile-photo.jpg',
  introduction: '中山大学软件工程专业在读，计划向 AI 与算法方向持续发展。具备良好的学习主动性与责任意识，做事认真细致，乐于探索新技术，并注重将所学知识落实到代码实践与问题解决中。',
  jobTarget: '软件开发实习生｜后端开发实习生｜AI 辅助开发实习生',
  education: {
    school: '中山大学',
    major: '软件工程',
    period: '2025.08—至今',
  },
  strengths: [
    'C/C++：熟练使用 C/C++，能够独立完成程序设计、编码实现、运行调试与常见问题排查。',
    'Python：掌握 Python 基础语法与常用开发方式，能够编写实用脚本，并应用于基础 Web 项目实践。',
    '开发与调试：熟悉 Dev-C++ 等开发工具，具备从代码编写、编译运行到错误定位的完整实践能力。',
    'AI 辅助开发：熟练使用 GitHub Copilot、Codex 等工具辅助编码、理解代码与排查问题，并坚持核验代码逻辑、运行结果及实现可靠性。',
  ],
  coursework: ['程序设计Ⅰ', '程序设计Ⅱ', '数学分析', '高等代数'],
  currentFocus: [
    '持续巩固数据结构、算法和 C/C++ 编程基础。',
    '学习 Node.js 后端开发、接口设计和基础数据管理。',
    '探索 AI API 在学习规划、内容总结和辅助开发场景中的可靠应用。',
  ],
  nearTermPlan: [
    '完善 AI 学习规划与复盘助手的提醒、趋势分析和薄弱知识点追踪能力。',
    '补充后端开发、数据库和工程化测试相关实践。',
    '在项目实践中持续沉淀调试经验、阶段复盘和 AI 代码核验方法。',
  ],
};

/** 项目数据仅定义结构，不填充具体项目内容。 */
export const projects = [
  {
    image: '/images/project-ai-study-coach.png',
    title: 'AI 学习规划与复盘助手',
    period: '2026.07—至今',
    status: '持续开发中',
    technologies: ['Node.js', 'JavaScript', 'OpenAI API', 'LocalStorage', '响应式设计', '持续开发中'],
    contribution: '独立设计学习目标、知识点优先级、执行计划与复习反馈的数据闭环；实现知识点录入、掌握度与难度评估、学习路径排序、间隔复习，以及详细的 8 周暑期学习计划。计划覆盖 56 天内容，支持按周查看每日学习主题、动手任务、产出要求、资料链接和复盘问题。',
    result: '形成可直接执行的长期学习计划工具，可统计计划完成进度、紧急知识点、复习任务和预计学习时长。用户能够完成每日打卡、记录学习状态，并根据掌握情况动态安排后续复习。在线版本使用本地规则完成规划与建议，不依赖模型密钥。',
    highlights: ['8 周 56 天详细学习计划', '知识点优先级与依赖排序', '每日任务、资料与复盘问题', '计划进度和间隔复习管理'],
    engineering: '将暑期计划拆分为独立数据模块，通过 LocalStorage 保存知识点、计划进度与复习状态；对用户内容进行 HTML 转义，并为 GitHub Pages 提供无需服务端的本地演示模式。',
    demoUrl: 'https://xiaoyf-debug.github.io/ai-study-coach/',
    repositoryUrl: 'https://github.com/xiaoyf-debug/ai-study-coach',
  },
  {
    image: '/images/project-study-notes.png',
    title: '个人学习知识库',
    period: '2026.07—至今',
    status: '持续开发中',
    technologies: ['HTML', 'CSS', 'JavaScript', 'LocalStorage', 'Python', '资料分类检索'],
    contribution: '围绕大学课程复习与资料整理需求，持续扩展离线学习知识库。除笔记、错题和学习统计外，新增课程资料中心，对本地资料和公开学习链接进行课程分类、资料类型识别、关键词搜索及组合筛选，并增加课程概览和深浅色主题切换。',
    result: '形成集知识记录、错题复盘、课程资料检索和学习统计于一体的本地学习档案。当前资料中心覆盖软件工程、计算机组成原理、离散数学、数据结构与算法等课程；第三方教材与答案仅保存在个人本地环境，不随公开仓库分发。',
    highlights: ['课程资料分类与组合筛选', '笔记与错题本地管理', '课程概览和学习统计', '深浅色主题与响应式界面'],
    engineering: '通过统一资料元数据管理本地文件与外部链接，按课程和文件类型动态分组；使用 LocalStorage 保存个人笔记、错题与界面主题，同时将受版权保护的课程资料与公开代码仓库隔离。',
    demoUrl: 'https://xiaoyf-debug.github.io/software-engineering-portfolio/study-notes/index.html',
    repositoryUrl: 'https://github.com/xiaoyf-debug/study_notes_web',
  },
] satisfies Array<{
  image: string;
  title: string;
  period: string;
  status: string;
  technologies: string[];
  contribution: string;
  result: string;
  highlights: string[];
  engineering: string;
  demoUrl: string;
  repositoryUrl: string;
}>;
