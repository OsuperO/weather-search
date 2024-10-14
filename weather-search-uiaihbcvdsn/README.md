<!--
 * @Author: = dengyy
 * @Date: 2024-08-12 10:37:21
 * @LastEditors: = dengyy
 * @LastEditTime: 2024-08-14 15:10:54
 * @FilePath: \jyzx-sidePanel-crx\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 项目背景
1. 根据文档完成一个侧边栏的插件项目搭建


# 参考文档
1. 微信公众号文章：2023新春版：React+Antd开发Chrome插件教程（Manifest V3）
2. https://doc.yilijishu.info/chrome/getstarted.html

# 参考项目
1. yjj的项目：https://github.com/995854654/forty-extension


# 扩展程序的结构
1. 插件的后台脚本入口文件是background/index.js
2. 插件的内容入口脚本文件是content/index.js
3. 插件的小窗口入口文件是popup/index.js
4. 插件的侧边栏入口文件是sidePanel/index.js


# 文件结构解释
```txt
// src文件夹下的目录树
├─api     // 项目所有的接口路由配置
│      index.js  // 总接口配置，后端接口，以及插件监听目标页面的api接口
│      lhjybt_api.js  // 插件监听灵活就业补贴的api接口
│      xnjyknrysbbt_api.js  // 插件监听吸纳就业苦难补贴的api接口
│      
├─background  // 后台代码
│      index.js
│      
├─common  // 通用包
│  ├─css  // 通用css
│  │      frame.css  
│  │      global.css
│  │      reset.css
│  │      
│  ├─js
│  │      CommonConstants.js  // 常量配置
│  │      subsidyConfig.js  // 补贴相关配置
│  │      
│  └─utils
│          common.js  // 通用工具
│          DateUtils.js  // 日期工具
│          Logger.js  // 日志工具
│          xpathAction.js  // xpath操作工具
│          
├─content  // content_script注入脚本
│  │  content.less
│  │  ContentMain.jsx  // content_script主组件。
│  │  index.js   // content_script入口文件
│  │  
│  ├─columns
│  │      columnsTotal.js
│  │      
│  └─components
│      ├─FloatWindow  // 悬浮窗口
│      │      floatWindow.less
│      │      index.jsx
│      │      
│      ├─MainDrawer  // 抽屉窗口
│      │      index.jsx
│      │      
│      ├─ProvinceDataShow  // 补贴类数据展示组件。
│      │      index.jsx
│      │      
│      └─subsidy  // 细化每个补贴类数据展示组件
│              LhjybtDataShow.jsx  // 灵活就业补贴数据展示
│              XnjyknsbbtDataShow.jsx  // 吸纳就业补贴数据展示
├─sidePanel  // 侧边栏
│    │ 
│    └─components
│       └─sidePanel.jsx // 侧边栏主组件
│              
└─popup  // 插件小窗口
    │  index.js  // 入口文件
    │  popup.css  // 入口样式
    │  
    ├─components
    ├─pages  // 页面
    │  ├─Home  // 主页
    │  └─Login  // 登录页面
    │          index.jsx
    │          login.less
    │          
    └─router // 小窗口的路由配置
            index.js
            
```

# 获取宿主页面的cookie
1.由于浏览器的限制,需要进行对浏览器的samesite进行设置才能获取到cookie,故放弃使用插件获取cookie

# 功能设计
## 1. 预审结果展示
    · 当宿主页面跳转到单位/人员详情页是自动获取该单位/人员预审结果，并将结果展示到页面上
    · 在想，如果是非详情页面时是不是还可以展示也写别的信息，比如可疑名单中的单位/人员
## 2. 

## 3. 登录
    · 登录页面支持注册、登录


## 3. 个人中心
    · 管理员 可管理下级成员，添加、删除下级成员、调整下级成员权限
