define zmw = Character("庄茗薇", color="#fff8c8")
define I = Character("我", color="#fffe00")
define config.adjust_view_size = True
image zmw gaolen = "images/zmw/zmw_gaolen.jpeg"
image bg classroom = "images/classroom@1.77.jpeg"

label start:
    scene bg classroom:
        with fade
    
    I "进入高二了，或许我今年该认真学习了..."
    I "现在教室还没人..."
    "一个女生走了进来"
    show zmw gaolen:
        zoom 0.25
        with dissolve
        at right
    "她准备坐到我的旁边的单排座位"
    menu:
        "我应该干什么？"
        
        "喝口水，假装没注意到她":
            "她似乎撇了我一眼..."
            hide zmw gaolen with dissolve
            "很快就上课了，一天就过去了"
            
        "跟她打个招呼试试？":
            I "额...你好？"
            zmw "嗯"
            "她看了我一眼"
            hide zmw gaolen with dissolve
            "很快就上课了，一天就过去了"
            
    return