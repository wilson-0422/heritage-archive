from werkzeug.security import generate_password_hash
from app import db
from app.models import User, Inheritor, Collection, CraftStep, Exhibition, Reservation


def seed_data():
    admin = User(
        username="admin",
        password_hash=generate_password_hash("admin123"),
        role="admin",
    )
    db.session.add(admin)

    user = User(
        username="zhangsan",
        password_hash=generate_password_hash("123456"),
        role="user",
    )
    db.session.add(user)
    db.session.commit()

    inheritors_data = [
        {
            "name": "王秀英",
            "gender": "女",
            "birth_year": 1952,
            "category": "传统技艺",
            "heritage_item": "苏绣",
            "province": "江苏",
            "city": "苏州",
            "description": "国家级非物质文化遗产苏绣代表性传承人，从事苏绣创作五十余年，作品多次获国内外大奖。擅长双面绣与乱针绣技法，培养弟子三十余人。",
            "phone": "13800001001",
        },
        {
            "name": "李德明",
            "gender": "男",
            "birth_year": 1948,
            "category": "传统技艺",
            "heritage_item": "景德镇手工制瓷技艺",
            "province": "江西",
            "city": "景德镇",
            "description": "省级非物质文化遗产景德镇手工制瓷技艺传承人，精通拉坯、利坯、画坯、施釉等全套工序，尤其擅长青花瓷绘制。",
            "phone": "13800001002",
        },
        {
            "name": "赵玉芬",
            "gender": "女",
            "birth_year": 1960,
            "category": "传统美术",
            "heritage_item": "剪纸",
            "province": "陕西",
            "city": "延安",
            "description": "市级非物质文化遗产剪纸传承人，作品风格粗犷豪放，题材涵盖民俗故事、花鸟鱼虫，多次参加国际文化交流展览。",
            "phone": "13800001003",
        },
        {
            "name": "陈建国",
            "gender": "男",
            "birth_year": 1955,
            "category": "传统技艺",
            "heritage_item": "宣纸制作技艺",
            "province": "安徽",
            "city": "宣城",
            "description": "国家级非物质文化遗产宣纸制作技艺代表性传承人，掌握108道传统工序，尤其精通捞纸与焙纸工艺。",
            "phone": "13800001004",
        },
        {
            "name": "杨秀兰",
            "gender": "女",
            "birth_year": 1963,
            "category": "传统戏剧",
            "heritage_item": "昆曲",
            "province": "江苏",
            "city": "昆山",
            "description": "国家级非物质文化遗产昆曲代表性传承人，工闺门旦，嗓音清丽婉转，代表剧目《牡丹亭》《长生殿》等。",
            "phone": "13800001005",
        },
    ]

    inheritor_objs = []
    for data in inheritors_data:
        obj = Inheritor(**data)
        db.session.add(obj)
        inheritor_objs.append(obj)
    db.session.commit()

    collections_data = [
        {
            "name": "双面绣《猫蝶图》",
            "category": "刺绣",
            "inheritor_id": inheritor_objs[0].id,
            "year": 2018,
            "material": "丝线、绢布",
            "size": "45cm×45cm",
            "description": "苏绣经典双面绣作品，正面为白猫戏蝶，反面为花猫扑蝶，两面图案不同而针法统一，堪称苏绣绝技之典范。",
        },
        {
            "name": "青花瓷瓶《山水图》",
            "category": "陶瓷",
            "inheritor_id": inheritor_objs[1].id,
            "year": 2020,
            "material": "高岭土、釉料",
            "size": "高38cm 口径12cm",
            "description": "手工拉坯成型，青花分水技法绘制山水图景，层次分明，意境深远，体现景德镇传统制瓷工艺之精髓。",
        },
        {
            "name": "剪纸《百鸟朝凤》",
            "category": "剪纸",
            "inheritor_id": inheritor_objs[2].id,
            "year": 2019,
            "material": "红宣纸",
            "size": "60cm×80cm",
            "description": "大型剪纸作品，以百鸟朝凤为主题，构图饱满，线条流畅，展现陕北剪纸的独特艺术风格。",
        },
        {
            "name": "特种净皮宣纸",
            "category": "宣纸",
            "inheritor_id": inheritor_objs[3].id,
            "year": 2021,
            "material": "青檀皮、沙田稻草",
            "size": "138cm×69cm",
            "description": "采用传统108道工序手工制作，纸质绵韧、墨韵万变，为书画创作之上品。",
        },
        {
            "name": "昆曲戏服《杜丽娘》",
            "category": "戏曲服饰",
            "inheritor_id": inheritor_objs[4].id,
            "year": 2017,
            "material": "丝绸、金线、珠片",
            "size": "定制尺寸",
            "description": "昆曲《牡丹亭》杜丽娘角色专用戏服，手工刺绣花纹，金线盘扣，珠片点缀，精美绝伦。",
        },
        {
            "name": "乱针绣《江南春色》",
            "category": "刺绣",
            "inheritor_id": inheritor_objs[0].id,
            "year": 2022,
            "material": "丝线、绢布",
            "size": "80cm×60cm",
            "description": "乱针绣代表作，以交叉线条表现光影变化，描绘江南水乡春日景色，色彩丰富层次分明。",
        },
    ]

    collection_objs = []
    for data in collections_data:
        obj = Collection(**data)
        db.session.add(obj)
        collection_objs.append(obj)
    db.session.commit()

    crafts_data = [
        {"collection_id": collection_objs[0].id, "step_number": 1, "title": "选稿与描图", "description": "根据设计稿选择合适图案，用细笔在绢布上描出轮廓线，确保双面图案位置对应。", "duration": "2天"},
        {"collection_id": collection_objs[0].id, "step_number": 2, "title": "上绷与配线", "description": "将绢布上绷架绷紧，根据图案配色要求选取丝线，苏绣用线可劈至1/64细。", "duration": "1天"},
        {"collection_id": collection_objs[0].id, "step_number": 3, "title": "正面刺绣", "description": "先绣正面图案，采用平针、散套针等技法，逐层施色，注意针脚整齐、丝理顺畅。", "duration": "15天"},
        {"collection_id": collection_objs[0].id, "step_number": 4, "title": "反面刺绣", "description": "翻转绷架绣制反面图案，需与正面针脚互不干扰，双面绣的核心难点所在。", "duration": "15天"},
        {"collection_id": collection_objs[0].id, "step_number": 5, "title": "整理与装裱", "description": "刺绣完成后下绷，修剪边缘，熨烫平整，装入特制镜框展示。", "duration": "2天"},
        {"collection_id": collection_objs[1].id, "step_number": 1, "title": "揉泥与拉坯", "description": "将练好的瓷泥揉匀排气，在辘轳上拉坯成型，控制坯体厚薄均匀。", "duration": "1天"},
        {"collection_id": collection_objs[1].id, "step_number": 2, "title": "利坯与修坯", "description": "坯体半干时用利坯刀修整外形，使器型规整、线条流畅。", "duration": "1天"},
        {"collection_id": collection_objs[1].id, "step_number": 3, "title": "画坯", "description": "在素坯上用青花料绘制山水图案，采用分水技法表现浓淡层次。", "duration": "3天"},
        {"collection_id": collection_objs[1].id, "step_number": 4, "title": "施釉与烧制", "description": "施透明釉后入窑，经1300°C高温还原焰烧制，青花发色青翠幽靓。", "duration": "2天"},
        {"collection_id": collection_objs[2].id, "step_number": 1, "title": "起稿与折叠", "description": "在红宣纸上起稿画出大致轮廓，将纸张按需折叠，确定剪纸的对称方式。", "duration": "1天"},
        {"collection_id": collection_objs[2].id, "step_number": 2, "title": "剪刻", "description": "用剪刀和刻刀沿轮廓线剪刻，先刻细部再剪大形，刀法稳健流畅。", "duration": "3天"},
        {"collection_id": collection_objs[2].id, "step_number": 3, "title": "展开与修整", "description": "小心展开剪纸，检查有无断裂，用刻刀修整毛边和细节。", "duration": "1天"},
        {"collection_id": collection_objs[2].id, "step_number": 4, "title": "装裱展示", "description": "将剪纸作品托裱于白色卡纸上，装入镜框保存展示。", "duration": "1天"},
    ]

    for data in crafts_data:
        obj = CraftStep(**data)
        db.session.add(obj)
    db.session.commit()

    exhibitions_data = [
        {
            "title": "锦绣江南——苏绣艺术精品展",
            "location": "苏州博物馆",
            "start_date": "2024-03-15",
            "end_date": "2024-06-15",
            "description": "汇集苏绣传承人王秀英及其弟子历年精品力作，展示苏绣从传统到当代的艺术演变，涵盖双面绣、乱针绣等多种技法。",
            "status": "进行中",
            "capacity": 200,
        },
        {
            "title": "千年瓷韵——景德镇传统制瓷技艺展",
            "location": "景德镇中国陶瓷博物馆",
            "start_date": "2024-05-01",
            "end_date": "2024-09-30",
            "description": "全面展示景德镇手工制瓷技艺从泥到瓷的全过程，现场演示拉坯、画坯等工序，观众可亲身体验。",
            "status": "进行中",
            "capacity": 300,
        },
        {
            "title": "纸上乾坤——中国剪纸艺术大展",
            "location": "中国美术馆",
            "start_date": "2024-07-01",
            "end_date": "2024-10-31",
            "description": "汇聚全国各地剪纸流派代表作，展现剪纸艺术的多样风貌与深厚文化底蕴。",
            "status": "未开始",
            "capacity": 500,
        },
        {
            "title": "墨韵宣香——宣纸制作技艺体验展",
            "location": "中国宣纸文化园",
            "start_date": "2024-04-01",
            "end_date": "2024-12-31",
            "description": "沉浸式体验宣纸制作全过程，从原料采集到成品纸张，感受千年造纸智慧。",
            "status": "进行中",
            "capacity": 150,
        },
        {
            "title": "水磨雅韵——昆曲艺术传承展",
            "location": "昆山昆曲博物馆",
            "start_date": "2023-09-01",
            "end_date": "2024-03-01",
            "description": "展示昆曲六百年传承历程，含戏服、曲谱、道具等珍贵文物，配合现场演出。",
            "status": "已结束",
            "capacity": 180,
        },
    ]

    exhibition_objs = []
    for data in exhibitions_data:
        obj = Exhibition(**data)
        db.session.add(obj)
        exhibition_objs.append(obj)
    db.session.commit()

    reservations_data = [
        {
            "exhibition_id": exhibition_objs[0].id,
            "user_id": user.id,
            "name": "张三",
            "phone": "13900001111",
            "people_count": 3,
            "visit_date": "2024-04-20",
            "note": "希望安排讲解服务",
        },
        {
            "exhibition_id": exhibition_objs[1].id,
            "user_id": user.id,
            "name": "张三",
            "phone": "13900001111",
            "people_count": 5,
            "visit_date": "2024-06-15",
            "note": "团队参观，需提前预约",
        },
        {
            "exhibition_id": exhibition_objs[3].id,
            "user_id": admin.id,
            "name": "管理员",
            "phone": "13800001000",
            "people_count": 2,
            "visit_date": "2024-05-10",
            "note": "考察调研",
        },
    ]

    for data in reservations_data:
        obj = Reservation(**data)
        db.session.add(obj)
    db.session.commit()

    print("种子数据导入完成！")
