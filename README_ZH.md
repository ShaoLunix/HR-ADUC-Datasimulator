# HR-ADUC-Datasimulator

HR-ADUC-Datasimulator 是一个用于生成 Active Directory 用户和组属性模拟数据的 Python 脚本。它旨在通过使用模拟数据而不是真实用户信息来促进数据提取过程的测试和演示，并保持机密性。

## 先决条件

为了正常运行，此脚本需要满足以下先决条件：
1. 在运行脚本的计算机上安装Python。该脚本开发所使用的版本为3.12.2。建议使用3.6或更高版本。
2. 安装以下模块：
    a. pandas：
        此库提供数据结构和数据分析工具。
    b. configparser：
        此模块允许使用INI格式配置文件。
    c. Faker：
        此库生成虚假数据，如姓名、地址、电话号码等。
    d. random或random2：
        这些模块提供生成随机数的函数。
    e. math：
        此模块提供一组标准数学函数，如三角函数、指数函数、对数函数等。
    f. unidecode：
        此模块将Unidecode字符串转换为ASCII。

configparser、random和math模块通常包含在Python中。
pandas、Faker和unidecode模块是外部包。

## 特点

- 生成随机数据以模拟提取 Active Directory (AD) 帐户的属性。
- 在不泄露真实用户信息的情况下帮助演示数据提取过程。
- 允许测试和验证 AD 帐户与人力资源 (HR) 提取之间的数据一致性。
- 强调异常并建议修改以改善 ADUC 服务器上的安全性。

## 用法

1. 克隆或下载存储库到本地计算机。
2. 复制与您语言对应的parameters_[XX].ini文件，并将其简单重命名为parameters.ini。
3. 自定义 parameters.ini 文件以定义数据生成过程的特定设置。
4. 运行 HR-ADUC-Datasimulator.py 脚本生成模拟数据。
5. 分析输出并用于测试、演示或安全性改进目的。

## 许可证

HR-ADUC-Datasimulator 根据 GNU Lesser General Public License v3.0 (LGPL-3.0) 许可。您可以根据许可的条款使用、修改和分发此脚本。

有关更多详细信息，请参阅 [LICENSE](https://github.com/ShaoLunix/HR-ADUC-Datasimulator/blob/main/LICENSE) 文件。

## 贡献

欢迎为此项目做出贡献。如果您遇到任何问题，有改进建议或想要贡献新功能，请在 GitHub 上开启一个问题或提交拉取请求。

## 免责声明

此脚本按“原样”提供，没有任何形式的保证或担保。自行决定使用。

## 作者

Stéphane-Hervé

## 联系方式

如有任何问题、反馈或支持，请联系 https://github.com/ShaoLunix/HR-ADUC-Datasimulator/issues。
