# 非遗文化数字化档案系统

## 项目简介

非遗文化数字化档案系统是一个基于 Python Flask 框架构建的 Web 应用，旨在对非物质文化遗产进行数字化管理与展示。系统涵盖非遗传承人资料管理、手作藏品档案、工艺步骤记录、线下展演管理、研学预约以及藏品线上展馆等核心功能模块，为非遗文化的保护、传承与传播提供信息化支撑。

## 适用场景

- **非遗保护机构**：对区域内非遗项目及传承人进行系统化档案管理
- **文化馆/博物馆**：管理藏品信息、策划线下展览、接受公众预约参观
- **研学教育基地**：组织非遗研学活动，管理预约与参观数据
- **学术研究**：为非遗研究提供结构化数据支持与检索服务
- **文化推广**：通过线上展馆向公众展示非遗文化魅力

## 核心功能

1. **非遗传承人管理**：录入、编辑、查看传承人基本信息，包括姓名、性别、出生年份、非遗类别、传承项目、地区等
2. **手作藏品档案**：管理非遗手作藏品，记录名称、类别、年代、材质、尺寸、描述等详细信息
3. **工艺步骤记录**：为每件藏品记录完整的制作工艺步骤，包括步骤序号、名称、详细说明、耗时等
4. **线下展演管理**：创建和管理展览活动，记录展览名称、地点、时间、状态、容量等
5. **研学预约**：用户可在线预约参观展览，填写参观人数、日期、联系方式等
6. **藏品线上展馆**：以列表和详情形式在线展示藏品，支持按类别浏览
7. **用户认证**：支持用户注册、登录，区分管理员和普通用户角色
8. **数据看板**：提供系统数据概览，包括传承人数量、藏品数量、展览数量等统计

## 技术栈

- **后端框架**：Python 3.11 + Flask 3.0
- **ORM**：Flask-SQLAlchemy 3.1
- **数据库**：SQLite
- **用户认证**：Flask-Login 0.6
- **模板引擎**：Jinja2
- **前端**：HTML5 + CSS3 + JavaScript（原生）
- **容器化**：Docker

## 目录结构

```
repo/
├── app.py                  # 应用入口
├── config.py               # 配置文件
├── seed.py                 # 种子数据
├── requirements.txt        # Python 依赖
├── app/
│   ├── __init__.py         # Flask 应用工厂
│   ├── models/             # 数据模型
│   │   ├── user.py         # 用户模型
│   │   ├── inheritor.py    # 传承人模型
│   │   ├── collection.py   # 藏品模型
│   │   ├── craft_step.py   # 工艺步骤模型
│   │   ├── exhibition.py   # 展览模型
│   │   └── reservation.py  # 预约模型
│   ├── routes/             # 路由控制器
│   │   ├── auth.py         # 认证路由
│   │   ├── inheritors.py   # 传承人路由
│   │   ├── collections.py  # 藏品路由
│   │   ├── crafts.py       # 工艺步骤路由
│   │   ├── exhibitions.py  # 展览路由
│   │   ├── reservations.py # 预约路由
│   │   └── main.py         # 主页路由
│   ├── services/           # 业务逻辑层
│   │   ├── user_service.py
│   │   ├── inheritor_service.py
│   │   ├── collection_service.py
│   │   ├── craft_service.py
│   │   ├── exhibition_service.py
│   │   └── reservation_service.py
│   ├── templates/          # Jinja2 模板
│   └── static/             # 静态资源
│       ├── css/style.css
│       └── js/main.js
```

## Docker 启动方式

```bash
# 构建镜像
docker build -t heritage-archive .

# 运行容器
docker run -d \
  -p 5000:5000 \
  -p 2222:22 \
  -e SECRET_KEY=your-secret-key \
  -e SSH_PUBLIC_KEY="$(cat ~/.ssh/id_rsa.pub)" \
  --name heritage-archive \
  heritage-archive
```

访问 http://localhost:5000 即可使用系统。

## 本地启动方式

```bash
cd repo/

# 安装依赖
pip install -r requirements.txt

# 启动应用（首次启动会自动创建数据库并导入种子数据）
python app.py
```

访问 http://localhost:5000 即可使用系统。

## 默认账号

| 用户名   | 密码      | 角色   |
|---------|-----------|--------|
| admin   | admin123  | 管理员  |
| zhangsan| 123456    | 普通用户 |

## 可扩展方向

1. **多媒体支持**：增加图片、音频、视频上传功能，丰富非遗档案的媒体形式
2. **全文检索**：集成 Elasticsearch 或 Whoosh，实现对传承人、藏品的全文搜索
3. **地图可视化**：接入地图 API，展示传承人地理分布和展览位置
4. **权限管理**：细化角色权限体系，支持多级审核流程
5. **数据导出**：支持将档案数据导出为 PDF、Excel 等格式
6. **API 接口**：构建 RESTful API，支持移动端和第三方系统对接
7. **社交互动**：增加评论、点赞、分享功能，促进非遗文化传播
8. **数据备份**：实现数据库自动备份与恢复机制
9. **多语言支持**：增加英文等语言版本，便于国际文化交流
10. **智能推荐**：基于用户浏览记录推荐相关藏品和展览
