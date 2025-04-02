# AutoGen Demo

## 项目简介
本项目是一个基于AutoGen框架的智能代理系统演示，主要功能包括：

1. 天气查询：通过OpenWeatherMap API获取指定城市的实时天气信息
2. 地址映射：根据城市名称映射对应的邮件地址
3. 邮件发送：将天气信息通过邮件发送给指定收件人

系统由三个智能代理组成：
- 天气代理：负责查询多个城市的天气信息
- 地址映射代理：将城市与邮件地址进行匹配
- 邮件代理：负责发送包含天气信息的邮件

项目展示了如何使用AutoGen框架构建多代理协作系统，实现复杂任务的自动化处理。


## 安装指南
### 依赖安装
确保你已经安装了以下依赖：
- Python 3.10+
- pip

### 安装步骤
1. 克隆项目仓库：
   ```bash
   git clone git@github.com:simson2010/autogen-demo.git
   ```
2. 进入项目目录：
   ```bash
   cd autogen-demo
   ```
3. 安装项目依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用说明
### 运行项目
```bash
python main.py
```

## 环境变量配置

### Windows
1. 右键点击"此电脑" -> "属性"
2. 选择"高级系统设置" -> "环境变量"
3. 在"系统变量"部分，点击"新建"
4. 变量名输入：`OPENAI_API_KEY`
5. 变量值输入：你的API密钥
6. 点击"确定"保存

### Linux
1. 打开终端
2. 编辑~/.bashrc文件：
   ```bash
   nano ~/.bashrc
   ```
3. 在文件末尾添加：
   ```bash
   export OPENAI_API_KEY="你的API密钥"
   ```
4. 保存并退出
5. 使更改生效：
   ```bash
   source ~/.bashrc
   ```

### macOS
1. 打开终端
2. 编辑~/.zshrc文件：
   ```bash
   nano ~/.zshrc
   ```
3. 在文件末尾添加：
   ```bash
   export OPENAI_API_KEY="你的API密钥"
   ```
4. 保存并退出
5. 使更改生效：
   ```bash
   source ~/.zshrc
   ```


## 项目结构 
